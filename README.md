# 🧠 Gemini Coding Brain

> An autonomous AI agent that learns coding concepts every day using the Gemini API,
> commits its growing knowledge base to GitHub automatically, and builds a fine-tuning
> dataset for future offline model training.

<!-- STATS_START -->
## 📊 Live Stats

| Metric | Value |
|---|---|
| Total Topics Learned | **2190** |
| Last Updated | `2026-10-02T12:57:14.738274+00:00` |
| Dataset Size | `2190 entries` |

## 📂 Categories Learned

| Category | Topics |
|---|---|
| data-structures | 1192 |
| trading-strategies | 228 |
| technical-analysis | 147 |
| crypto-blockchain | 122 |
| market-analysis | 114 |
| algorithms | 100 |
| system-design | 83 |
| stocks-markets | 71 |
| databases | 34 |
| probability-math | 27 |
| security | 18 |
| machine-learning | 15 |
| networking | 12 |
| web-dev | 9 |
| language-specific | 7 |
| devops | 7 |
| data-visualization | 2 |
| best-practices | 1 |
| testing | 1 |

## 🕐 Last 5 Topics Learned

- `Implementation of a lock-free thread-safe concurrent LSM-Tree (Log-Structured Merge-Tree) using atomic memtable-swapping and SSTable-compaction CAS primitives alongside hazard pointer memory reclamation for high-throughput write-heavy data ingestion and multi-core range querying in real-time distributed key-value stores and concurrent transactional database engines`
- `Implementation of a lock-free thread-safe concurrent Persistent Segment Tree using atomic version-node-linking and path-copying CAS primitives alongside hazard pointer memory reclamation for high-throughput historical range queries and multi-core functional data structure updates in real-time financial ledger systems and concurrent time-travel debugging engines`
- `Implementation of a lock-free thread-safe concurrent Bloom-ier Filter using atomic version-vector-tagging and false-positive-mitigation CAS primitives alongside hazard pointer memory reclamation for high-throughput stream membership validation and multi-core time-decaying probabilistic lookups in real-time fraud detection systems and concurrent network telemetry platforms`
- `Implementation of a lock-free thread-safe concurrent Disjoint Set (Union-Find) using atomic parent-pointer-compression and rank-balancing CAS primitives alongside hazard pointer memory reclamation for high-throughput equivalence class merging and multi-core connected components analysis in real-time social network graph partitioning and concurrent compiler type inference engines`
- `Implementation of a lock-free thread-safe concurrent Segment Tree using atomic lazy-propagation-tagging and range-query CAS primitives alongside hazard pointer memory reclamation for high-throughput range sum updates and multi-core spatial statistical aggregation in real-time financial analytics platforms and concurrent gaming telemetry engines`

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
