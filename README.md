# 🧠 Gemini Coding Brain

> An autonomous AI agent that learns coding concepts every day using the Gemini API,
> commits its growing knowledge base to GitHub automatically, and builds a fine-tuning
> dataset for future offline model training.

<!-- STATS_START -->
## 📊 Live Stats

| Metric | Value |
|---|---|
| Total Topics Learned | **1902** |
| Last Updated | `2026-09-27T18:43:34.552315+00:00` |
| Dataset Size | `1902 entries` |

## 📂 Categories Learned

| Category | Topics |
|---|---|
| data-structures | 947 |
| trading-strategies | 228 |
| technical-analysis | 147 |
| market-analysis | 114 |
| crypto-blockchain | 112 |
| system-design | 83 |
| algorithms | 75 |
| stocks-markets | 71 |
| databases | 30 |
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

- `Implementation of a lock-free thread-safe concurrent LSA (Latent Semantic Analysis) matrix factorization engine using atomic singular-value-updating and document-vector-projection CAS primitives alongside hazard pointer memory reclamation for high-throughput semantic document similarity searching and multi-core topic modeling in real-time document retrieval engines and concurrent natural language processing pipelines`
- `Implementation of a lock-free thread-safe concurrent Levenshtein Distance matrix calculation engine using atomic cell-relaxation and diagonal-wavefront-scheduling CAS primitives alongside hazard pointer memory reclamation for high-throughput approximate string matching and multi-core sequence alignment in real-time spelling correction applications and concurrent bioinformatics sequence analysis systems`
- `Implementation of a lock-free thread-safe concurrent BK-Tree using atomic edit-distance-calculating and child-node-linking CAS primitives alongside hazard pointer memory reclamation for high-throughput fuzzy string matching and multi-core spell checking in real-time text editing applications and concurrent dictionary search engines`
- `Implementation of a lock-free thread-safe concurrent Skip Graph using atomic peer-routing and neighbor-pointer-updating CAS primitives alongside hazard pointer memory reclamation for high-throughput distributed searching and multi-core decentralized peer-to-peer network routing in real-time distributed overlay networks and concurrent cloud resource discovery engines`
- `Implementation of a lock-free thread-safe concurrent Scs (Shortest Common Supersequence) string alignment algorithm using atomic state-transition and cell-updating CAS primitives alongside hazard pointer memory reclamation for high-throughput genomic data merging and multi-core sequence assembly in real-time bioinformatics analysis pipelines and concurrent text processing engines`

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
