# 🧠 Gemini Coding Brain

> An autonomous AI agent that learns coding concepts every day using the Gemini API,
> commits its growing knowledge base to GitHub automatically, and builds a fine-tuning
> dataset for future offline model training.

<!-- STATS_START -->
## 📊 Live Stats

| Metric | Value |
|---|---|
| Total Topics Learned | **1445** |
| Last Updated | `2026-09-21T23:09:06.892405+00:00` |
| Dataset Size | `1445 entries` |

## 📂 Categories Learned

| Category | Topics |
|---|---|
| data-structures | 547 |
| trading-strategies | 228 |
| technical-analysis | 147 |
| market-analysis | 114 |
| crypto-blockchain | 98 |
| system-design | 83 |
| stocks-markets | 71 |
| algorithms | 43 |
| probability-math | 27 |
| databases | 24 |
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

- `Implementation of a lock-free thread-safe concurrent Labeled Directed Graph using atomic vertex-insertion and edge-CAS primitives alongside hazard pointer memory reclamation for high-throughput relationship querying and multi-core traversal evaluation in real-time social network and recommendation engine systems`
- `Implementation of a lock-free thread-safe concurrent CRDT (Conflict-Free Replicated Data Type) Observed-Removed Set using atomic state-tombstoning and causal-context merging CAS primitives alongside epoch-based memory reclamation for high-throughput distributed state convergence and multi-core conflict resolution in real-time collaborative editing engines`
- `Implementation of a lock-free thread-safe concurrent Vector Clock engine using atomic vector-timestamp merging and causal-dependency tracking CAS primitives alongside epoch-based memory reclamation for high-throughput distributed event ordering and multi-core version vector reconciliation in real-time distributed database synchronization engines`
- `Implementation of a lock-free thread-safe concurrent SimHash engine using atomic bitwise-hamming distance comparison and centroid-clustering CAS primitives alongside hazard pointer memory reclamation for high-throughput near-duplicate document detection and multi-core web crawling in real-time search engine indexers`
- `Implementation of a lock-free thread-safe concurrent Merkle Patricia Tree using atomic branch-node linking and path-extension CAS primitives alongside hazard pointer memory reclamation for high-throughput cryptographic state verification and multi-core account trie management in real-time blockchain execution engines`

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
