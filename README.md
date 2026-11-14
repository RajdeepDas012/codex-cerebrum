# 🧠 Gemini Coding Brain

> An autonomous AI agent that learns coding concepts every day using the Gemini API,
> commits its growing knowledge base to GitHub automatically, and builds a fine-tuning
> dataset for future offline model training.

<!-- STATS_START -->
## 📊 Live Stats

| Metric | Value |
|---|---|
| Total Topics Learned | **4912** |
| Last Updated | `2026-11-14T10:29:02.065305+00:00` |
| Dataset Size | `4912 entries` |

## 📂 Categories Learned

| Category | Topics |
|---|---|
| data-structures | 3535 |
| algorithms | 302 |
| trading-strategies | 228 |
| crypto-blockchain | 203 |
| technical-analysis | 147 |
| system-design | 121 |
| market-analysis | 114 |
| stocks-markets | 71 |
| databases | 51 |
| security | 40 |
| probability-math | 27 |
| networking | 23 |
| machine-learning | 22 |
| web-dev | 9 |
| language-specific | 7 |
| devops | 7 |
| best-practices | 2 |
| data-visualization | 2 |
| testing | 1 |

## 🕐 Last 5 Topics Learned

- `Implementation of a lock-free thread-safe concurrent Merkle Tree using atomic cryptographic-hashing and branch-root-swinging CAS primitives alongside hazard pointer memory reclamation for high-throughput verifiable data integrity proofs and multi-core parallel cryptographic validation execution in real-time blockchain transaction verification engines and concurrent distributed trustless storage systems`
- `Implementation of a lock-free thread-safe concurrent Leftist Heap using atomic null-path-length-updating and heap-merging CAS primitives alongside hazard pointer memory reclamation for high-throughput mergeable priority queue operations and multi-core parallel event scheduling execution in real-time task management systems and concurrent job scheduling engines`
- `Implementation of a lock-free thread-safe concurrent Bloom-Cascading Cache using atomic aging-bucket-shifting and generational-eviction CAS primitives alongside hazard pointer memory reclamation for high-throughput cache replacement and multi-core parallel hit-rate optimization execution in real-time edge caching systems and concurrent in-memory storage layers`
- `Implementation of a lock-free thread-safe concurrent B+ Tree using atomic leaf-linking and node-merging CAS primitives alongside hazard pointer memory reclamation for high-throughput range scans and multi-core parallel sorted record retrieval execution in real-time relational database storage engines and concurrent in-memory indexing platforms`
- `Implementation of a lock-free thread-safe concurrent Bloom Filter using atomic bit-setting and word-masking CAS primitives alongside hazard pointer memory reclamation for high-throughput probabilistic membership testing and multi-core parallel duplicate filtering execution in real-time web crawler engines and concurrent distributed database caching layers`

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
