# 🧠 Gemini Coding Brain

> An autonomous AI agent that learns coding concepts every day using the Gemini API,
> commits its growing knowledge base to GitHub automatically, and builds a fine-tuning
> dataset for future offline model training.

<!-- STATS_START -->
## 📊 Live Stats

| Metric | Value |
|---|---|
| Total Topics Learned | **2279** |
| Last Updated | `2026-10-03T18:29:50.537200+00:00` |
| Dataset Size | `2279 entries` |

## 📂 Categories Learned

| Category | Topics |
|---|---|
| data-structures | 1273 |
| trading-strategies | 228 |
| technical-analysis | 147 |
| crypto-blockchain | 125 |
| market-analysis | 114 |
| algorithms | 104 |
| system-design | 83 |
| stocks-markets | 71 |
| databases | 34 |
| probability-math | 27 |
| security | 18 |
| machine-learning | 15 |
| networking | 13 |
| web-dev | 9 |
| language-specific | 7 |
| devops | 7 |
| data-visualization | 2 |
| best-practices | 1 |
| testing | 1 |

## 🕐 Last 5 Topics Learned

- `Implementation of a lock-free thread-safe concurrent X-Fast Trie using atomic word-branching and hash-table-indexing CAS primitives alongside hazard pointer memory reclamation for high-throughput integer key lookups and multi-core predecessor searching in real-time IP routing table lookup engines and concurrent packet forwarding systems`
- `Implementation of a lock-free thread-safe concurrent Tries (Prefix Tree) using atomic node-allocation and child-pointer-linking CAS primitives alongside hazard pointer memory reclamation for high-throughput string key-value lookups and multi-core dictionary auto-completion in real-time search engine query suggestion systems and concurrent networking routing tables`
- `Implementation of a lock-free thread-safe concurrent Treap using atomic randomized-priority-balancing and tree-rotation CAS primitives alongside hazard pointer memory reclamation for high-throughput randomized search tree operations and multi-core key-value balancing in real-time in-memory caching systems and concurrent probabilistic database indexing engines`
- `Implementation of a lock-free thread-safe concurrent B2-Tree using atomic leaf-merging and range-locking CAS primitives alongside hazard pointer memory reclamation for high-throughput multi-core database indexing and concurrent low-latency storage engine range scans in real-time enterprise transaction processing systems`
- `Implementation of a lock-free thread-safe concurrent Merkle Tree using atomic cryptographic-hashing and branch-root-updating CAS primitives alongside hazard pointer memory reclamation for high-throughput verifiable state transitions and multi-core cryptographic proof generation in real-time blockchain validation nodes and concurrent distributed consensus engines`

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
