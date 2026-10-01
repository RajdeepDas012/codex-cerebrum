# 🧠 Gemini Coding Brain

> An autonomous AI agent that learns coding concepts every day using the Gemini API,
> commits its growing knowledge base to GitHub automatically, and builds a fine-tuning
> dataset for future offline model training.

<!-- STATS_START -->
## 📊 Live Stats

| Metric | Value |
|---|---|
| Total Topics Learned | **2124** |
| Last Updated | `2026-10-01T13:15:24.010735+00:00` |
| Dataset Size | `2124 entries` |

## 📂 Categories Learned

| Category | Topics |
|---|---|
| data-structures | 1136 |
| trading-strategies | 228 |
| technical-analysis | 147 |
| crypto-blockchain | 120 |
| market-analysis | 114 |
| algorithms | 96 |
| system-design | 83 |
| stocks-markets | 71 |
| databases | 32 |
| probability-math | 27 |
| security | 18 |
| machine-learning | 13 |
| networking | 12 |
| web-dev | 9 |
| language-specific | 7 |
| devops | 7 |
| data-visualization | 2 |
| best-practices | 1 |
| testing | 1 |

## 🕐 Last 5 Topics Learned

- `Implementation of a lock-free thread-safe concurrent Cover Tree using atomic distance-scale-adjustments and hierarchical-node-insertion CAS primitives alongside hazard pointer memory reclamation for high-throughput nearest neighbor classification and multi-core metric space searching in real-time machine learning inference engines and concurrent pattern recognition systems`
- `Implementation of a lock-free thread-safe concurrent Vantage-Point Tree using atomic pivot-selection and metric-space-partitioning CAS primitives alongside hazard pointer memory reclamation for high-throughput multi-dimensional similarity searches and multi-core high-dimensional nearest neighbor queries in real-time vector database indexing engines and concurrent multimedia retrieval systems`
- `Implementation of a lock-free thread-safe concurrent Skip-Quadtree using atomic quadrant-pointer-stitching and dynamic-node-pruning CAS primitives alongside hazard pointer memory reclamation for high-throughput spatial point indexing and multi-core collision detection in real-time location-based services platforms and concurrent geographical information systems`
- `Implementation of a lock-free thread-safe concurrent Persistent Segment Tree using atomic version-branching and node-sharing CAS primitives alongside hazard pointer memory reclamation for high-throughput historical interval querying and multi-core point-in-time state tracking in real-time financial audit systems and concurrent version-controlled database engines`
- `Implementation of a lock-free thread-safe concurrent Suffix Array using atomic index-sorting and doubling-step-merging CAS primitives alongside hazard pointer memory reclamation for high-throughput substring searching and multi-core pattern matching in real-time text mining analytics systems and concurrent bioinformatics sequence alignment engines`

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
