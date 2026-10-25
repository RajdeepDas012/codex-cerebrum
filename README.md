# 🧠 Gemini Coding Brain

> An autonomous AI agent that learns coding concepts every day using the Gemini API,
> commits its growing knowledge base to GitHub automatically, and builds a fine-tuning
> dataset for future offline model training.

<!-- STATS_START -->
## 📊 Live Stats

| Metric | Value |
|---|---|
| Total Topics Learned | **3847** |
| Last Updated | `2026-10-25T16:11:56.278680+00:00` |
| Dataset Size | `3847 entries` |

## 📂 Categories Learned

| Category | Topics |
|---|---|
| data-structures | 2597 |
| algorithms | 236 |
| trading-strategies | 228 |
| crypto-blockchain | 169 |
| technical-analysis | 147 |
| system-design | 119 |
| market-analysis | 114 |
| stocks-markets | 71 |
| databases | 42 |
| security | 32 |
| probability-math | 27 |
| networking | 20 |
| machine-learning | 17 |
| web-dev | 9 |
| language-specific | 7 |
| devops | 7 |
| best-practices | 2 |
| data-visualization | 2 |
| testing | 1 |

## 🕐 Last 5 Topics Learned

- `Implementation of a lock-free thread-safe concurrent Binomial Heap using atomic root-linking and node-merging CAS primitives alongside hazard pointer memory reclamation for high-throughput mergeable priority queue operations and multi-core parallel event notification in real-time operating systems and concurrent job scheduling engines`
- `Implementation of a lock-free thread-safe concurrent Suffix Array using atomic index-sorting and rank-updating CAS primitives alongside hazard pointer memory reclamation for high-throughput substring indexing and multi-core parallel full-text search in real-time document search engines and concurrent log analytics platforms`
- `Implementation of a lock-free thread-safe concurrent Radix Tree using atomic child-pointer-swapping and node-compressing CAS primitives alongside hazard pointer memory reclamation for high-throughput IP routing table lookups and multi-core parallel longest prefix matching in real-time software-defined networking platforms and concurrent packet forwarding engines`
- `Implementation of a lock-free thread-safe concurrent Disjoint Set Union using atomic rank-merging and path-halving CAS primitives alongside hazard pointer memory reclamation for high-throughput connected component analysis and multi-core parallel equivalence relation tracking in real-time network topology discovery platforms and concurrent graph clustering engines`
- `Implementation of a lock-free thread-safe concurrent B-link Tree using atomic right-link-swinging and high-key-propagating CAS primitives alongside hazard pointer memory reclamation for high-throughput concurrent record locking and multi-core parallel index traversals in real-time enterprise database engines and concurrent transactional storage systems`

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
