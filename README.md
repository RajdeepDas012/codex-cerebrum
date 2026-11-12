# 🧠 Gemini Coding Brain

> An autonomous AI agent that learns coding concepts every day using the Gemini API,
> commits its growing knowledge base to GitHub automatically, and builds a fine-tuning
> dataset for future offline model training.

<!-- STATS_START -->
## 📊 Live Stats

| Metric | Value |
|---|---|
| Total Topics Learned | **4824** |
| Last Updated | `2026-11-12T17:54:22.621664+00:00` |
| Dataset Size | `4824 entries` |

## 📂 Categories Learned

| Category | Topics |
|---|---|
| data-structures | 3455 |
| algorithms | 298 |
| trading-strategies | 228 |
| crypto-blockchain | 200 |
| technical-analysis | 147 |
| system-design | 121 |
| market-analysis | 114 |
| stocks-markets | 71 |
| databases | 50 |
| security | 40 |
| probability-math | 27 |
| networking | 23 |
| machine-learning | 22 |
| web-dev | 9 |
| language-specific | 7 |
| devops | 7 |
| best-practices | 2 |
| data-visualization | 2 |
| testing | 1 |

## 🕐 Last 5 Topics Learned

- `Implementation of a lock-free thread-safe concurrent Interval Tree using atomic endpoint-updating and max-right-tracking CAS primitives alongside hazard pointer memory reclamation for high-throughput overlapping range querying and multi-core parallel time-interval intersection execution in real-time calendar scheduling systems and concurrent event-driven simulation engines`
- `Implementation of a lock-free thread-safe concurrent Vantage-Point Tree using atomic distance-partitioning and metric-radius-bounding CAS primitives alongside hazard pointer memory reclamation for high-throughput similarity searching and multi-core parallel high-dimensional metric space query execution in real-time multimedia retrieval systems and concurrent computer vision feature matching engines`
- `Implementation of a lock-free thread-safe concurrent Suffix Automaton using atomic state-transition-linking and node-cloning CAS primitives alongside hazard pointer memory reclamation for high-throughput substring indexing and multi-core parallel pattern matching execution in real-time text editing applications and concurrent bioinformatics sequence alignment engines`
- `Implementation of a lock-free thread-safe concurrent Skip List using atomic tower-height-allocating and forward-pointer-splicing CAS primitives alongside hazard pointer memory reclamation for high-throughput probabilistic ordered set indexing and multi-core parallel sorted map execution in real-time in-memory databases and concurrent caching storage engines`
- `Implementation of a lock-free thread-safe concurrent Cuckoo Filter using atomic bucket-swapping and fingerprint-relocation CAS primitives alongside hazard pointer memory reclamation for high-throughput space-efficient item deletion and multi-core parallel probabilistic membership testing execution in real-time distributed key-value caches and concurrent network security packet filtering engines`

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
