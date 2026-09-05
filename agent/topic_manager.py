"""
topic_manager.py
Handles picking the next topic to learn.
Priority: topics_queue.json → Gemini auto-generates next topic
"""

import json
import os
import re
from datetime import datetime


TOPICS_FILE = "data/topics_queue.json"


def load_topics() -> dict:
    if os.path.exists(TOPICS_FILE):
        with open(TOPICS_FILE) as f:
            return json.load(f)
    return {"pending": [], "completed": [], "last_picked": None}


def save_topics(data: dict):
    with open(TOPICS_FILE, "w") as f:
        json.dump(data, f, indent=2)


def pick_topic(model, knowledge_entries: list) -> str:
    """
    Returns the next topic to learn.
    Uses queue first, then asks Gemini to suggest one.
    """
    topics = load_topics()

    # ── Use queue if available ─────────────────────────
    if topics["pending"]:
        topic = topics["pending"].pop(0)
        topics["completed"].append(topic)
        topics["last_picked"] = topic
        save_topics(topics)
        print(f"📋 From queue: {topic}")
        return topic

    # ── Queue empty → ask Gemini to suggest next ───────
    print("📋 Queue empty — asking Gemini for next topic...")

    already_learned = [e["topic"] for e in knowledge_entries[-30:]]
    completed       = topics.get("completed", [])[-30:]

    prompt = f"""You are managing a coding knowledge base for a developer learning system.

Topics already learned (do NOT repeat these):
{json.dumps(already_learned + completed, indent=2)}

Suggest ONE new specific coding topic that:
- Is NOT in the list above
- Is practically useful for developers in real jobs
- Is a specific subtopic, not broad (e.g. "Python generators vs list comprehensions" not just "Python")
- Covers a different area than the last 5 topics learned

Reply with ONLY the topic name. No explanation, no numbering, no quotes."""

    response = model.generate_content(prompt)
    topic    = response.text.strip().strip('"').strip("'")

    # Clean up any accidental formatting
    topic = re.sub(r"^[\d\.\-\*]+\s*", "", topic).strip()

    topics["completed"].append(topic)
    topics["last_picked"] = topic
    save_topics(topics)

    print(f"🤖 Gemini suggested: {topic}")
    return topic
