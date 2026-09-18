# 🧠 Gemini Coding Brain

> An autonomous AI agent that learns coding concepts every day using the Gemini API,
> commits its growing knowledge base to GitHub automatically, and builds a fine-tuning
> dataset for future offline model training.

<!-- STATS_START -->
## 📊 Live Stats

| Metric | Value |
|---|---|
| Total Topics Learned | **1152** |
| Last Updated | `2026-09-18T14:19:45.003515+00:00` |
| Dataset Size | `1152 entries` |

## 📂 Categories Learned

| Category | Topics |
|---|---|
| data-structures | 300 |
| trading-strategies | 228 |
| technical-analysis | 147 |
| market-analysis | 114 |
| crypto-blockchain | 86 |
| system-design | 77 |
| stocks-markets | 71 |
| algorithms | 27 |
| probability-math | 27 |
| databases | 20 |
| machine-learning | 10 |
| web-dev | 9 |
| security | 9 |
| networking | 9 |
| language-specific | 7 |
| devops | 7 |
| data-visualization | 2 |
| best-practices | 1 |
| testing | 1 |

## 🕐 Last 5 Topics Learned

- `Implementation of a lock-free thread-safe concurrent Leftist Heap using atomic null-path-length root-linking CAS primitives and hazard pointer memory reclamation for high-throughput mergeable priority queue operations in real-time job scheduling and priority-based task dispatching engines`
- `Implementation of a lock-free thread-safe concurrent B+ Tree using atomic leaf-sibling pointer CAS primitives and epoch-based memory reclamation for high-throughput range queries and concurrent updates in real-time transactional storage engines`
- `Implementation of a lock-free thread-safe concurrent Treap using atomic randomized-priority rotation CAS primitives and hazard pointer memory reclamation for high-throughput balanced search tree operations in real-time in-memory databases and concurrent key-value indexing engines`
- `Implementation of a lock-free thread-safe concurrent Fenwick Tree (Binary Indexed Tree) using atomic prefix-sum updating CAS primitives and epoch-based memory reclamation for high-throughput cumulative frequency queries and dynamic rank updates in real-time stream analytics and financial order-book engines`
- `Implementation of a lock-free thread-safe concurrent Skip Graph using atomic peer-pointer routing CAS primitives and hazard pointer memory reclamation for high-throughput decentralized peer-to-peer searching and distributed hash table routing in real-time distributed file systems and cloud storage engines`

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
