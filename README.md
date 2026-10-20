# 🧠 Gemini Coding Brain

> An autonomous AI agent that learns coding concepts every day using the Gemini API,
> commits its growing knowledge base to GitHub automatically, and builds a fine-tuning
> dataset for future offline model training.

<!-- STATS_START -->
## 📊 Live Stats

| Metric | Value |
|---|---|
| Total Topics Learned | **3407** |
| Last Updated | `2026-10-20T00:43:09.687134+00:00` |
| Dataset Size | `3407 entries` |

## 📂 Categories Learned

| Category | Topics |
|---|---|
| data-structures | 2212 |
| trading-strategies | 228 |
| algorithms | 207 |
| crypto-blockchain | 158 |
| technical-analysis | 147 |
| system-design | 115 |
| market-analysis | 114 |
| stocks-markets | 71 |
| databases | 40 |
| security | 27 |
| probability-math | 27 |
| networking | 17 |
| machine-learning | 16 |
| web-dev | 9 |
| language-specific | 7 |
| devops | 7 |
| best-practices | 2 |
| data-visualization | 2 |
| testing | 1 |

## 🕐 Last 5 Topics Learned

- `Implementation of a lock-free thread-safe concurrent Deque using atomic head-tail-stealing and pointer-cascading CAS primitives alongside hazard pointer memory reclamation for high-throughput work-stealing task scheduling and multi-core parallel load balancing in real-time asynchronous execution engines and concurrent task processing frameworks`
- `Implementation of a lock-free thread-safe concurrent Merkle Patricia Tree using atomic branch-node-hashing and state-root-updating CAS primitives alongside hazard pointer memory reclamation for high-throughput cryptographic state verification and multi-core parallel blockchain ledger updates in real-time decentralized transaction engines and concurrent distributed key-value database storage layers`
- `Implementation of a lock-free thread-safe concurrent Wavelet Tree using atomic alphabet-bit-partitioning and child-node-routing CAS primitives alongside hazard pointer memory reclamation for high-throughput succinct text indexing and multi-core parallel rank-select queries in real-time compressed bioinformatics databases and concurrent string analysis engines`
- `Implementation of a lock-free thread-safe concurrent Bloom Filter using atomic bit-array-setting and hash-collision-resolving CAS primitives alongside hazard pointer memory reclamation for high-throughput approximate membership testing and multi-core parallel item lookup in real-time distributed caching systems and concurrent database query optimization engines`
- `Implementation of a lock-free thread-safe concurrent Fenwick Tree using atomic point-updating and prefix-sum-accumulating CAS primitives alongside hazard pointer memory reclamation for high-throughput cumulative frequency queries and multi-core parallel range prefix updates in real-time streaming analytics engines and concurrent statistical tracking systems`

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
