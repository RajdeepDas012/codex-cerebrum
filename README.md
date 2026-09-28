# 🧠 Gemini Coding Brain

> An autonomous AI agent that learns coding concepts every day using the Gemini API,
> commits its growing knowledge base to GitHub automatically, and builds a fine-tuning
> dataset for future offline model training.

<!-- STATS_START -->
## 📊 Live Stats

| Metric | Value |
|---|---|
| Total Topics Learned | **1945** |
| Last Updated | `2026-09-28T07:03:03.025936+00:00` |
| Dataset Size | `1945 entries` |

## 📂 Categories Learned

| Category | Topics |
|---|---|
| data-structures | 979 |
| trading-strategies | 228 |
| technical-analysis | 147 |
| crypto-blockchain | 115 |
| market-analysis | 114 |
| system-design | 83 |
| algorithms | 82 |
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

- `Implementation of a lock-free thread-safe concurrent Aho-Corasick automaton using atomic failure-link-updating and state-transition-linking CAS primitives alongside hazard pointer memory reclamation for high-throughput multi-pattern string matching and multi-core dictionary searching in real-time intrusion detection systems and concurrent network security filtering engines`
- `Implementation of a lock-free thread-safe concurrent Disjoint-Set (Union-Find) data structure using atomic path-compression and rank-linking CAS primitives alongside hazard pointer memory reclamation for high-throughput equivalence class merging and multi-core connected components querying in real-time social network friend suggestion engines and concurrent graph processing frameworks`
- `Implementation of a lock-free thread-safe concurrent Bloom Filter using atomic bit-setting and word-masking CAS primitives alongside hazard pointer memory reclamation for high-throughput approximate membership querying and multi-core duplicate elimination in real-time web crawler URL filtering and concurrent distributed cache routing layers`
- `Implementation of a lock-free thread-safe concurrent Radix Tree using atomic child-pointer-updating and path-compression CAS primitives alongside hazard pointer memory reclamation for high-throughput prefix routing and multi-core IP address lookups in real-time software-defined networking switches and concurrent network packet forwarding engines`
- `Implementation of a lock-free thread-safe concurrent Merkle Patricia Trie using atomic branch-node-updating and state-root-swapping CAS primitives alongside hazard pointer memory reclamation for high-throughput cryptographic state verification and multi-core account trie modifications in real-time blockchain execution clients and concurrent distributed ledger storage engines`

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
