# 🧠 Gemini Coding Brain

> An autonomous AI agent that learns coding concepts every day using the Gemini API,
> commits its growing knowledge base to GitHub automatically, and builds a fine-tuning
> dataset for future offline model training.

<!-- STATS_START -->
## 📊 Live Stats

| Metric | Value |
|---|---|
| Total Topics Learned | **3967** |
| Last Updated | `2026-10-27T01:54:06.941984+00:00` |
| Dataset Size | `3967 entries` |

## 📂 Categories Learned

| Category | Topics |
|---|---|
| data-structures | 2704 |
| algorithms | 242 |
| trading-strategies | 228 |
| crypto-blockchain | 173 |
| technical-analysis | 147 |
| system-design | 119 |
| market-analysis | 114 |
| stocks-markets | 71 |
| databases | 44 |
| security | 33 |
| probability-math | 27 |
| networking | 20 |
| machine-learning | 17 |
| web-dev | 9 |
| language-specific | 7 |
| devops | 7 |
| best-practices | 2 |
| data-visualization | 2 |
| testing | 1 |

## 🕐 Last 5 Topics Learned

- `Implementation of a lock-free thread-safe concurrent Bounded Queue using atomic head-tail-advancing and ring-buffer-wrapping CAS primitives alongside hazard pointer memory reclamation for high-throughput single-producer single-consumer messaging and multi-core parallel work-stealing queues in real-time trading platforms and concurrent event-driven server engines`
- `Implementation of a lock-free thread-safe concurrent Fenwick Tree using atomic point-updating and prefix-sum-calculating CAS primitives alongside hazard pointer memory reclamation for high-throughput cumulative frequency queries and multi-core parallel prefix sum updates in real-time analytics platforms and concurrent stream processing engines`
- `Implementation of a lock-free thread-safe concurrent Merkle Tree using atomic cryptographic-hash-combining and branch-root-updating CAS primitives alongside hazard pointer memory reclamation for high-throughput cryptographic verification and multi-core parallel blockchain state validation in real-time distributed ledger platforms and concurrent trustless verification engines`
- `Implementation of a lock-free thread-safe concurrent B-Tree using atomic node-splitting and root-coalescing CAS primitives alongside hazard pointer memory reclamation for high-throughput concurrent record lookups and multi-core parallel dynamic sorting in real-time transactional database systems and concurrent key-value storage engines`
- `Implementation of a lock-free thread-safe concurrent Cuckoo Filter using atomic bucket-swapping and fingerprint-relocation CAS primitives alongside hazard pointer memory reclamation for high-throughput deletion-supported approximate membership testing and multi-core parallel set filtering in real-time distributed caching systems and concurrent database storage engines`

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
