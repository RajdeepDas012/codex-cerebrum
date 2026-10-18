# 🧠 Gemini Coding Brain

> An autonomous AI agent that learns coding concepts every day using the Gemini API,
> commits its growing knowledge base to GitHub automatically, and builds a fine-tuning
> dataset for future offline model training.

<!-- STATS_START -->
## 📊 Live Stats

| Metric | Value |
|---|---|
| Total Topics Learned | **3330** |
| Last Updated | `2026-10-18T23:25:31.150012+00:00` |
| Dataset Size | `3330 entries` |

## 📂 Categories Learned

| Category | Topics |
|---|---|
| data-structures | 2150 |
| trading-strategies | 228 |
| algorithms | 201 |
| crypto-blockchain | 155 |
| technical-analysis | 147 |
| market-analysis | 114 |
| system-design | 110 |
| stocks-markets | 71 |
| databases | 40 |
| security | 27 |
| probability-math | 27 |
| machine-learning | 16 |
| networking | 16 |
| web-dev | 9 |
| language-specific | 7 |
| devops | 7 |
| best-practices | 2 |
| data-visualization | 2 |
| testing | 1 |

## 🕐 Last 5 Topics Learned

- `Implementation of a lock-free thread-safe concurrent Work-Stealing Deque using atomic top-bottom-pointer-adjusting and descriptor-stealing CAS primitives alongside hazard pointer memory reclamation for high-throughput task scheduling and multi-core parallel load balancing in real-time actor runtimes and concurrent fork-join execution engines`
- `Implementation of a lock-free thread-safe concurrent Priority Queue using atomic heap-node-swapping and index-tracking CAS primitives alongside hazard pointer memory reclamation for high-throughput task prioritization and multi-core parallel job scheduling in real-time event-driven engines and concurrent task execution frameworks`
- `Implementation of a lock-free thread-safe concurrent Futex-based lightweight mutex using atomic state-transition and thread-parking CAS primitives alongside hazard pointer memory reclamation for high-throughput synchronization and multi-core parallel resource locking in real-time operating system runtimes and concurrent systems programming frameworks`
- `Implementation of a lock-free thread-safe concurrent Suffix Tree using atomic node-stitching and edge-splitting CAS primitives alongside hazard pointer memory reclamation for high-throughput substring searching and multi-core parallel bioinformatics pattern matching in real-time genomic sequencing pipelines and concurrent text analytics systems`
- `Implementation of a lock-free thread-safe concurrent Concurrent Queue using atomic head-tail-node-advancing and enqueue-dequeue-pointer-splicing CAS primitives alongside hazard pointer memory reclamation for high-throughput multi-producer multi-consumer task handoff and multi-core parallel message passing in real-time asynchronous execution engines and concurrent actor frameworks`

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
