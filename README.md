# 🧠 Gemini Coding Brain

> An autonomous AI agent that learns coding concepts every day using the Gemini API,
> commits its growing knowledge base to GitHub automatically, and builds a fine-tuning
> dataset for future offline model training.

<!-- STATS_START -->
## 📊 Live Stats

| Metric | Value |
|---|---|
| Total Topics Learned | **1836** |
| Last Updated | `2026-09-26T22:47:49.137309+00:00` |
| Dataset Size | `1836 entries` |

## 📂 Categories Learned

| Category | Topics |
|---|---|
| data-structures | 894 |
| trading-strategies | 228 |
| technical-analysis | 147 |
| market-analysis | 114 |
| crypto-blockchain | 110 |
| system-design | 83 |
| stocks-markets | 71 |
| algorithms | 66 |
| databases | 30 |
| probability-math | 27 |
| security | 16 |
| networking | 12 |
| machine-learning | 11 |
| web-dev | 9 |
| language-specific | 7 |
| devops | 7 |
| data-visualization | 2 |
| best-practices | 1 |
| testing | 1 |

## 🕐 Last 5 Topics Learned

- `Implementation of a lock-free thread-safe concurrent Bounding Volume Hierarchy (BVH) using atomic bounding-box-merging and tree-refitting CAS primitives alongside hazard pointer memory reclamation for high-throughput ray-triangle intersection querying and multi-core spatial acceleration in real-time computer graphics ray tracing engines and concurrent physics simulation platforms`
- `Implementation of a lock-free thread-safe concurrent R-Tree using atomic bounding-box-updating and node-splitting CAS primitives alongside hazard pointer memory reclamation for high-throughput spatial indexing and multi-core geometric data searching in real-time geographic information systems and concurrent geospatial database engines`
- `Implementation of a lock-free thread-safe concurrent Priority Queue using atomic heap-node-swapping and index-tracking CAS primitives alongside hazard pointer memory reclamation for high-throughput task prioritization and multi-core thread scheduling in real-time asynchronous execution engines and concurrent task dispatching frameworks`
- `Implementation of a lock-free thread-safe concurrent Circular Buffer (Ring Buffer) using atomic head-tail-advancing and wrap-around-managing CAS primitives alongside hazard pointer memory reclamation for high-throughput inter-thread message passing and multi-core stream buffering in real-time audio processing pipelines and concurrent high-frequency trading market data ingestion engines`
- `Implementation of a lock-free thread-safe concurrent B-link Tree using atomic right-link-traversing and concurrent-node-splitting CAS primitives alongside hazard pointer memory reclamation for high-throughput concurrent database indexing and multi-core high-concurrency key-value storage in real-time enterprise storage systems and high-performance relational database engines`

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
