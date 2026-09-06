"""
learner.py
Sends a topic to Gemini and returns a structured knowledge entry.
Category is determined by a separate focused Gemini call —
no hardcoded keywords, works for any topic forever.
"""

import json
import re
from datetime import datetime, timezone


# ── Fixed category list — Gemini MUST pick from these ──
VALID_CATEGORIES = [
    "crypto-blockchain",
    "stocks-markets",
    "trading-strategies",
    "technical-analysis",
    "probability-math",
    "market-analysis",
    "data-visualization",
    "language-specific",
    "algorithms",
    "data-structures",
    "web-dev",
    "devops",
    "databases",
    "security",
    "testing",
    "system-design",
    "networking",
    "machine-learning",
    "best-practices",
    "debugging",
    "tools",
]


def clean_json_response(raw: str) -> str:
    """Strip markdown fences and whitespace from Gemini response."""
    raw = raw.strip()
    raw = re.sub(r"^```(?:json)?\s*", "", raw)
    raw = re.sub(r"\s*```$",          "", raw)
    return raw.strip()


def get_category(model, topic: str) -> str:
    """
    Ask Gemini to pick ONE category from the fixed list.
    Separate short call — cheap, fast, focused.
    Validates response — falls back to best-practices if invalid.
    """
    categories_list = "\n".join(f"- {c}" for c in VALID_CATEGORIES)

    prompt = f"""Categorize this topic into EXACTLY ONE category from the list below.

Topic: "{topic}"

Valid categories — pick ONLY from these:
{categories_list}

Rules:
- Reply with ONLY the category name
- No explanation, no punctuation, no extra words
- Must match exactly one category from the list above
- Think carefully — crypto topics go in crypto-blockchain,
  chart indicators go in technical-analysis,
  buy/sell strategies go in trading-strategies,
  probability and math go in probability-math,
  news and sentiment go in market-analysis"""

    try:
        response = model.generate_content(prompt)
        category = response.text.strip().lower().strip()

        # Clean up any accidental punctuation or spaces
        category = re.sub(r"[^a-z0-9\-]", "", category)

        if category in VALID_CATEGORIES:
            print(f"   Category: {category}")
            return category

        # Gemini returned something invalid — try to find closest match
        for valid in VALID_CATEGORIES:
            if valid in category or category in valid:
                print(f"   Category (fuzzy match): {valid}")
                return valid

        # Nothing matched — use best-practices
        print(f"   Category invalid ('{category}') — using best-practices")
        return "best-practices"

    except Exception as e:
        print(f"   Category call failed ({e}) — using best-practices")
        return "best-practices"


def learn_topic(model, topic: str, recent_entries: list) -> dict:
    """
    Ask Gemini to deeply learn a topic.
    Returns a structured dict ready to save.
    """

    # ── Step 1: Get category (separate focused call) ───
    category = get_category(model, topic)

    # ── Step 2: Build context from recent entries ──────
    context = ""
    if recent_entries:
        context = f"""
Recently learned topics (avoid repeating same examples):
{json.dumps([{"topic": e["topic"], "category": e["category"]} for e in recent_entries[-5:]], indent=2)}
"""

    # ── Step 3: Learn the topic deeply ────────────────
    prompt = f"""You are an expert teacher building a structured knowledge base.
{context}
Topic to learn: "{topic}"
Category: "{category}"

Reply ONLY with valid JSON. No markdown. No text outside JSON.

{{
  "topic": "{topic}",
  "category": "{category}",
  "language": "primary language or language-agnostic",
  "difficulty": "beginner | intermediate | advanced",
  "summary": "Clear 2-3 sentence explanation. What it is and why it matters.",
  "key_points": [
    "Specific important point 1",
    "Specific important point 2",
    "Specific important point 3",
    "Specific important point 4"
  ],
  "code_example": {{
    "language": "python or javascript or bash etc",
    "description": "One sentence: what this code demonstrates",
    "correct": "working correct code example here",
    "wrong": "common mistake people make"
  }},
  "common_mistakes": [
    "Specific mistake 1",
    "Specific mistake 2"
  ],
  "best_practices": [
    "Actionable best practice 1",
    "Actionable best practice 2",
    "Actionable best practice 3"
  ],
  "when_to_use": "Short explanation of when this is the right choice",
  "when_not_to_use": "Short explanation of when to avoid this",
  "interview_questions": [
    {{
      "question": "A real interview question about this topic?",
      "answer": "Concise correct answer"
    }},
    {{
      "question": "Another common interview question?",
      "answer": "Concise correct answer"
    }}
  ],
  "related_topics": ["related topic 1", "related topic 2", "related topic 3"],
  "confidence_score": 0.95
}}"""

    response = model.generate_content(prompt)
    raw      = clean_json_response(response.text)

    try:
        entry = json.loads(raw)
    except json.JSONDecodeError:
        print("   JSON parse failed — asking Gemini to fix it...")
        fix_prompt = f"Fix this malformed JSON and return ONLY valid JSON:\n{raw}"
        fixed_raw  = model.generate_content(fix_prompt).text
        entry      = json.loads(clean_json_response(fixed_raw))

    # Always force our validated category
    entry["category"]   = category
    entry["learned_at"] = datetime.now(timezone.utc).isoformat()
    return entry
