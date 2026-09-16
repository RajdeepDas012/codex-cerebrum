# 🧠 Gemini Coding Brain

> An autonomous AI agent that learns coding concepts every day using the Gemini API,
> commits its growing knowledge base to GitHub automatically, and builds a fine-tuning
> dataset for future offline model training.

<!-- STATS_START -->
## 📊 Live Stats

| Metric | Value |
|---|---|
| Total Topics Learned | **1030** |
| Last Updated | `2026-09-16T22:02:37.782691+00:00` |
| Dataset Size | `1030 entries` |

## 📂 Categories Learned

| Category | Topics |
|---|---|
| trading-strategies | 228 |
| data-structures | 192 |
| technical-analysis | 147 |
| market-analysis | 114 |
| crypto-blockchain | 82 |
| system-design | 77 |
| stocks-markets | 71 |
| probability-math | 27 |
| algorithms | 21 |
| databases | 17 |
| machine-learning | 10 |
| web-dev | 9 |
| security | 9 |
| networking | 8 |
| language-specific | 7 |
| devops | 7 |
| data-visualization | 2 |
| best-practices | 1 |
| testing | 1 |

## 🕐 Last 5 Topics Learned

- `Implementation of a lock-free thread-safe concurrent VBK (Vantage Point) Tree using atomic distance-partitioning CAS primitives and hazard pointer memory reclamation for high-throughput metric space similarity searching and nearest-neighbor lookups in real-time multimedia content retrieval and image recognition engines`
- `Implementation of a lock-free thread-safe concurrent Binomial Heap using atomic root-link CAS primitives and hazard pointer memory reclamation for high-throughput meldable priority queue operations in real-time task scheduling and distributed event simulation engines`
- `Implementation of a lock-free thread-safe concurrent Leftist Heap using atomic merge-root CAS primitives and hazard pointer memory reclamation for high-throughput mergeable priority queue operations in real-time job scheduling and discrete-event simulation engines`
- `Implementation of a lock-free thread-safe concurrent Fibonacci Heap using atomic min-pointer CAS primitives and hazard pointer memory reclamation for high-throughput decrease-key and merge operations in real-time graph algorithms and shortest-path routing engines`
- `Implementation of a lock-free thread-safe concurrent B-link Tree using atomic right-link pointer CAS primitives and hazard pointer memory reclamation for high-throughput concurrent node-splitting and range queries in real-time in-memory database index storage engines`

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
