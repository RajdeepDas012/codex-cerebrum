# 🧠 Gemini Coding Brain

> An autonomous AI agent that learns coding concepts every day using the Gemini API,
> commits its growing knowledge base to GitHub automatically, and builds a fine-tuning
> dataset for future offline model training.

<!-- STATS_START -->
## 📊 Live Stats

| Metric | Value |
|---|---|
| Total Topics Learned | **4330** |
| Last Updated | `2026-11-01T13:28:23.947855+00:00` |
| Dataset Size | `4330 entries` |

## 📂 Categories Learned

| Category | Topics |
|---|---|
| data-structures | 3031 |
| algorithms | 256 |
| trading-strategies | 228 |
| crypto-blockchain | 184 |
| technical-analysis | 147 |
| system-design | 120 |
| market-analysis | 114 |
| stocks-markets | 71 |
| databases | 48 |
| security | 36 |
| probability-math | 27 |
| networking | 21 |
| machine-learning | 19 |
| web-dev | 9 |
| language-specific | 7 |
| devops | 7 |
| best-practices | 2 |
| data-visualization | 2 |
| testing | 1 |

## 🕐 Last 5 Topics Learned

- `Implementation of a lock-free thread-safe concurrent Suffix Automaton using atomic state-transition-linking and node-cloning CAS primitives alongside hazard pointer memory reclamation for high-throughput compressed substring indexing and multi-core parallel pattern matching execution in real-time string processing systems and concurrent genomic analysis engines`
- `Implementation of a lock-free thread-safe concurrent R-Tree using atomic bounding-box-merging and node-splitting CAS primitives alongside hazard pointer memory reclamation for high-throughput spatial indexing and multi-core parallel range-query execution in real-time geographic information systems and concurrent spatial database engines`
- `Implementation of a lock-free thread-safe concurrent Fibonacci Heap using atomic root-list-splicing and decrease-key CAS primitives alongside hazard pointer memory reclamation for high-throughput amortized graph algorithm operations and multi-core parallel shortest path execution in real-time network routing engines and concurrent graph processing systems`
- `Implementation of a lock-free thread-safe concurrent B+ Tree using atomic leaf-sibling-linking and node-splitting CAS primitives alongside hazard pointer memory reclamation for high-throughput ranged indexing and multi-core parallel range-scan execution in real-time transactional database systems and concurrent storage engines`
- `Implementation of a lock-free thread-safe concurrent BK-Tree using atomic edit-distance-calculating and node-branch-swapping CAS primitives alongside hazard pointer memory reclamation for high-throughput fuzzy string matching and multi-core parallel spell-checking execution in real-time auto-complete systems and concurrent dictionary search engines`

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
