# 🧠 Gemini Coding Brain

> An autonomous AI agent that learns coding concepts every day using the Gemini API,
> commits its growing knowledge base to GitHub automatically, and builds a fine-tuning
> dataset for future offline model training.

<!-- STATS_START -->
## 📊 Live Stats

| Metric | Value |
|---|---|
| Total Topics Learned | **1605** |
| Last Updated | `2026-09-24T00:05:39.837190+00:00` |
| Dataset Size | `1605 entries` |

## 📂 Categories Learned

| Category | Topics |
|---|---|
| data-structures | 692 |
| trading-strategies | 228 |
| technical-analysis | 147 |
| market-analysis | 114 |
| crypto-blockchain | 103 |
| system-design | 83 |
| stocks-markets | 71 |
| algorithms | 50 |
| databases | 27 |
| probability-math | 27 |
| security | 14 |
| machine-learning | 11 |
| networking | 11 |
| web-dev | 9 |
| language-specific | 7 |
| devops | 7 |
| data-visualization | 2 |
| best-practices | 1 |
| testing | 1 |

## 🕐 Last 5 Topics Learned

- `Implementation of a lock-free thread-safe concurrent Treap using atomic randomized-priority-balancing and tree-rotation CAS primitives alongside hazard pointer memory reclamation for high-throughput randomized search operations and multi-core priority dictionary management in real-time distributed key-value stores and message-broker routing tables`
- `Implementation of a lock-free thread-safe concurrent Interval Tree using atomic overlap-detecting and interval-endpoint-updating CAS primitives alongside hazard pointer memory reclamation for high-throughput range-overlapping queries and multi-core interval scheduling in real-time calendar management systems and network firewall packet-filtering engines`
- `Implementation of a lock-free thread-safe concurrent B-Tree using atomic node-splitting and structural-merging CAS primitives alongside hazard pointer memory reclamation for high-throughput range querying and multi-core index management in real-time enterprise database storage and high-frequency transaction processing engines`
- `Implementation of a lock-free thread-safe concurrent Bloom Filter using atomic bit-setting and word-cascading CAS primitives alongside hazard pointer memory reclamation for high-throughput approximate membership testing and multi-core set-membership verification in real-time distributed caching and security proxy engines`
- `Implementation of a lock-free thread-safe concurrent Left-Leaning Red-Black Tree using atomic color-flipping and rotation CAS primitives alongside hazard pointer memory reclamation for high-throughput balanced tree updates and multi-core sorted indexing in real-time in-memory databases and concurrent stream processing engines`

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
