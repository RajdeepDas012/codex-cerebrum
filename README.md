# 🧠 Gemini Coding Brain

> An autonomous AI agent that learns coding concepts every day using the Gemini API,
> commits its growing knowledge base to GitHub automatically, and builds a fine-tuning
> dataset for future offline model training.

<!-- STATS_START -->
## 📊 Live Stats

| Metric | Value |
|---|---|
| Total Topics Learned | **4406** |
| Last Updated | `2026-11-02T21:14:29.711686+00:00` |
| Dataset Size | `4406 entries` |

## 📂 Categories Learned

| Category | Topics |
|---|---|
| data-structures | 3097 |
| algorithms | 262 |
| trading-strategies | 228 |
| crypto-blockchain | 187 |
| technical-analysis | 147 |
| system-design | 120 |
| market-analysis | 114 |
| stocks-markets | 71 |
| databases | 48 |
| security | 37 |
| probability-math | 27 |
| networking | 21 |
| machine-learning | 19 |
| web-dev | 9 |
| language-specific | 7 |
| devops | 7 |
| best-practices | 2 |
| data-visualization | 2 |
| testing | 1 |

## 🕐 Last 5 Topics Learned

- `Implementation of a lock-free thread-safe concurrent Merkle Tree using atomic hash-propagating and node-updating CAS primitives alongside hazard pointer memory reclamation for high-throughput cryptographic verification and multi-core parallel blockchain state validation execution in real-time distributed ledger systems and concurrent decentralized storage engines`
- `Implementation of a lock-free thread-safe concurrent Suffix Tree using atomic node-splitting and suffix-link-updating CAS primitives alongside hazard pointer memory reclamation for high-throughput linear-time substring searching and multi-core parallel string matching execution in real-time genomic sequence analysis systems and concurrent text retrieval engines`
- `Implementation of a lock-free thread-safe concurrent Finger Tree using atomic structural-concatenation and measure-caching CAS primitives alongside hazard pointer memory reclamation for high-throughput persistent sequence operations and multi-core parallel functional data-structure execution in real-time stream processing systems and concurrent functional programming engines`
- `Implementation of a lock-free thread-safe concurrent Persistent Red-Black Tree using atomic structural-sharing and node-cloning CAS primitives alongside hazard pointer memory reclamation for high-throughput immutable state history querying and multi-core parallel time-travel debugging execution in real-time functional programming systems and concurrent versioned database storage engines`
- `Implementation of a lock-free thread-safe concurrent Segment Tree using atomic lazy-propagation and range-update CAS primitives alongside hazard pointer memory reclamation for high-throughput interval query processing and multi-core parallel range-maximum execution in real-time financial analytics systems and concurrent computational geometry engines`

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
