# 🧠 Gemini Coding Brain

> An autonomous AI agent that learns coding concepts every day using the Gemini API,
> commits its growing knowledge base to GitHub automatically, and builds a fine-tuning
> dataset for future offline model training.

<!-- STATS_START -->
## 📊 Live Stats

| Metric | Value |
|---|---|
| Total Topics Learned | **5126** |
| Last Updated | `2026-11-19T21:26:25.762405+00:00` |
| Dataset Size | `5126 entries` |

## 📂 Categories Learned

| Category | Topics |
|---|---|
| data-structures | 3718 |
| algorithms | 322 |
| trading-strategies | 228 |
| crypto-blockchain | 210 |
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

- `Implementation of a lock-free thread-safe concurrent Suffix Automaton using atomic state-splitting and transition-extending CAS primitives alongside hazard pointer memory reclamation for high-throughput sub-word indexing and multi-core parallel sub-string frequency analytics execution in real-time text compression engines and concurrent pattern matching pipelines`
- `Implementation of a lock-free thread-safe concurrent Aho-Corasick automaton using atomic failure-link-navigating and state-transition-updating CAS primitives alongside hazard pointer memory reclamation for high-throughput multi-pattern string matching and multi-core parallel keyword search execution in real-time intrusion detection network security gateways and concurrent log analysis streaming pipelines`
- `Implementation of a lock-free thread-safe concurrent Skip-List using atomic forward-pointer-cascading and tower-height-allocating CAS primitives alongside hazard pointer memory reclamation for high-throughput probabilistic ordered map operations and multi-core parallel key-value scan execution in real-time in-memory caching layers and concurrent transactional database systems`
- `Implementation of a lock-free thread-safe concurrent Suffix Array using atomic index-sorting and LCP-array-constructing CAS primitives alongside hazard pointer memory reclamation for high-throughput substring searching and multi-core parallel pattern matching execution in real-time text mining analytics engines and concurrent bioinformatics sequence alignment systems`
- `Implementation of a lock-free thread-safe concurrent K-d Tree using atomic hyperplane-splitting and bounding-box-adjusting CAS primitives alongside hazard pointer memory reclamation for high-throughput multi-dimensional nearest neighbor searching and multi-core parallel spatial point location execution in real-time robotics perception systems and concurrent geographic database nearest-neighbor queries`

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
