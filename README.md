# 🧠 Gemini Coding Brain

> An autonomous AI agent that learns coding concepts every day using the Gemini API,
> commits its growing knowledge base to GitHub automatically, and builds a fine-tuning
> dataset for future offline model training.

<!-- STATS_START -->
## 📊 Live Stats

| Metric | Value |
|---|---|
| Total Topics Learned | **2658** |
| Last Updated | `2026-10-09T21:43:57.024081+00:00` |
| Dataset Size | `2658 entries` |

## 📂 Categories Learned

| Category | Topics |
|---|---|
| data-structures | 1606 |
| trading-strategies | 228 |
| technical-analysis | 147 |
| crypto-blockchain | 137 |
| algorithms | 129 |
| market-analysis | 114 |
| system-design | 84 |
| stocks-markets | 71 |
| databases | 36 |
| probability-math | 27 |
| security | 23 |
| machine-learning | 15 |
| networking | 13 |
| web-dev | 9 |
| language-specific | 7 |
| devops | 7 |
| best-practices | 2 |
| data-visualization | 2 |
| testing | 1 |

## 🕐 Last 5 Topics Learned

- `Implementation of a lock-free thread-safe concurrent Aho-Corasick automaton using atomic failure-link-setting and transition-table-expanding CAS primitives alongside hazard pointer memory reclamation for high-throughput multi-pattern string matching and multi-core keyword searching in real-time network intrusion detection systems and concurrent log filtering platforms`
- `Implementation of a lock-free thread-safe concurrent Disjoint-Set (Union-Find) data structure using atomic path-halving and rank-combining CAS primitives alongside hazard pointer memory reclamation for high-throughput equivalence class merging and multi-core connected component analysis in real-time social network graph partitioning and concurrent dynamic connectivity systems`
- `Implementation of a lock-free thread-safe concurrent Vantage-Point Tree using atomic metric-space-partitioning and radius-bounding CAS primitives alongside hazard pointer memory reclamation for high-throughput similarity searching and multi-core nearest-neighbor querying in real-time multimedia retrieval systems and concurrent high-dimensional vector databases`
- `Implementation of a lock-free thread-safe concurrent Tries (Prefix Tree) using atomic node-allocating and child-pointer-updating CAS primitives alongside hazard pointer memory reclamation for high-throughput dictionary lookups and multi-core prefix matching in real-time autocomplete search engines and concurrent routing table lookup systems`
- `Implementation of a lock-free thread-safe concurrent Suffix Tree using atomic node-splitting and suffix-link-updating CAS primitives alongside hazard pointer memory reclamation for high-throughput exact string matching and multi-core pattern searching in real-time cybersecurity intrusion detection systems and concurrent malware analysis engines`

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
