# 🧠 Gemini Coding Brain

> An autonomous AI agent that learns coding concepts every day using the Gemini API,
> commits its growing knowledge base to GitHub automatically, and builds a fine-tuning
> dataset for future offline model training.

<!-- STATS_START -->
## 📊 Live Stats

| Metric | Value |
|---|---|
| Total Topics Learned | **5290** |
| Last Updated | `2026-11-23T08:53:55.682711+00:00` |
| Dataset Size | `5290 entries` |

## 📂 Categories Learned

| Category | Topics |
|---|---|
| data-structures | 3869 |
| algorithms | 329 |
| trading-strategies | 228 |
| crypto-blockchain | 213 |
| technical-analysis | 147 |
| system-design | 121 |
| market-analysis | 114 |
| stocks-markets | 71 |
| databases | 53 |
| security | 42 |
| probability-math | 27 |
| networking | 26 |
| machine-learning | 22 |
| web-dev | 9 |
| language-specific | 7 |
| devops | 7 |
| best-practices | 2 |
| data-visualization | 2 |
| testing | 1 |

## 🕐 Last 5 Topics Learned

- `Implementation of a lock-free thread-safe concurrent Fenwick Tree using atomic point-updating and prefix-sum-calculating CAS primitives alongside hazard pointer memory reclamation for high-throughput cumulative frequency tracking and multi-core parallel rank query execution in real-time streaming analytics engines and concurrent game leaderboards`
- `Implementation of a lock-free thread-safe concurrent Radix Tree using atomic bit-testing and child-pointer-swinging CAS primitives alongside hazard pointer memory reclamation for high-throughput IP routing table lookups and multi-core parallel prefix matching execution in real-time software-defined networking packet forwarders and concurrent operating system network stack layers`
- `Implementation of a lock-free thread-safe concurrent Fibonacci Heap using atomic min-pointer-updating and node-degree-linking CAS primitives alongside hazard pointer memory reclamation for high-throughput amortized priority queue operations and multi-core parallel shortest path execution in real-time graph processing engines and concurrent network routing simulators`
- `Implementation of a lock-free thread-safe concurrent Bloom Filter using atomic bit-setting and word-cas-masking CAS primitives alongside hazard pointer memory reclamation for high-throughput probabilistic set membership testing and multi-core parallel duplicate URL checking execution in real-time web crawler filtering systems and concurrent database query caching layers`
- `Implementation of a lock-free thread-safe concurrent B-link Tree using atomic right-link-navigating and leaf-splitting CAS primitives alongside hazard pointer memory reclamation for high-throughput concurrent index traversal and multi-core parallel sorted range query execution in real-time relational database engines and concurrent in-memory storage systems`

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
