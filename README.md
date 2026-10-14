# 🧠 Gemini Coding Brain

> An autonomous AI agent that learns coding concepts every day using the Gemini API,
> commits its growing knowledge base to GitHub automatically, and builds a fine-tuning
> dataset for future offline model training.

<!-- STATS_START -->
## 📊 Live Stats

| Metric | Value |
|---|---|
| Total Topics Learned | **2951** |
| Last Updated | `2026-10-14T18:38:20.791348+00:00` |
| Dataset Size | `2951 entries` |

## 📂 Categories Learned

| Category | Topics |
|---|---|
| data-structures | 1842 |
| trading-strategies | 228 |
| algorithms | 165 |
| technical-analysis | 147 |
| crypto-blockchain | 144 |
| market-analysis | 114 |
| system-design | 89 |
| stocks-markets | 71 |
| databases | 39 |
| probability-math | 27 |
| security | 25 |
| machine-learning | 16 |
| networking | 16 |
| web-dev | 9 |
| language-specific | 7 |
| devops | 7 |
| best-practices | 2 |
| data-visualization | 2 |
| testing | 1 |

## 🕐 Last 5 Topics Learned

- `Implementation of a lock-free thread-safe concurrent Vantage-Point Tree using atomic distance-partitioning and child-node-linking CAS primitives alongside hazard pointer memory reclamation for high-throughput metric space nearest-neighbor searching and multi-core similarity querying in real-time image retrieval platforms and concurrent recommendation engine databases`
- `Implementation of a lock-free thread-safe concurrent Aho-Corasick automaton using atomic state-transition and failure-link-updating CAS primitives alongside hazard pointer memory reclamation for high-throughput multi-pattern string matching and multi-core dictionary scanning in real-time intrusion detection systems and concurrent log analysis engines`
- `Implementation of a lock-free thread-safe concurrent Disjoint Set Union (Union-Find) using atomic path-compression and rank-merging CAS primitives alongside hazard pointer memory reclamation for high-throughput connected component querying and multi-core equivalence relation tracking in real-time social network analysis platforms and concurrent graph clustering engines`
- `Implementation of a lock-free thread-safe concurrent Fenwick Tree (Binary Indexed Tree) using atomic prefix-sum-updating and node-indexing CAS primitives alongside hazard pointer memory reclamation for high-throughput cumulative frequency querying and multi-core point-update processing in real-time stream aggregation platforms and concurrent statistical computing engines`
- `Implementation of a lock-free thread-safe concurrent Token Bucket rate limiter using atomic credit-replenishing and burst-permitting CAS primitives alongside hazard pointer memory reclamation for high-throughput traffic throttling and multi-core rate enforcement in real-time microservice API gateways and concurrent cloud ingress proxies`

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
