# 🧠 Gemini Coding Brain

> An autonomous AI agent that learns coding concepts every day using the Gemini API,
> commits its growing knowledge base to GitHub automatically, and builds a fine-tuning
> dataset for future offline model training.

<!-- STATS_START -->
## 📊 Live Stats

| Metric | Value |
|---|---|
| Total Topics Learned | **3288** |
| Last Updated | `2026-10-18T14:59:35.931017+00:00` |
| Dataset Size | `3288 entries` |

## 📂 Categories Learned

| Category | Topics |
|---|---|
| data-structures | 2117 |
| trading-strategies | 228 |
| algorithms | 196 |
| crypto-blockchain | 154 |
| technical-analysis | 147 |
| market-analysis | 114 |
| system-design | 107 |
| stocks-markets | 71 |
| databases | 40 |
| security | 27 |
| probability-math | 27 |
| machine-learning | 16 |
| networking | 16 |
| web-dev | 9 |
| language-specific | 7 |
| devops | 7 |
| best-practices | 2 |
| data-visualization | 2 |
| testing | 1 |

## 🕐 Last 5 Topics Learned

- `Implementation of a lock-free thread-safe concurrent Count-Min Sketch using atomic frequency-incrementing and hash-bucket-updating CAS primitives alongside hazard pointer memory reclamation for high-throughput heavy-hitter stream frequency estimation and multi-core parallel event tracking in real-time network traffic analysis platforms and concurrent log monitoring engines`
- `Implementation of a lock-free thread-safe concurrent Consistent Hashing ring using atomic virtual-node-splicing and ring-boundary-updating CAS primitives alongside hazard pointer memory reclamation for high-throughput distributed load balancing and multi-core parallel key routing in real-time microservice gateway routing and concurrent distributed cache partitioning systems`
- `Implementation of a lock-free thread-safe concurrent LRU cache using atomic doubly-linked-list-splicing and hash-map-routing CAS primitives alongside hazard pointer memory reclamation for high-throughput cache hit management and multi-core parallel hot-data retention in real-time in-memory databases and concurrent application caching layers`
- `Implementation of a lock-free thread-safe concurrent LFU (Least Frequently Used) cache using atomic frequency-list-splicing and node-eviction CAS primitives alongside hazard pointer memory reclamation for high-throughput cache eviction management and multi-core parallel hot-key retention in real-time content delivery networks and concurrent distributed caching services`
- `Implementation of a lock-free thread-safe concurrent Segment Tree using atomic range-bound-updating and lazy-propagation CAS primitives alongside hazard pointer memory reclamation for high-throughput interval query aggregation and multi-core parallel range modification in real-time financial trading analytics and concurrent spatial database indexing systems`

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
