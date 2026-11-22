# 🧠 Gemini Coding Brain

> An autonomous AI agent that learns coding concepts every day using the Gemini API,
> commits its growing knowledge base to GitHub automatically, and builds a fine-tuning
> dataset for future offline model training.

<!-- STATS_START -->
## 📊 Live Stats

| Metric | Value |
|---|---|
| Total Topics Learned | **5272** |
| Last Updated | `2026-11-22T19:21:02.919017+00:00` |
| Dataset Size | `5272 entries` |

## 📂 Categories Learned

| Category | Topics |
|---|---|
| data-structures | 3853 |
| algorithms | 328 |
| trading-strategies | 228 |
| crypto-blockchain | 212 |
| technical-analysis | 147 |
| system-design | 121 |
| market-analysis | 114 |
| stocks-markets | 71 |
| databases | 53 |
| security | 42 |
| probability-math | 27 |
| networking | 26 |
| machine-learning | 22 |
| web-dev | 9 |
| language-specific | 7 |
| devops | 7 |
| best-practices | 2 |
| data-visualization | 2 |
| testing | 1 |

## 🕐 Last 5 Topics Learned

- `Implementation of a lock-free thread-safe concurrent Splay Tree using atomic root-splicing and zig-zig-rotation CAS primitives alongside hazard pointer memory reclamation for high-throughput self-adjusting search operations and multi-core parallel frequently-accessed node promotion execution in real-time in-memory caching layers and concurrent database index tuning engines`
- `Implementation of a lock-free thread-safe concurrent Vector Clock using atomic version-vector-incrementing and timestamp-merging CAS primitives alongside hazard pointer memory reclamation for high-throughput causal ordering and multi-core parallel event synchronization execution in real-time distributed messaging systems and concurrent eventual consistency data stores`
- `Implementation of a lock-free thread-safe concurrent Priority Queue using atomic heap-node-promoting and trunk-cascading CAS primitives alongside hazard pointer memory reclamation for high-throughput task scheduling and multi-core parallel asynchronous event execution in real-time operating system kernels and concurrent high-performance computing task dispatchers`
- `Implementation of a lock-free thread-safe concurrent Persistent Segment Tree using atomic version-node-linking and path-copying CAS primitives alongside hazard pointer memory reclamation for high-throughput historical range querying and multi-core parallel time-travel analytics execution in real-time financial auditing systems and concurrent versioned database transactional layers`
- `Implementation of a lock-free thread-safe concurrent Bw-Tree using atomic mapping-table-swapping and delta-chain-installing CAS primitives alongside hazard pointer memory reclamation for high-throughput latch-free memory-optimized index updates and multi-core parallel transactional storage execution in real-time modern relational database engines and concurrent in-memory key-value stores`

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
