# 🧠 Gemini Coding Brain

> An autonomous AI agent that learns coding concepts every day using the Gemini API,
> commits its growing knowledge base to GitHub automatically, and builds a fine-tuning
> dataset for future offline model training.

<!-- STATS_START -->
## 📊 Live Stats

| Metric | Value |
|---|---|
| Total Topics Learned | **3459** |
| Last Updated | `2026-10-20T20:34:45.742395+00:00` |
| Dataset Size | `3459 entries` |

## 📂 Categories Learned

| Category | Topics |
|---|---|
| data-structures | 2253 |
| trading-strategies | 228 |
| algorithms | 212 |
| crypto-blockchain | 159 |
| technical-analysis | 147 |
| system-design | 117 |
| market-analysis | 114 |
| stocks-markets | 71 |
| databases | 40 |
| security | 29 |
| probability-math | 27 |
| machine-learning | 17 |
| networking | 17 |
| web-dev | 9 |
| language-specific | 7 |
| devops | 7 |
| best-practices | 2 |
| data-visualization | 2 |
| testing | 1 |

## 🕐 Last 5 Topics Learned

- `Implementation of a lock-free thread-safe concurrent Consistent Hashing ring using atomic node-token-allocating and virtual-node-rebalancing CAS primitives alongside hazard pointer memory reclamation for high-throughput distributed load balancing and multi-core parallel key routing in real-time caching clusters and concurrent microservice partitioning engines`
- `Implementation of a lock-free thread-safe concurrent R-Tree using atomic bounding-box-adjusting and node-splitting CAS primitives alongside hazard pointer memory reclamation for high-throughput spatial indexing and multi-core parallel geometric range queries in real-time geospatial tracking systems and concurrent location-based service engines`
- `Implementation of a lock-free thread-safe concurrent Wavelet Tree using atomic character-ranking and bit-vector-splicing CAS primitives alongside hazard pointer memory reclamation for high-throughput succinct text indexing and multi-core parallel compressed pattern matching in real-time genomic sequence analysis systems and concurrent text search engines`
- `Implementation of a lock-free thread-safe concurrent Segment Tree using atomic range-query-updating and lazy-propagation CAS primitives alongside hazard pointer memory reclamation for high-throughput interval aggregation and multi-core parallel range updates in real-time financial trading systems and concurrent analytical query engines`
- `Implementation of a lock-free thread-safe concurrent B-link Tree using atomic right-link-traversing and node-splitting CAS primitives alongside hazard pointer memory reclamation for high-throughput concurrent database indexing and multi-core parallel range scans in real-time in-memory storage engines and concurrent transactional databases`

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
