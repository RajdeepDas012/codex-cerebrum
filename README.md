# 🧠 Gemini Coding Brain

> An autonomous AI agent that learns coding concepts every day using the Gemini API,
> commits its growing knowledge base to GitHub automatically, and builds a fine-tuning
> dataset for future offline model training.

<!-- STATS_START -->
## 📊 Live Stats

| Metric | Value |
|---|---|
| Total Topics Learned | **2903** |
| Last Updated | `2026-10-14T01:46:34.379749+00:00` |
| Dataset Size | `2903 entries` |

## 📂 Categories Learned

| Category | Topics |
|---|---|
| data-structures | 1803 |
| trading-strategies | 228 |
| algorithms | 160 |
| technical-analysis | 147 |
| crypto-blockchain | 144 |
| market-analysis | 114 |
| system-design | 86 |
| stocks-markets | 71 |
| databases | 38 |
| probability-math | 27 |
| security | 25 |
| machine-learning | 16 |
| networking | 16 |
| web-dev | 9 |
| language-specific | 7 |
| devops | 7 |
| best-practices | 2 |
| data-visualization | 2 |
| testing | 1 |

## 🕐 Last 5 Topics Learned

- `Implementation of a lock-free thread-safe concurrent Cuckoo Filter using atomic bucket-relocating and finger-printing CAS primitives alongside hazard pointer memory reclamation for high-throughput space-efficient item deletion support and multi-core approximate membership testing in real-time network security scanners and concurrent caching systems`
- `Implementation of a lock-free thread-safe concurrent Priority Queue using atomic heap-node-bubbling and index-swapping CAS primitives alongside hazard pointer memory reclamation for high-throughput task scheduling and multi-core event-driven execution in real-time job processing engines and concurrent task dispatching systems`
- `Implementation of a lock-free thread-safe concurrent Segment Tree using atomic range-updating and query-propagating CAS primitives alongside hazard pointer memory reclamation for high-throughput range-maximum querying and multi-core interval computation in real-time financial analytics platforms and concurrent time-series databases`
- `Implementation of a lock-free thread-safe concurrent HyperLogLog using atomic register-updating and max-val-merging CAS primitives alongside hazard pointer memory reclamation for high-throughput cardinality estimation and multi-core distinct count aggregation in real-time stream processing analytics platforms and concurrent database query engines`
- `Implementation of a lock-free thread-safe concurrent Concurrent Hash Map using atomic bucket-resizing and node-chain-splicing CAS primitives alongside hazard pointer memory reclamation for high-throughput thread-safe key-value insertions and multi-core concurrent lookups in real-time in-memory caching layers and high-concurrency database storage engines`

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
