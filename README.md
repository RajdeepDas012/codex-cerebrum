# 🧠 Gemini Coding Brain

> An autonomous AI agent that learns coding concepts every day using the Gemini API,
> commits its growing knowledge base to GitHub automatically, and builds a fine-tuning
> dataset for future offline model training.

<!-- STATS_START -->
## 📊 Live Stats

| Metric | Value |
|---|---|
| Total Topics Learned | **2438** |
| Last Updated | `2026-10-06T03:08:44.552828+00:00` |
| Dataset Size | `2438 entries` |

## 📂 Categories Learned

| Category | Topics |
|---|---|
| data-structures | 1409 |
| trading-strategies | 228 |
| technical-analysis | 147 |
| crypto-blockchain | 130 |
| algorithms | 117 |
| market-analysis | 114 |
| system-design | 83 |
| stocks-markets | 71 |
| databases | 36 |
| probability-math | 27 |
| security | 20 |
| machine-learning | 15 |
| networking | 13 |
| web-dev | 9 |
| language-specific | 7 |
| devops | 7 |
| best-practices | 2 |
| data-visualization | 2 |
| testing | 1 |

## 🕐 Last 5 Topics Learned

- `Implementation of a lock-free thread-safe concurrent Suffix Array using atomic index-sorting and LCP-array-constructing CAS primitives alongside hazard pointer memory reclamation for high-throughput substring querying and multi-core pattern matching in real-time genome sequencing pipelines and concurrent text search engines`
- `Implementation of a lock-free thread-safe concurrent Merkle Tree using atomic hash-propagating and node-rebuilding CAS primitives alongside hazard pointer memory reclamation for high-throughput cryptographic state verification and multi-core data integrity checking in real-time distributed ledger systems and concurrent blockchain synchronization engines`
- `Implementation of a lock-free thread-safe concurrent Scoped Read-Copy Update (RCU) mechanism using atomic epoch-advancing and deferred-free-callback-queuing CAS primitives alongside hazard pointer memory reclamation for high-throughput read-mostly synchronization and multi-core reference tracking in real-time operating system kernel modules and concurrent in-memory configuration stores`
- `Implementation of a lock-free thread-safe concurrent K-d Tree using atomic bounding-hyperplane-updating and axis-splitting CAS primitives alongside hazard pointer memory reclamation for high-throughput multi-dimensional nearest neighbor searching and multi-core point cloud querying in real-time robotics perception systems and concurrent computer graphics acceleration pipelines`
- `Implementation of a lock-free thread-safe concurrent Priority Queue using atomic heap-node-cascading and pointer-swapping CAS primitives alongside hazard pointer memory reclamation for high-throughput task scheduling and multi-core thread pool management in real-time operating systems and concurrent job dispatching engines`

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
