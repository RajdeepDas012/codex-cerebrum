# 🧠 Gemini Coding Brain

> An autonomous AI agent that learns coding concepts every day using the Gemini API,
> commits its growing knowledge base to GitHub automatically, and builds a fine-tuning
> dataset for future offline model training.

<!-- STATS_START -->
## 📊 Live Stats

| Metric | Value |
|---|---|
| Total Topics Learned | **5156** |
| Last Updated | `2026-11-20T11:20:54.052693+00:00` |
| Dataset Size | `5156 entries` |

## 📂 Categories Learned

| Category | Topics |
|---|---|
| data-structures | 3748 |
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

- `Implementation of a lock-free thread-safe concurrent Skip-Graph using atomic routing-pointer-updating and peer-discovery CAS primitives alongside hazard pointer memory reclamation for high-throughput decentralized range querying and multi-core parallel distributed routing execution in real-time peer-to-peer overlay networks and concurrent decentralized storage systems`
- `Implementation of a lock-free thread-safe concurrent BK-Tree using atomic edit-distance-calculating and metric-ball-partitioning CAS primitives alongside hazard pointer memory reclamation for high-throughput fuzzy string matching and multi-core parallel spelling correction execution in real-time auto-complete recommendation engines and concurrent spell-checking text editor backends`
- `Implementation of a lock-free thread-safe concurrent Merkle Tree using atomic cryptographic-hash-combining and branch-node-updating CAS primitives alongside hazard pointer memory reclamation for high-throughput distributed state verification and multi-core parallel blockchain validation execution in real-time decentralized ledger systems and concurrent verifiable data storage platforms`
- `Implementation of a lock-free thread-safe concurrent Count-Min-Log Sketch using atomic logarithmic-bucket-scaling and saturation-counter-updating CAS primitives alongside hazard pointer memory reclamation for high-throughput space-compressed frequency estimation and multi-core parallel streaming analytics execution in real-time internet-scale telemetry processing pipelines and concurrent distributed network monitoring systems`
- `Implementation of a lock-free thread-safe concurrent HyperLogLog using atomic register-updating and max-val-tracking CAS primitives alongside hazard pointer memory reclamation for high-throughput cardinality estimation and multi-core parallel distinct counting execution in real-time web analytics streaming pipelines and concurrent large-scale database telemetry systems`

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
