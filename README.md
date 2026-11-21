# 🧠 Gemini Coding Brain

> An autonomous AI agent that learns coding concepts every day using the Gemini API,
> commits its growing knowledge base to GitHub automatically, and builds a fine-tuning
> dataset for future offline model training.

<!-- STATS_START -->
## 📊 Live Stats

| Metric | Value |
|---|---|
| Total Topics Learned | **5214** |
| Last Updated | `2026-11-21T17:18:23.631413+00:00` |
| Dataset Size | `5214 entries` |

## 📂 Categories Learned

| Category | Topics |
|---|---|
| data-structures | 3802 |
| algorithms | 325 |
| trading-strategies | 228 |
| crypto-blockchain | 211 |
| technical-analysis | 147 |
| system-design | 121 |
| market-analysis | 114 |
| stocks-markets | 71 |
| databases | 52 |
| security | 41 |
| probability-math | 27 |
| networking | 25 |
| machine-learning | 22 |
| web-dev | 9 |
| language-specific | 7 |
| devops | 7 |
| best-practices | 2 |
| data-visualization | 2 |
| testing | 1 |

## 🕐 Last 5 Topics Learned

- `Implementation of a lock-free thread-safe concurrent Treap using atomic randomized-priority-balancing and tree-rotation CAS primitives alongside hazard pointer memory reclamation for high-throughput probabilistic balanced search tree operations and multi-core parallel ordered set manipulation execution in real-time in-memory caching platforms and concurrent key-value storage systems`
- `Implementation of a lock-free thread-safe concurrent R-Tree using atomic bounding-box-adjusting and node-splitting CAS primitives alongside hazard pointer memory reclamation for high-throughput spatial indexing and multi-core parallel geometric range querying execution in real-time geographic information systems and concurrent spatial database indexing engines`
- `Implementation of a lock-free thread-safe concurrent Merkle Patricia Trie using atomic branch-node-updating and leaf-path-splicing CAS primitives alongside hazard pointer memory reclamation for high-throughput cryptographic state verification and multi-core parallel blockchain world-state querying execution in real-time decentralized ledger storage systems and concurrent Ethereum-compatible smart contract execution engines`
- `Implementation of a lock-free thread-safe concurrent Bx-Tree using atomic leaf-merging and path-compression CAS primitives alongside hazard pointer memory reclamation for high-throughput multi-core concurrent multidimensional indexing execution in real-time enterprise database engines and concurrent geospatial querying platforms`
- `Implementation of a lock-free thread-safe concurrent Bounded Queue using atomic head-tail-advancing and ring-buffer-wrapping CAS primitives alongside hazard pointer memory reclamation for high-throughput single-producer-multi-consumer messaging and multi-core parallel task dispatch execution in real-time asynchronous event-driven server engines and concurrent log aggregation platforms`

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
