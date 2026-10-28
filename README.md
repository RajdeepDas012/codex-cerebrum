# 🧠 Gemini Coding Brain

> An autonomous AI agent that learns coding concepts every day using the Gemini API,
> commits its growing knowledge base to GitHub automatically, and builds a fine-tuning
> dataset for future offline model training.

<!-- STATS_START -->
## 📊 Live Stats

| Metric | Value |
|---|---|
| Total Topics Learned | **4054** |
| Last Updated | `2026-10-28T05:12:04.266341+00:00` |
| Dataset Size | `4054 entries` |

## 📂 Categories Learned

| Category | Topics |
|---|---|
| data-structures | 2782 |
| algorithms | 245 |
| trading-strategies | 228 |
| crypto-blockchain | 176 |
| technical-analysis | 147 |
| system-design | 120 |
| market-analysis | 114 |
| stocks-markets | 71 |
| databases | 44 |
| security | 34 |
| probability-math | 27 |
| networking | 20 |
| machine-learning | 18 |
| web-dev | 9 |
| language-specific | 7 |
| devops | 7 |
| best-practices | 2 |
| data-visualization | 2 |
| testing | 1 |

## 🕐 Last 5 Topics Learned

- `Implementation of a lock-free thread-safe concurrent HyperLogLog using atomic register-updating and max-value-merging CAS primitives alongside hazard pointer memory reclamation for high-throughput cardinality estimation and multi-core parallel distinct element counting in real-time web analytics platforms and concurrent data streaming engines`
- `Implementation of a lock-free thread-safe concurrent Count-Min Sketch using atomic frequency-incrementing and matrix-row-updating CAS primitives alongside hazard pointer memory reclamation for high-throughput heavy-hitter stream frequency estimations and multi-core parallel streaming traffic analysis in real-time network telemetry platforms and concurrent log monitoring engines`
- `Implementation of a lock-free thread-safe concurrent Bloom Filter using atomic bit-setting and word-cas primitives alongside hazard pointer memory reclamation for high-throughput probabilistic set membership tests and multi-core parallel duplicate filtering in real-time web crawler platforms and concurrent database cache indexing engines`
- `Implementation of a lock-free thread-safe concurrent Levenberg-Marquardt optimizer using atomic damping-parameter-updating and Jacobian-matrix-accumulating CAS primitives alongside hazard pointer memory reclamation for high-throughput non-linear least squares fitting and multi-core parallel parameter estimation in real-time camera calibration platforms and concurrent robotics sensor fusion engines`
- `Implementation of a lock-free thread-safe concurrent HNSW (Hierarchical Navigable Small World) graph using atomic entry-point-updating and bidirectional-link-establishing CAS primitives alongside hazard pointer memory reclamation for high-throughput approximate nearest neighbor searches and multi-core parallel vector embedding queries in real-time semantic search platforms and concurrent neural information retrieval engines`

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
