# 🧠 Gemini Coding Brain

> An autonomous AI agent that learns coding concepts every day using the Gemini API,
> commits its growing knowledge base to GitHub automatically, and builds a fine-tuning
> dataset for future offline model training.

<!-- STATS_START -->
## 📊 Live Stats

| Metric | Value |
|---|---|
| Total Topics Learned | **2605** |
| Last Updated | `2026-10-08T22:30:42.763365+00:00` |
| Dataset Size | `2605 entries` |

## 📂 Categories Learned

| Category | Topics |
|---|---|
| data-structures | 1558 |
| trading-strategies | 228 |
| technical-analysis | 147 |
| crypto-blockchain | 136 |
| algorithms | 125 |
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

- `Implementation of a lock-free thread-safe concurrent Segment Tree using atomic lazy-propagation and range-update CAS primitives alongside hazard pointer memory reclamation for high-throughput interval aggregation and multi-core range query processing in real-time financial analytics platforms and concurrent computational geometry systems`
- `Implementation of a lock-free thread-safe concurrent Fenwick Tree (Binary Indexed Tree) using atomic prefix-sum-updating and index-masking CAS primitives alongside hazard pointer memory reclamation for high-throughput cumulative frequency queries and multi-core point updates in real-time stream analytics engines and concurrent ranking leaderboard systems`
- `Implementation of a lock-free thread-safe concurrent BK-Tree using atomic edit-distance-partitioning and child-node-linking CAS primitives alongside hazard pointer memory reclamation for high-throughput fuzzy string matching and multi-core spelling correction in real-time search engine query suggestion systems and concurrent dictionary lookup engines`
- `Implementation of a lock-free thread-safe concurrent BKD-Tree using atomic leaf-partitioning and bounding-box-adjusting CAS primitives alongside hazard pointer memory reclamation for high-throughput spatial-temporal indexing and multi-core high-dimensional point searching in real-time geospatial analytics databases and concurrent moving-object tracking systems`
- `Implementation of a lock-free thread-safe concurrent Left-Leaning Red-Black Tree using atomic color-flipping and rotation-balancing CAS primitives alongside hazard pointer memory reclamation for high-throughput self-balancing ordered mapping and multi-core key-value searching in real-time in-memory databases and concurrent caching engines`

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
