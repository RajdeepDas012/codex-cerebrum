# 🧠 Gemini Coding Brain

> An autonomous AI agent that learns coding concepts every day using the Gemini API,
> commits its growing knowledge base to GitHub automatically, and builds a fine-tuning
> dataset for future offline model training.

<!-- STATS_START -->
## 📊 Live Stats

| Metric | Value |
|---|---|
| Total Topics Learned | **3127** |
| Last Updated | `2026-10-16T23:23:35.293578+00:00` |
| Dataset Size | `3127 entries` |

## 📂 Categories Learned

| Category | Topics |
|---|---|
| data-structures | 1986 |
| trading-strategies | 228 |
| algorithms | 180 |
| crypto-blockchain | 149 |
| technical-analysis | 147 |
| market-analysis | 114 |
| system-design | 100 |
| stocks-markets | 71 |
| databases | 39 |
| probability-math | 27 |
| security | 26 |
| machine-learning | 16 |
| networking | 16 |
| web-dev | 9 |
| language-specific | 7 |
| devops | 7 |
| best-practices | 2 |
| data-visualization | 2 |
| testing | 1 |

## 🕐 Last 5 Topics Learned

- `Implementation of a lock-free thread-safe concurrent Bounded Priority Queue using atomic heap-array-sinking and priority-masking CAS primitives alongside hazard pointer memory reclamation for high-throughput bounded-capacity task prioritization and multi-core thread scheduling in real-time embedded telemetry systems and concurrent job dispatch execution engines`
- `Implementation of a lock-free thread-safe concurrent Cuckoo Hash Table using atomic bucket-relocating and table-resizing CAS primitives alongside hazard pointer memory reclamation for high-throughput key-value lookups and multi-core high-load dynamic resizing in real-time in-memory caching systems and concurrent distributed storage execution engines`
- `Implementation of a lock-free thread-safe concurrent Bloom Filter using atomic bit-vector-updating and double-hashing CAS primitives alongside hazard pointer memory reclamation for high-throughput space-efficient probabilistic set membership testing and multi-core duplicate filtering in real-time distributed database query engines and concurrent web caching proxy servers`
- `Implementation of a lock-free thread-safe concurrent Suffix Automaton using atomic state-transition-extending and link-updating CAS primitives alongside hazard pointer memory reclamation for high-throughput substring indexing and multi-core text pattern searching in real-time data compression engines and concurrent bioinformatics sequence alignment systems`
- `Implementation of a lock-free thread-safe concurrent LFU (Least Frequently Used) Cache using atomic frequency-counter-incrementing and doubly-linked-bucket-splicing CAS primitives alongside hazard pointer memory reclamation for high-throughput eviction policy management and multi-core high-frequency data access in real-time in-memory caching systems and concurrent database storage engines`

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
