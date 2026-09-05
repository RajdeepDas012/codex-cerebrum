"""
agent.py  ←  Main entry point
─────────────────────────────────────────────────────────────────
Run manually:  python agent/agent.py
Run via CI:    GitHub Actions calls this automatically

Flow:
  1. Load existing knowledge base
  2. Pick next topic to learn
  3. Ask Gemini to learn it deeply (structured JSON)
  4. Save to knowledge_base.json
  5. Write daily markdown log
  6. Export training pair to JSONL
  7. Update README stats
  GitHub Actions then commits everything.
─────────────────────────────────────────────────────────────────
"""

import sys
import os
import json
from datetime import datetime, timezone, date

# Add project root to path so imports work from both
# root (python agent/agent.py) and agent dir
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import google.generativeai as genai

from agent.topic_manager import pick_topic
from agent.learner       import learn_topic
from agent.logger        import write_daily_log, update_readme
from agent.exporter      import export_entry, get_export_stats


# ── File paths (relative to project root) ──────────────
KNOWLEDGE_FILE = "data/knowledge_base.json"


# ── Helpers ─────────────────────────────────────────────
def load_knowledge() -> dict:
    if os.path.exists(KNOWLEDGE_FILE):
        with open(KNOWLEDGE_FILE) as f:
            return json.load(f)
    return {
        "meta": {
            "project":              "Gemini Coding Brain",
            "description":          "Auto-generated coding knowledge base",
            "started":              date.today().isoformat(),
            "total_runs":           0,
            "last_updated":         None,
            "total_topics_learned": 0
        },
        "entries": []
    }


def save_knowledge(data: dict):
    os.makedirs("data", exist_ok=True)
    with open(KNOWLEDGE_FILE, "w") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


def already_learned(topic: str, entries: list) -> bool:
    """Avoid learning the exact same topic twice."""
    learned = {e["topic"].lower().strip() for e in entries}
    return topic.lower().strip() in learned


# ── Main ────────────────────────────────────────────────
def main():
    print("\n" + "═" * 50)
    print("🤖  GEMINI CODING BRAIN — Starting")
    print("═" * 50)

    # ── 1. Setup Gemini ──────────────────────────────
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        print("❌  GEMINI_API_KEY not set. Exiting.")
        sys.exit(1)

    genai.configure(api_key=api_key)
    model = genai.GenerativeModel("gemini-3.5-flash-lite")
    print("✅  Gemini connected")

    # ── 2. Load existing knowledge ───────────────────
    knowledge = load_knowledge()
    entries   = knowledge["entries"]
    meta      = knowledge["meta"]

    print(f"📚  Knowledge base: {len(entries)} entries so far")

    # ── 3. Pick topic ────────────────────────────────
    topic = pick_topic(model, entries)

    # Skip if already learned
    if already_learned(topic, entries):
        print(f"⏭️   Already learned '{topic}' — skipping")
        topic = pick_topic(model, entries)   # try once more

    # ── 4. Learn it ──────────────────────────────────
    print(f"\n📖  Learning: {topic}")
    print("    Asking Gemini...")

    entry = learn_topic(model, topic, entries[-10:])

    # Stamp run number
    meta["total_runs"]           += 1
    meta["total_topics_learned"] += 1
    meta["last_updated"]          = datetime.now(timezone.utc).isoformat()

    if not meta.get("started"):
        meta["started"] = date.today().isoformat()

    entry["run_number"] = meta["total_runs"]

    # ── 5. Save knowledge base ───────────────────────
    knowledge["entries"].append(entry)
    knowledge["meta"] = meta
    save_knowledge(knowledge)
    print(f"💾  Saved to {KNOWLEDGE_FILE}")

    # ── 6. Write daily log ───────────────────────────
    write_daily_log(entry, meta["total_runs"])

    # ── 7. Export training pair ──────────────────────
    export_entry(entry)
    stats = get_export_stats()
    print(f"📦  Export: {stats['total_pairs']} training pairs ({stats['file_size_kb']} KB)")

    # ── 8. Update README ─────────────────────────────
    update_readme(knowledge)

    # ── Done ─────────────────────────────────────────
    print("\n" + "═" * 50)
    print(f"✅  Run #{meta['total_runs']} complete!")
    print(f"🧠  Learned: {topic}")
    print(f"📊  Category: {entry.get('category', 'N/A')} | Difficulty: {entry.get('difficulty', 'N/A')}")
    print("═" * 50 + "\n")


if __name__ == "__main__":
    main()
