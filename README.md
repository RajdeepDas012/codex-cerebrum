# 🧠 Gemini Coding Brain

> An autonomous AI agent that learns coding concepts every day using the Gemini API,
> commits its growing knowledge base to GitHub automatically, and builds a fine-tuning
> dataset for future offline model training.

<!-- STATS_START -->
## 📊 Live Stats

| Metric | Value |
|---|---|
| Total Topics Learned | **4026** |
| Last Updated | `2026-10-27T20:14:21.268896+00:00` |
| Dataset Size | `4026 entries` |

## 📂 Categories Learned

| Category | Topics |
|---|---|
| data-structures | 2760 |
| algorithms | 243 |
| trading-strategies | 228 |
| crypto-blockchain | 175 |
| technical-analysis | 147 |
| system-design | 119 |
| market-analysis | 114 |
| stocks-markets | 71 |
| databases | 44 |
| security | 33 |
| probability-math | 27 |
| networking | 20 |
| machine-learning | 17 |
| web-dev | 9 |
| language-specific | 7 |
| devops | 7 |
| best-practices | 2 |
| data-visualization | 2 |
| testing | 1 |

## 🕐 Last 5 Topics Learned

- `Implementation of a lock-free thread-safe concurrent Segment Tree using atomic range-update-propagating and lazy-propagation-marking CAS primitives alongside hazard pointer memory reclamation for high-throughput range query operations and multi-core parallel dynamic interval computations in real-time financial analytics platforms and concurrent computational geometry engines`
- `Implementation of a lock-free thread-safe concurrent Suffix Tree using atomic node-splitting and suffix-link-updating CAS primitives alongside hazard pointer memory reclamation for high-throughput substring pattern matching and multi-core parallel bioinformatics genomic sequence alignment in real-time text mining platforms and concurrent compiler syntax analysis engines`
- `Implementation of a lock-free thread-safe concurrent T-Digest using atomic centroid-merging and quantile-estimating CAS primitives alongside hazard pointer memory reclamation for high-throughput percentile calculations and multi-core parallel streaming distribution summarization in real-time observability telemetry platforms and concurrent performance monitoring engines`
- `Implementation of a lock-free thread-safe concurrent Merkle Patricia Trie using atomic branch-node-updating and path-compression CAS primitives alongside hazard pointer memory reclamation for high-throughput cryptographic state verification and multi-core parallel persistent storage state synchronization in real-time Ethereum-compatible blockchain validation platforms and concurrent decentralized ledger engines`
- `Implementation of a lock-free thread-safe concurrent HyperLogLog using atomic register-updating and max-merging CAS primitives alongside hazard pointer memory reclamation for high-throughput cardinality estimation and multi-core parallel distinct element counting in real-time analytics platforms and concurrent big data streaming engines`

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
