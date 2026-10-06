# 🧠 Gemini Coding Brain

> An autonomous AI agent that learns coding concepts every day using the Gemini API,
> commits its growing knowledge base to GitHub automatically, and builds a fine-tuning
> dataset for future offline model training.

<!-- STATS_START -->
## 📊 Live Stats

| Metric | Value |
|---|---|
| Total Topics Learned | **2445** |
| Last Updated | `2026-10-06T03:32:45.128163+00:00` |
| Dataset Size | `2445 entries` |

## 📂 Categories Learned

| Category | Topics |
|---|---|
| data-structures | 1414 |
| trading-strategies | 228 |
| technical-analysis | 147 |
| crypto-blockchain | 131 |
| algorithms | 118 |
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

- `Implementation of a lock-free thread-safe concurrent Fenwick Tree (Binary Indexed Tree) using atomic prefix-sum-updating and node-value-cascading CAS primitives alongside hazard pointer memory reclamation for high-throughput cumulative frequency querying and multi-core rank tracking in real-time stream processing engines and concurrent statistical monitoring systems`
- `Implementation of a lock-free thread-safe concurrent B-Tree using atomic node-splitting and structural-modification-operation (SMO) descriptor CAS primitives alongside hazard pointer memory reclamation for high-throughput concurrent indexed searching and multi-core database record updating in real-time enterprise storage engines and concurrent in-memory caching systems`
- `Implementation of a lock-free thread-safe concurrent Leftist Heap using atomic null-path-length-updating and priority-merging CAS primitives alongside hazard pointer memory reclamation for high-throughput mergeable priority queue operations and multi-core task scheduling in real-time operating system kernels and concurrent event-driven simulation engines`
- `Implementation of a lock-free thread-safe concurrent Levenberg-Marquardt optimizer using atomic Jacobian-updating and damping-factor-adjusting CAS primitives alongside hazard pointer memory reclamation for high-throughput non-linear curve fitting and multi-core parameter estimation in real-time robotics calibration systems and concurrent computer vision sensor fusion engines`
- `Implementation of a lock-free thread-safe concurrent Treap using atomic randomized-priority-balancing and tree-rotation CAS primitives alongside hazard pointer memory reclamation for high-throughput probabilistic balanced searching and multi-core randomized priority sorting in real-time in-memory databases and concurrent probabilistic map structures`

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
