# 🧠 Gemini Coding Brain

> An autonomous AI agent that learns coding concepts every day using the Gemini API,
> commits its growing knowledge base to GitHub automatically, and builds a fine-tuning
> dataset for future offline model training.

<!-- STATS_START -->
## 📊 Live Stats

| Metric | Value |
|---|---|
| Total Topics Learned | **2648** |
| Last Updated | `2026-10-09T16:29:11.345885+00:00` |
| Dataset Size | `2648 entries` |

## 📂 Categories Learned

| Category | Topics |
|---|---|
| data-structures | 1597 |
| trading-strategies | 228 |
| technical-analysis | 147 |
| crypto-blockchain | 137 |
| algorithms | 128 |
| market-analysis | 114 |
| system-design | 84 |
| stocks-markets | 71 |
| databases | 36 |
| probability-math | 27 |
| security | 23 |
| machine-learning | 15 |
| networking | 13 |
| web-dev | 9 |
| language-specific | 7 |
| devops | 7 |
| best-practices | 2 |
| data-visualization | 2 |
| testing | 1 |

## 🕐 Last 5 Topics Learned

- `Implementation of a lock-free thread-safe concurrent Interval Tree using atomic node-overlapping-updating and interval-endpoint-balancing CAS primitives alongside hazard pointer memory reclamation for high-throughput temporal range queries and multi-core schedule overlap detection in real-time calendar management systems and concurrent resource allocation engines`
- `Implementation of a lock-free thread-safe concurrent KD-Tree using atomic bounding-hyperplane-partitioning and child-node-attaching CAS primitives alongside hazard pointer memory reclamation for high-throughput multi-dimensional spatial partitioning and multi-core nearest-neighbor querying in real-time robotic sensor localization systems and concurrent spatial database engines`
- `Implementation of a lock-free thread-safe concurrent R-Tree using atomic bounding-box-adjusting and branch-splitting CAS primitives alongside hazard pointer memory reclamation for high-throughput spatial indexing and multi-core geometric range searching in real-time geographic information systems and concurrent location-based service platforms`
- `Implementation of a lock-free thread-safe concurrent Persistent Segment Tree using atomic version-branching and node-sharing CAS primitives alongside hazard pointer memory reclamation for high-throughput historical interval querying and multi-core time-travel state indexing in real-time financial auditing engines and concurrent version-controlled database storage systems`
- `Implementation of a lock-free thread-safe concurrent Merkle Tree using atomic hash-propagating and node-updating CAS primitives alongside hazard pointer memory reclamation for high-throughput cryptographic verification and multi-core tamper-evident data validation in real-time distributed ledger systems and concurrent blockchain storage engines`

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
