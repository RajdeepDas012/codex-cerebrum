# 🧠 Gemini Coding Brain

> An autonomous AI agent that learns coding concepts every day using the Gemini API,
> commits its growing knowledge base to GitHub automatically, and builds a fine-tuning
> dataset for future offline model training.

<!-- STATS_START -->
## 📊 Live Stats

| Metric | Value |
|---|---|
| Total Topics Learned | **2847** |
| Last Updated | `2026-10-12T19:32:14.855631+00:00` |
| Dataset Size | `2847 entries` |

## 📂 Categories Learned

| Category | Topics |
|---|---|
| data-structures | 1760 |
| trading-strategies | 228 |
| algorithms | 151 |
| technical-analysis | 147 |
| crypto-blockchain | 143 |
| market-analysis | 114 |
| system-design | 84 |
| stocks-markets | 71 |
| databases | 38 |
| probability-math | 27 |
| security | 24 |
| machine-learning | 16 |
| networking | 16 |
| web-dev | 9 |
| language-specific | 7 |
| devops | 7 |
| best-practices | 2 |
| data-visualization | 2 |
| testing | 1 |

## 🕐 Last 5 Topics Learned

- `Implementation of a lock-free thread-safe concurrent Merkle Patricia Trie using atomic branch-node-updating and cryptographic-hash-linking CAS primitives alongside hazard pointer memory reclamation for high-throughput state verification and multi-core account management in real-time blockchain execution engines and concurrent distributed ledger databases`
- `Implementation of a lock-free thread-safe concurrent Bloom Filter using atomic bit-setting and word-cascading CAS primitives alongside hazard pointer memory reclamation for high-throughput approximate membership testing and multi-core distributed caching in real-time key-value storage engines and concurrent database systems`
- `Implementation of a lock-free thread-safe concurrent Skip Graph using atomic pointer-routing and peer-membership-updating CAS primitives alongside hazard pointer memory reclamation for high-throughput decentralized distributed routing and multi-core overlay network lookup in real-time peer-to-peer distributed systems and concurrent cloud storage architectures`
- `Implementation of a lock-free thread-safe concurrent Interval Tree using atomic node-overlapping and endpoint-updating CAS primitives alongside hazard pointer memory reclamation for high-throughput time-interval querying and multi-core schedule overlap detection in real-time calendar management platforms and concurrent event-scheduling engines`
- `Implementation of a lock-free thread-safe concurrent Disjoint Set (Union-Find) using atomic parent-pointer-compressing and rank-bounding CAS primitives alongside hazard pointer memory reclamation for high-throughput connected components analysis and multi-core equivalence relation tracking in real-time graph processing platforms and concurrent network topology engines`

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
