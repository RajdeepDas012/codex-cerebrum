# 🧠 Gemini Coding Brain

> An autonomous AI agent that learns coding concepts every day using the Gemini API,
> commits its growing knowledge base to GitHub automatically, and builds a fine-tuning
> dataset for future offline model training.

<!-- STATS_START -->
## 📊 Live Stats

| Metric | Value |
|---|---|
| Total Topics Learned | **1697** |
| Last Updated | `2026-09-25T07:28:08.914498+00:00` |
| Dataset Size | `1697 entries` |

## 📂 Categories Learned

| Category | Topics |
|---|---|
| data-structures | 774 |
| trading-strategies | 228 |
| technical-analysis | 147 |
| market-analysis | 114 |
| crypto-blockchain | 105 |
| system-design | 83 |
| stocks-markets | 71 |
| algorithms | 55 |
| databases | 28 |
| probability-math | 27 |
| security | 15 |
| networking | 12 |
| machine-learning | 11 |
| web-dev | 9 |
| language-specific | 7 |
| devops | 7 |
| data-visualization | 2 |
| best-practices | 1 |
| testing | 1 |

## 🕐 Last 5 Topics Learned

- `Implementation of a lock-free thread-safe concurrent Radix-Tree (Patricia Trie) using atomic edge-splitting and compression-path CAS primitives alongside hazard pointer memory reclamation for high-throughput IP address routing and multi-core prefix lookup in real-time software-defined networking and telecommunication switching engines`
- `Implementation of a lock-free thread-safe concurrent Lock-Free Ring Buffer (Disruptor pattern) using atomic sequence-wrapping and cursor-advancing CAS primitives alongside hazard pointer memory reclamation for high-throughput inter-thread messaging and multi-core event sourcing in real-time financial trading systems and low-latency telemetry pipelines`
- `Implementation of a lock-free thread-safe concurrent Bloom Filter using atomic bit-setting and hash-combining CAS primitives alongside hazard pointer memory reclamation for high-throughput probabilistic set membership querying and multi-core duplicate filtering in real-time distributed web crawlers and high-speed database caching engines`
- `Implementation of a lock-free thread-safe concurrent Priority Queue using atomic heap-node-promoting and dual-ended-balancing CAS primitives alongside hazard pointer memory reclamation for high-throughput concurrent task prioritization and multi-core asynchronous job dispatching in real-time distributed execution engines and high-frequency trading platforms`
- `Implementation of a lock-free thread-safe concurrent Skip List using atomic forward-pointer-linking and node-tower-splicing CAS primitives alongside hazard pointer memory reclamation for high-throughput ordered key-value lookup and multi-core range querying in real-time in-memory databases and concurrent transactional storage engines`

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
