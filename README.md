# 🧠 Gemini Coding Brain

> An autonomous AI agent that learns coding concepts every day using the Gemini API,
> commits its growing knowledge base to GitHub automatically, and builds a fine-tuning
> dataset for future offline model training.

<!-- STATS_START -->
## 📊 Live Stats

| Metric | Value |
|---|---|
| Total Topics Learned | **4835** |
| Last Updated | `2026-11-12T23:47:50.441809+00:00` |
| Dataset Size | `4835 entries` |

## 📂 Categories Learned

| Category | Topics |
|---|---|
| data-structures | 3465 |
| algorithms | 299 |
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

- `Implementation of a lock-free thread-safe concurrent Persistent Segment Tree using atomic version-branching and node-sharing CAS primitives alongside hazard pointer memory reclamation for high-throughput historical range querying and multi-core parallel time-travel analytical execution in real-time financial auditing platforms and concurrent version-controlled database engines`
- `Implementation of a lock-free thread-safe concurrent Segment Tree using atomic lazy-propagation-marking and range-minimum-updating CAS primitives alongside hazard pointer memory reclamation for high-throughput range query optimization and multi-core parallel interval update execution in real-time financial trading systems and concurrent analytics engines`
- `Implementation of a lock-free thread-safe concurrent Suffix Tree using atomic node-splitting and suffix-link-updating CAS primitives alongside hazard pointer memory reclamation for high-throughput exact string matching and multi-core parallel bioinformatics pattern discovery execution in real-time genomic sequence analysis engines and concurrent text indexing pipelines`
- `Implementation of a lock-free thread-safe concurrent KD-Tree using atomic bounding-hyperplane-splitting and axis-cycling CAS primitives alongside hazard pointer memory reclamation for high-throughput multi-dimensional nearest neighbor searching and multi-core parallel spatial point query execution in real-time robotics perception systems and concurrent geographic information databases`
- `Implementation of a lock-free thread-safe concurrent Wavelet Tree using atomic bitmap-splitting and rank-select-querying CAS primitives alongside hazard pointer memory reclamation for high-throughput compressed text indexing and multi-core parallel succinct data structure execution in real-time bioinformatics sequence analysis engines and concurrent compressed column store databases`

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
