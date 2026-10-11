# 🧠 Gemini Coding Brain

> An autonomous AI agent that learns coding concepts every day using the Gemini API,
> commits its growing knowledge base to GitHub automatically, and builds a fine-tuning
> dataset for future offline model training.

<!-- STATS_START -->
## 📊 Live Stats

| Metric | Value |
|---|---|
| Total Topics Learned | **2801** |
| Last Updated | `2026-10-11T22:24:41.621370+00:00` |
| Dataset Size | `2801 entries` |

## 📂 Categories Learned

| Category | Topics |
|---|---|
| data-structures | 1725 |
| trading-strategies | 228 |
| technical-analysis | 147 |
| algorithms | 144 |
| crypto-blockchain | 140 |
| market-analysis | 114 |
| system-design | 84 |
| stocks-markets | 71 |
| databases | 38 |
| probability-math | 27 |
| security | 24 |
| networking | 16 |
| machine-learning | 15 |
| web-dev | 9 |
| language-specific | 7 |
| devops | 7 |
| best-practices | 2 |
| data-visualization | 2 |
| testing | 1 |

## 🕐 Last 5 Topics Learned

- `Implementation of a lock-free thread-safe concurrent R-Tree using atomic bounding-box-expanding and node-splitting CAS primitives alongside hazard pointer memory reclamation for high-throughput spatial indexing and multi-core geometric data searching in real-time geographic information systems and concurrent geospatial database engines`
- `Implementation of a lock-free thread-safe concurrent Hash Array Mapped Trie (HAMT) using atomic node-expansion and pointer-swapping CAS primitives alongside hazard pointer memory reclamation for high-throughput persistent key-value indexing and multi-core immutable collection transformations in real-time distributed state stores and concurrent functional programming platforms`
- `Implementation of a lock-free thread-safe concurrent Persistent Map using atomic structural-sharing and root-swapping CAS primitives alongside hazard pointer memory reclamation for high-throughput immutable state versioning and multi-core functional data transformations in real-time event-sourcing engines and concurrent state-management platforms`
- `Implementation of a lock-free thread-safe concurrent Quotient Filter using atomic metadata-shifting and run-descriptor-updating CAS primitives alongside hazard pointer memory reclamation for high-throughput space-efficient approximate membership querying and multi-core distributed deduplication in real-time caching systems and concurrent database storage engines`
- `Implementation of a lock-free thread-safe concurrent B+ Tree using atomic leaf-sibling-linking and split-coordination CAS primitives alongside hazard pointer memory reclamation for high-throughput range querying and multi-core transactional record storage in real-time relational database management systems and concurrent storage engines`

<!-- STATS_END -->

---

## 🚀 How It Works

```
GitHub Actions (every ~72 min = 20x per day)
        ↓
  agent.py picks next topic from queue
        ↓
  Gemini learns it deeply → returns structured JSON
        ↓
  Saves to data/knowledge_base.json
        ↓
  Writes daily log to data/logs/YYYY-MM-DD.md
        ↓
  Exports training pair to export/finetune_ready.jsonl
        ↓
  Updates README stats
        ↓
  GitHub Actions commits everything automatically
```

---

## 📁 Project Structure

```
gemini-coding-brain/
├── .github/
│   └── workflows/
│       └── daily_train.yml      ← runs 20x per day
├── agent/
│   ├── agent.py                 ← main orchestrator
│   ├── topic_manager.py         ← picks next topic
│   ├── learner.py               ← asks Gemini, structures response
│   ├── logger.py                ← daily logs + README updates
│   └── exporter.py              ← JSONL export for fine-tuning
├── data/
│   ├── knowledge_base.json      ← 📈 grows with every run
│   ├── topics_queue.json        ← topic queue (auto-refills)
│   └── logs/
│       └── YYYY-MM-DD.md        ← daily learning logs
├── export/
│   └── finetune_ready.jsonl     ← future fine-tuning dataset
├── requirements.txt
└── README.md
```

---

## ⚙️ Setup (5 minutes)

### 1. Fork / Clone this repo

```bash
git clone https://github.com/YOUR_USERNAME/gemini-coding-brain
cd gemini-coding-brain
```

### 2. Get a Gemini API Key

Go to [aistudio.google.com](https://aistudio.google.com) → Get API key → Copy it

**It's free** — Gemini 3.5 Flash lite has a generous free tier.

## 🧪 Run Locally (Optional)

```bash
# Install dependency
pip install -r requirements.txt

# Set your key
export GEMINI_API_KEY="your-key-here"   # Mac/Linux
set GEMINI_API_KEY=your-key-here        # Windows

# Run once
python agent/agent.py
```

---

## 📂 Knowledge Base Format

Each entry in `knowledge_base.json` looks like:

```json
{
  "topic": "Python list comprehensions vs loops",
  "category": "language-specific",
  "language": "python",
  "difficulty": "intermediate",
  "summary": "...",
  "key_points": ["...", "..."],
  "code_example": {
    "language": "python",
    "description": "...",
    "correct": "...",
    "wrong": "..."
  },
  "common_mistakes": ["..."],
  "best_practices": ["..."],
  "when_to_use": "...",
  "when_not_to_use": "...",
  "interview_questions": [
    { "question": "...", "answer": "..." }
  ],
  "related_topics": ["...", "..."],
  "confidence_score": 0.95,
  "learned_at": "2025-06-15T10:30:00+00:00",
  "run_number": 42
}


---

### 📂 Licence

MIT — use it, fork it, build on it.
