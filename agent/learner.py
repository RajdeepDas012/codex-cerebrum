"""
learner.py
Sends a topic to Gemini and returns a structured knowledge entry.
All output is strict JSON — no markdown, no prose.
"""

import json
import re
from datetime import datetime, timezone


def clean_json_response(raw: str) -> str:
    """Strip markdown fences and whitespace from Gemini response."""
    raw = raw.strip()
    # Remove ```json ... ``` or ``` ... ```
    raw = re.sub(r"^```(?:json)?\s*", "", raw)
    raw = re.sub(r"\s*```$",          "", raw)
    return raw.strip()


def learn_topic(model, topic: str, recent_entries: list) -> dict:
    """
    Ask Gemini to deeply learn a coding topic.
    Returns a structured dict ready to save.
    """

    # Give Gemini context of recent learning so it doesn't repeat
    context = ""
    if recent_entries:
        context = f"""
Recently learned topics for context (avoid repeating same examples):
{json.dumps([{"topic": e["topic"], "category": e["category"]} for e in recent_entries[-5:]], indent=2)}
"""

    prompt = f"""You are an expert software engineer building a structured coding knowledge base.
{context}
Your task: Learn this topic deeply and return structured knowledge.

TOPIC: "{topic}"

Reply ONLY with a valid JSON object. No markdown. No explanation outside JSON.
No trailing commas. Use double quotes only.

JSON structure:
{{
  "topic": "{topic}",
  "category": "one of: algorithms | data-structures | web-dev | devops | language-specific | databases | system-design | best-practices | debugging | tools | security | testing",
  "language": "primary language this applies to, or 'language-agnostic'",
  "difficulty": "beginner | intermediate | advanced",
  "summary": "Clear 2-3 sentence explanation of the core concept. What it is and why it matters.",
  "key_points": [
    "Specific important point 1",
    "Specific important point 2",
    "Specific important point 3",
    "Specific important point 4"
  ],
  "code_example": {{
    "language": "python or javascript or bash etc",
    "description": "One sentence: what this code demonstrates",
    "correct": "// GOOD: working correct code example here\\ncode line 2\\ncode line 3",
    "wrong": "// BAD: common mistake people make\\nwrong code here"
  }},
  "common_mistakes": [
    "Specific mistake 1 developers make",
    "Specific mistake 2 developers make"
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
  "resources": [
    "Official docs or MDN link description",
    "Key concept to search for to learn more"
  ],
  "confidence_score": 0.95
}}"""

    response = model.generate_content(prompt)
    raw      = clean_json_response(response.text)

    try:
        entry = json.loads(raw)
    except json.JSONDecodeError:
        # Second attempt: ask Gemini to fix its own JSON
        print("⚠️  JSON parse failed — asking Gemini to fix it...")
        fix_prompt = f"""The following JSON is malformed. Fix it and return ONLY valid JSON, nothing else:

{raw}"""
        fixed_raw = model.generate_content(fix_prompt).text
        entry     = json.loads(clean_json_response(fixed_raw))

    # Stamp metadata
    entry["learned_at"] = datetime.now(timezone.utc).isoformat()
    return entry
