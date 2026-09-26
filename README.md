# 🧠 Gemini Coding Brain

> An autonomous AI agent that learns coding concepts every day using the Gemini API,
> commits its growing knowledge base to GitHub automatically, and builds a fine-tuning
> dataset for future offline model training.

<!-- STATS_START -->
## 📊 Live Stats

| Metric | Value |
|---|---|
| Total Topics Learned | **1769** |
| Last Updated | `2026-09-26T02:00:35.566574+00:00` |
| Dataset Size | `1769 entries` |

## 📂 Categories Learned

| Category | Topics |
|---|---|
| data-structures | 836 |
| trading-strategies | 228 |
| technical-analysis | 147 |
| market-analysis | 114 |
| crypto-blockchain | 108 |
| system-design | 83 |
| stocks-markets | 71 |
| algorithms | 60 |
| databases | 29 |
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

- `Implementation of a lock-free thread-safe concurrent Priority Queue using atomic heap-node-cas and array-resizing primitives alongside hazard pointer memory reclamation for high-throughput task dispatching and multi-core asynchronous event scheduling in real-time game simulation servers and distributed cloud execution engines`
- `Implementation of a lock-free thread-safe concurrent Fenwick Tree (Binary Indexed Tree) using atomic prefix-sum-updating and index-masking CAS primitives alongside hazard pointer memory reclamation for high-throughput cumulative frequency tracking and multi-core real-time rank querying in high-frequency trading order books and concurrent metrics aggregation systems`
- `Implementation of a lock-free thread-safe concurrent Merkle Tree using atomic hash-propagating and node-rebuilding CAS primitives alongside hazard pointer memory reclamation for high-throughput cryptographic verification and multi-core state validation in real-time blockchain execution engines and distributed trust systems`
- `Implementation of a lock-free thread-safe concurrent HyperLogLog using atomic register-updating and max-val-merging CAS primitives alongside hazard pointer memory reclamation for high-throughput cardinality estimation and multi-core distinct count aggregation in real-time stream processing pipelines and distributed analytics databases`
- `Implementation of a lock-free thread-safe concurrent Wavelet Tree using atomic alphabet-partitioning and bit-vector-building CAS primitives alongside hazard pointer memory reclamation for high-throughput succinct range querying and multi-core rank-select data structure indexing in real-time compressed full-text retrieval systems and bioinformatics genome analysis engines`

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
