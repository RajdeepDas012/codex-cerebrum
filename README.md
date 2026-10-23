# 🧠 Gemini Coding Brain

> An autonomous AI agent that learns coding concepts every day using the Gemini API,
> commits its growing knowledge base to GitHub automatically, and builds a fine-tuning
> dataset for future offline model training.

<!-- STATS_START -->
## 📊 Live Stats

| Metric | Value |
|---|---|
| Total Topics Learned | **3680** |
| Last Updated | `2026-10-23T19:12:20.490996+00:00` |
| Dataset Size | `3680 entries` |

## 📂 Categories Learned

| Category | Topics |
|---|---|
| data-structures | 2448 |
| trading-strategies | 228 |
| algorithms | 226 |
| crypto-blockchain | 165 |
| technical-analysis | 147 |
| system-design | 119 |
| market-analysis | 114 |
| stocks-markets | 71 |
| databases | 41 |
| security | 31 |
| probability-math | 27 |
| networking | 18 |
| machine-learning | 17 |
| web-dev | 9 |
| language-specific | 7 |
| devops | 7 |
| best-practices | 2 |
| data-visualization | 2 |
| testing | 1 |

## 🕐 Last 5 Topics Learned

- `Implementation of a lock-free thread-safe concurrent Fibonacci Heap using atomic root-list-splicing and minimum-key-updating CAS primitives alongside hazard pointer memory reclamation for high-throughput Dijkstra's shortest path algorithm execution and multi-core parallel network routing optimization in real-time telecommunication traffic engines and concurrent graph processing platforms`
- `Implementation of a lock-free thread-safe concurrent Disjoint Set (Union-Find) using atomic parent-pointer-compression and rank-combining CAS primitives alongside hazard pointer memory reclamation for high-throughput equivalence class management and multi-core parallel connected components analysis in real-time social network graph partitioning and concurrent network connectivity engines`
- `Implementation of a lock-free thread-safe concurrent Merkle Tree using atomic hash-node-cascading and path-verification CAS primitives alongside hazard pointer memory reclamation for high-throughput cryptographic block validation and multi-core parallel tamper-evident logging in real-time distributed ledger systems and concurrent blockchain validation engines`
- `Implementation of a lock-free thread-safe concurrent Quotient Filter using atomic metadata-bit-shifting and run-cluster-shifting CAS primitives alongside hazard pointer memory reclamation for high-throughput memory-efficient approximate membership testing and multi-core parallel duplicate detection in real-time distributed caching layers and concurrent database storage engines`
- `Implementation of a lock-free thread-safe concurrent SimHash index using atomic bit-vector-manipulation and hamming-distance-calculating CAS primitives alongside hazard pointer memory reclamation for high-throughput near-duplicate document detection and multi-core parallel similarity searching in real-time web crawling pipelines and concurrent plagiarism detection engines`

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
