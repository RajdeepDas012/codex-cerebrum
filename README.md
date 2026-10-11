# 🧠 Gemini Coding Brain

> An autonomous AI agent that learns coding concepts every day using the Gemini API,
> commits its growing knowledge base to GitHub automatically, and builds a fine-tuning
> dataset for future offline model training.

<!-- STATS_START -->
## 📊 Live Stats

| Metric | Value |
|---|---|
| Total Topics Learned | **2790** |
| Last Updated | `2026-10-11T21:50:08.506831+00:00` |
| Dataset Size | `2790 entries` |

## 📂 Categories Learned

| Category | Topics |
|---|---|
| data-structures | 1715 |
| trading-strategies | 228 |
| technical-analysis | 147 |
| algorithms | 143 |
| crypto-blockchain | 140 |
| market-analysis | 114 |
| system-design | 84 |
| stocks-markets | 71 |
| databases | 38 |
| probability-math | 27 |
| security | 24 |
| networking | 16 |
| machine-learning | 15 |
| web-dev | 9 |
| language-specific | 7 |
| devops | 7 |
| best-practices | 2 |
| data-visualization | 2 |
| testing | 1 |

## 🕐 Last 5 Topics Learned

- `Implementation of a lock-free thread-safe concurrent Wavelet Tree using atomic alphabet-partitioning and bit-vector-updating CAS primitives alongside hazard pointer memory reclamation for high-throughput range quantile queries and multi-core compressed text indexing in real-time bioinformatics data platforms and concurrent column-store database engines`
- `Implementation of a lock-free thread-safe concurrent Treap using atomic randomized-priority-balancing and rotation-descriptor-swapping CAS primitives alongside hazard pointer memory reclamation for high-throughput randomized key-value indexing and multi-core balanced search operations in real-time in-memory caching systems and concurrent transactional databases`
- `Implementation of a lock-free thread-safe concurrent Finger Tree using atomic node-concatenating and deep-spine-restructuring CAS primitives alongside hazard pointer memory reclamation for high-throughput persistent sequence operations and multi-core functional collection transformations in real-time stream processing engines and concurrent functional data structure platforms`
- `Implementation of a lock-free thread-safe concurrent Xor Filter using atomic fingerprint-calculating and coefficient-swapping CAS primitives alongside hazard pointer memory reclamation for high-throughput space-efficient approximate membership querying and multi-core distributed deduplication in real-time caching systems and concurrent database storage engines`
- `Implementation of a lock-free thread-safe concurrent Merkle Tree using atomic hash-propagating and node-updating CAS primitives alongside hazard pointer memory reclamation for high-throughput distributed state synchronization and multi-core cryptographic proof generation in real-time peer-to-peer file sharing networks and concurrent decentralized ledger systems`

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
