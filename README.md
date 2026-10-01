# 🧠 Gemini Coding Brain

> An autonomous AI agent that learns coding concepts every day using the Gemini API,
> commits its growing knowledge base to GitHub automatically, and builds a fine-tuning
> dataset for future offline model training.

<!-- STATS_START -->
## 📊 Live Stats

| Metric | Value |
|---|---|
| Total Topics Learned | **2154** |
| Last Updated | `2026-10-01T23:26:44.162970+00:00` |
| Dataset Size | `2154 entries` |

## 📂 Categories Learned

| Category | Topics |
|---|---|
| data-structures | 1162 |
| trading-strategies | 228 |
| technical-analysis | 147 |
| crypto-blockchain | 121 |
| market-analysis | 114 |
| algorithms | 97 |
| system-design | 83 |
| stocks-markets | 71 |
| databases | 33 |
| probability-math | 27 |
| security | 18 |
| machine-learning | 14 |
| networking | 12 |
| web-dev | 9 |
| language-specific | 7 |
| devops | 7 |
| data-visualization | 2 |
| best-practices | 1 |
| testing | 1 |

## 🕐 Last 5 Topics Learned

- `Implementation of a lock-free thread-safe concurrent Persistent Segment Tree using atomic version-node-linking and path-copying CAS primitives alongside hazard pointer memory reclamation for high-throughput historical range queries and multi-core snapshot isolation in real-time functional data processing engines and concurrent time-travel database systems`
- `Implementation of a lock-free thread-safe concurrent LSA (Latent Semantic Analysis) matrix factorization engine using atomic gradient-updating and singular-value-decomposition CAS primitives alongside hazard pointer memory reclamation for high-throughput semantic document similarity searches and multi-core latent vector projection in real-time natural language processing pipelines and concurrent information retrieval systems`
- `Implementation of a lock-free thread-safe concurrent B-link Tree using atomic right-link-traversal and latch-free-node-splitting CAS primitives alongside hazard pointer memory reclamation for high-throughput concurrent record searching and multi-core horizontal database scaling in real-time online transaction processing engines and concurrent database management systems`
- `Implementation of a lock-free thread-safe concurrent Bx-Tree using atomic key-redirection and node-merging CAS primitives alongside hazard pointer memory reclamation for high-throughput temporal database versioning and multi-core append-only index management in real-time time-series analytics engines and concurrent archival storage systems`
- `Implementation of a lock-free thread-safe concurrent Link-Cut Tree using atomic path-parent-updating and preferred-child-splicing CAS primitives alongside hazard pointer memory reclamation for high-throughput dynamic tree operations and multi-core network flow optimization in real-time routing protocol analysis systems and concurrent graph algorithm execution engines`

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
