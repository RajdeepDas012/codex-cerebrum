# 🧠 Gemini Coding Brain

> An autonomous AI agent that learns coding concepts every day using the Gemini API,
> commits its growing knowledge base to GitHub automatically, and builds a fine-tuning
> dataset for future offline model training.

<!-- STATS_START -->
## 📊 Live Stats

| Metric | Value |
|---|---|
| Total Topics Learned | **2421** |
| Last Updated | `2026-10-05T22:39:07.303767+00:00` |
| Dataset Size | `2421 entries` |

## 📂 Categories Learned

| Category | Topics |
|---|---|
| data-structures | 1396 |
| trading-strategies | 228 |
| technical-analysis | 147 |
| crypto-blockchain | 129 |
| algorithms | 116 |
| market-analysis | 114 |
| system-design | 83 |
| stocks-markets | 71 |
| databases | 35 |
| probability-math | 27 |
| security | 20 |
| machine-learning | 15 |
| networking | 13 |
| web-dev | 9 |
| language-specific | 7 |
| devops | 7 |
| data-visualization | 2 |
| best-practices | 1 |
| testing | 1 |

## 🕐 Last 5 Topics Learned

- `Implementation of a lock-free thread-safe concurrent Skip-List using atomic forward-pointer-updating and node-splicing CAS primitives alongside hazard pointer memory reclamation for high-throughput ordered key-value lookup and multi-core sorted range querying in real-time in-memory databases and concurrent transactional storage engines`
- `Implementation of a lock-free thread-safe concurrent Interval Tree using atomic overlap-detecting and max-endpoint-updating CAS primitives alongside hazard pointer memory reclamation for high-throughput temporal range querying and multi-core resource scheduling in real-time calendar management systems and concurrent interval-overlap search engines`
- `Implementation of a lock-free thread-safe concurrent Binomial Heap using atomic root-linking and min-node-swapping CAS primitives alongside hazard pointer memory reclamation for high-throughput mergeable priority queue operations and multi-core task scheduling in real-time operating system kernels and concurrent event-driven simulation engines`
- `Implementation of a lock-free thread-safe concurrent Bε-Tree using atomic buffer-merging and leaf-splitting CAS primitives alongside hazard pointer memory reclamation for high-throughput write-optimized indexing and multi-core append-heavy logging in real-time LSM-tree storage engines and concurrent time-series databases`
- `Implementation of a lock-free thread-safe concurrent Fibonacci Heap using atomic min-pointer-updating and node-degree-linking CAS primitives alongside hazard pointer memory reclamation for high-throughput Dijkstra shortest path routing and multi-core priority queue operations in real-time network traffic optimization engines and concurrent graph analytics pipelines`

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
