# 🧠 Gemini Coding Brain

> An autonomous AI agent that learns coding concepts every day using the Gemini API,
> commits its growing knowledge base to GitHub automatically, and builds a fine-tuning
> dataset for future offline model training.

<!-- STATS_START -->
## 📊 Live Stats

| Metric | Value |
|---|---|
| Total Topics Learned | **1936** |
| Last Updated | `2026-09-28T01:17:35.040859+00:00` |
| Dataset Size | `1936 entries` |

## 📂 Categories Learned

| Category | Topics |
|---|---|
| data-structures | 972 |
| trading-strategies | 228 |
| technical-analysis | 147 |
| market-analysis | 114 |
| crypto-blockchain | 114 |
| system-design | 83 |
| algorithms | 81 |
| stocks-markets | 71 |
| databases | 31 |
| probability-math | 27 |
| security | 17 |
| machine-learning | 12 |
| networking | 12 |
| web-dev | 9 |
| language-specific | 7 |
| devops | 7 |
| data-visualization | 2 |
| best-practices | 1 |
| testing | 1 |

## 🕐 Last 5 Topics Learned

- `Implementation of a lock-free thread-safe concurrent Quotient Filter using atomic metadata-shifting and quotient-probing CAS primitives alongside hazard pointer memory reclamation for high-throughput space-efficient approximate membership testing and multi-core dynamic resizing in real-time distributed storage systems and concurrent network packet filtering engines`
- `Implementation of a lock-free thread-safe concurrent LFU (Least Frequently Used) Cache using atomic frequency-list-splicing and min-frequency-tracking CAS primitives alongside hazard pointer memory reclamation for high-throughput cache eviction and multi-core data access in real-time in-memory database systems and concurrent web application caching layers`
- `Implementation of a lock-free thread-safe concurrent LSA (Latent Semantic Analysis) matrix factorization engine using atomic singular-value-updating and document-term-weighting CAS primitives alongside hazard pointer memory reclamation for high-throughput semantic text clustering and multi-core vector space modeling in real-time document search engines and concurrent natural language processing pipelines`
- `Implementation of a lock-free thread-safe concurrent Merkle Mountain Range using atomic peak-appending and proof-verification CAS primitives alongside hazard pointer memory reclamation for high-throughput append-only cryptographic commitment history and multi-core accumulator proofs in real-time blockchain timestamping engines and concurrent verifiable log systems`
- `Implementation of a lock-free thread-safe concurrent BFD (Best-Fit Decreasing) bin packing allocator using atomic capacity-tracking and fragment-merging CAS primitives alongside hazard pointer memory reclamation for high-throughput memory resource allocation and multi-core bin compaction in real-time cloud infrastructure resource schedulers and concurrent systems memory management engines`

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
