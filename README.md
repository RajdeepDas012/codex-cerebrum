# 🧠 Gemini Coding Brain

> An autonomous AI agent that learns coding concepts every day using the Gemini API,
> commits its growing knowledge base to GitHub automatically, and builds a fine-tuning
> dataset for future offline model training.

<!-- STATS_START -->
## 📊 Live Stats

| Metric | Value |
|---|---|
| Total Topics Learned | **4067** |
| Last Updated | `2026-10-28T12:33:07.233787+00:00` |
| Dataset Size | `4067 entries` |

## 📂 Categories Learned

| Category | Topics |
|---|---|
| data-structures | 2793 |
| algorithms | 245 |
| trading-strategies | 228 |
| crypto-blockchain | 177 |
| technical-analysis | 147 |
| system-design | 120 |
| market-analysis | 114 |
| stocks-markets | 71 |
| databases | 44 |
| security | 34 |
| probability-math | 27 |
| networking | 21 |
| machine-learning | 18 |
| web-dev | 9 |
| language-specific | 7 |
| devops | 7 |
| best-practices | 2 |
| data-visualization | 2 |
| testing | 1 |

## 🕐 Last 5 Topics Learned

- `Implementation of a lock-free thread-safe concurrent Skip List using atomic tower-height-scaling and forward-pointer-splicing CAS primitives alongside hazard pointer memory reclamation for high-throughput ordered key-value lookup and multi-core parallel range iteration in real-time in-memory key-value stores and concurrent transactional database indexing engines`
- `Implementation of a lock-free thread-safe concurrent Splay Tree using atomic root-rotation and zig-zag-splicing CAS primitives alongside hazard pointer memory reclamation for high-throughput self-adjusting search queries and multi-core parallel frequently-accessed node optimization in real-time caching proxies and concurrent memory management systems`
- `Implementation of a lock-free thread-safe concurrent Priority Search Tree using atomic coordinate-merging and range-filtering CAS primitives alongside hazard pointer memory reclamation for high-throughput two-dimensional orthogonal range queries and multi-core parallel spatial database indexing in real-time geographic positioning platforms and concurrent GIS spatial analytics engines`
- `Implementation of a lock-free thread-safe concurrent Quadtree using atomic quad-node-splitting and bounding-box-intersecting CAS primitives alongside hazard pointer memory reclamation for high-throughput 2D spatial indexing and multi-core parallel point-location queries in real-time geospatial information systems and concurrent location-based gaming engines`
- `Implementation of a lock-free thread-safe concurrent B+ Tree using atomic sibling-pointer-linking and leaf-node-splitting CAS primitives alongside hazard pointer memory reclamation for high-throughput indexed range queries and multi-core parallel sorted data access in real-time relational database systems and concurrent transactional storage engines`

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
