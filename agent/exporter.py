"""
exporter.py
Exports knowledge entries to JSONL format for future model fine-tuning.
Each line = one training example in instruction/output format.
"""

import json
import os


EXPORT_FILE = "export/finetune_ready.jsonl"


def entry_to_training_pair(entry: dict) -> list[dict]:
    """
    Convert one knowledge entry into multiple training pairs.
    More pairs = richer fine-tuning signal later.
    """
    topic = entry.get("topic", "")
    pairs = []

    # ── Pair 1: General explanation ───────────────────
    output_lines = [entry.get("summary", "")]

    if entry.get("key_points"):
        output_lines.append("\nKey Points:")
        output_lines += [f"- {p}" for p in entry["key_points"]]

    if entry.get("best_practices"):
        output_lines.append("\nBest Practices:")
        output_lines += [f"- {p}" for p in entry["best_practices"]]

    pairs.append({
        "instruction": f"Explain {topic} clearly with key points and best practices.",
        "input":       "",
        "output":      "\n".join(output_lines)
    })

    # ── Pair 2: Code example ──────────────────────────
    if entry.get("code_example"):
        ex = entry["code_example"]
        pairs.append({
            "instruction": f"Show me a code example for {topic}.",
            "input":       "",
            "output":      f"{ex.get('description', '')}\n\n```{ex.get('language', '')}\n{ex.get('correct', '')}\n```"
        })

        if ex.get("wrong"):
            pairs.append({
                "instruction": f"What is the common mistake when using {topic}?",
                "input":       "",
                "output":      f"Common mistake:\n```{ex.get('language', '')}\n{ex['wrong']}\n```\n\nCorrect approach:\n```{ex.get('language', '')}\n{ex.get('correct', '')}\n```"
            })

    # ── Pair 3: When to use ───────────────────────────
    if entry.get("when_to_use") and entry.get("when_not_to_use"):
        pairs.append({
            "instruction": f"When should I use {topic} and when should I avoid it?",
            "input":       "",
            "output":      f"Use it when: {entry['when_to_use']}\n\nAvoid it when: {entry['when_not_to_use']}"
        })

    # ── Pair 4: Interview Q&A ─────────────────────────
    for qa in entry.get("interview_questions", []):
        pairs.append({
            "instruction": qa.get("question", ""),
            "input":       "",
            "output":      qa.get("answer", "")
        })

    return pairs


def export_entry(entry: dict):
    """Append one knowledge entry as multiple JSONL training lines."""
    os.makedirs("export", exist_ok=True)

    pairs = entry_to_training_pair(entry)

    with open(EXPORT_FILE, "a", encoding="utf-8") as f:
        for pair in pairs:
            f.write(json.dumps(pair, ensure_ascii=False) + "\n")

    print(f"📦 Exported {len(pairs)} training pairs → {EXPORT_FILE}")


def get_export_stats() -> dict:
    """Return stats about the current export file."""
    if not os.path.exists(EXPORT_FILE):
        return {"total_pairs": 0, "file_size_kb": 0}

    with open(EXPORT_FILE) as f:
        lines = [l for l in f.readlines() if l.strip()]

    size_kb = round(os.path.getsize(EXPORT_FILE) / 1024, 1)
    return {"total_pairs": len(lines), "file_size_kb": size_kb}
