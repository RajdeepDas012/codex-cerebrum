# 🧠 Gemini Coding Brain

> An autonomous AI agent that learns coding concepts every day using the Gemini API,
> commits its growing knowledge base to GitHub automatically, and builds a fine-tuning
> dataset for future offline model training.

<!-- STATS_START -->
## 📊 Live Stats

| Metric | Value |
|---|---|
| Total Topics Learned | **4615** |
| Last Updated | `2026-11-07T14:28:13.645216+00:00` |
| Dataset Size | `4615 entries` |

## 📂 Categories Learned

| Category | Topics |
|---|---|
| data-structures | 3280 |
| algorithms | 277 |
| trading-strategies | 228 |
| crypto-blockchain | 193 |
| technical-analysis | 147 |
| system-design | 121 |
| market-analysis | 114 |
| stocks-markets | 71 |
| databases | 49 |
| security | 39 |
| probability-math | 27 |
| networking | 22 |
| machine-learning | 19 |
| web-dev | 9 |
| language-specific | 7 |
| devops | 7 |
| best-practices | 2 |
| data-visualization | 2 |
| testing | 1 |

## 🕐 Last 5 Topics Learned

- `Implementation of a lock-free thread-safe concurrent BK-Tree using atomic edit-distance-thresholding and child-pointer-linking CAS primitives alongside hazard pointer memory reclamation for high-throughput approximate string matching and multi-core parallel spell checking execution in real-time text processing platforms and concurrent natural language search engines`
- `Implementation of a lock-free thread-safe concurrent T-Digest using atomic centroid-merging and quantile-compression CAS primitives alongside hazard pointer memory reclamation for high-throughput accurate percentile estimation and multi-core parallel streaming distribution analysis execution in real-time telemetry monitoring systems and concurrent metrics aggregation engines`
- `Implementation of a lock-free thread-safe concurrent Count-Min Sketch using atomic frequency-cell-incrementing and multi-hash-probing CAS primitives alongside hazard pointer memory reclamation for high-throughput stream frequency estimation and multi-core parallel heavy-hitter detection execution in real-time network traffic monitoring systems and concurrent stream processing engines`
- `Implementation of a lock-free thread-safe concurrent HyperLogLog using atomic register-updating and max-bucket-merging CAS primitives alongside hazard pointer memory reclamation for high-throughput cardinality estimation and multi-core parallel distinct element counting execution in real-time streaming analytics systems and concurrent big data processing engines`
- `Implementation of a lock-free thread-safe concurrent LSM-Tree (Log-Structured Merge-Tree) using atomic memtable-swapping and SSTable-compaction CAS primitives alongside hazard pointer memory reclamation for high-throughput write-heavy transaction processing and multi-core parallel background compaction execution in real-time distributed key-value storage systems and concurrent database engines`

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
