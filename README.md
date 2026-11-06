# 🧠 Gemini Coding Brain

> An autonomous AI agent that learns coding concepts every day using the Gemini API,
> commits its growing knowledge base to GitHub automatically, and builds a fine-tuning
> dataset for future offline model training.

<!-- STATS_START -->
## 📊 Live Stats

| Metric | Value |
|---|---|
| Total Topics Learned | **4572** |
| Last Updated | `2026-11-06T20:46:30.534197+00:00` |
| Dataset Size | `4572 entries` |

## 📂 Categories Learned

| Category | Topics |
|---|---|
| data-structures | 3244 |
| algorithms | 273 |
| trading-strategies | 228 |
| crypto-blockchain | 192 |
| technical-analysis | 147 |
| system-design | 121 |
| market-analysis | 114 |
| stocks-markets | 71 |
| databases | 48 |
| security | 38 |
| probability-math | 27 |
| networking | 22 |
| machine-learning | 19 |
| web-dev | 9 |
| language-specific | 7 |
| devops | 7 |
| best-practices | 2 |
| data-visualization | 2 |
| testing | 1 |

## 🕐 Last 5 Topics Learned

- `Implementation of a lock-free thread-safe concurrent Suffix Array using atomic index-sorting and LCP-array-building CAS primitives alongside hazard pointer memory reclamation for high-throughput substring indexing and multi-core parallel genome sequence analysis execution in real-time bioinformatics data processing systems and concurrent text mining engines`
- `Implementation of a lock-free thread-safe concurrent Cover Tree using atomic hierarchical-level-linking and distance-threshold-cas primitives alongside hazard pointer memory reclamation for high-throughput multi-dimensional nearest-neighbor searching and multi-core parallel metric space querying execution in real-time machine learning similarity search engines and concurrent recommendation systems`
- `Implementation of a lock-free thread-safe concurrent Skip Graph using atomic peer-pointer-updating and membership-vector-routing CAS primitives alongside hazard pointer memory reclamation for high-throughput decentralized searching and multi-core parallel distributed routing execution in real-time peer-to-peer overlay networks and concurrent decentralized storage systems`
- `Implementation of a lock-free thread-safe concurrent Cuckoo Filter using atomic bucket-slot-swapping and kick-out-path CAS primitives alongside hazard pointer memory reclamation for high-throughput space-efficient approximate membership checking and multi-core parallel item deletion execution in real-time distributed caching systems and concurrent database storage engines`
- `Implementation of a lock-free thread-safe concurrent Skip List using atomic forward-pointer-cas and node-tower-splicing primitives alongside hazard pointer memory reclamation for high-throughput ordered key-value map operations and multi-core parallel sorted range query execution in real-time in-memory database systems and concurrent cache storage engines`

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
