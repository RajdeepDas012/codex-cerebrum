# 🧠 Gemini Coding Brain

> An autonomous AI agent that learns coding concepts every day using the Gemini API,
> commits its growing knowledge base to GitHub automatically, and builds a fine-tuning
> dataset for future offline model training.

<!-- STATS_START -->
## 📊 Live Stats

| Metric | Value |
|---|---|
| Total Topics Learned | **2166** |
| Last Updated | `2026-10-02T05:18:39.207257+00:00` |
| Dataset Size | `2166 entries` |

## 📂 Categories Learned

| Category | Topics |
|---|---|
| data-structures | 1173 |
| trading-strategies | 228 |
| technical-analysis | 147 |
| crypto-blockchain | 121 |
| market-analysis | 114 |
| algorithms | 98 |
| system-design | 83 |
| stocks-markets | 71 |
| databases | 33 |
| probability-math | 27 |
| security | 18 |
| machine-learning | 14 |
| networking | 12 |
| web-dev | 9 |
| language-specific | 7 |
| devops | 7 |
| data-visualization | 2 |
| best-practices | 1 |
| testing | 1 |

## 🕐 Last 5 Topics Learned

- `Implementation of a lock-free thread-safe concurrent Cuckoo Filter using atomic bucket-kicking and fingerprint-relocation CAS primitives alongside hazard pointer memory reclamation for high-throughput space-efficient approximate membership testing and multi-core high-speed item deletion in real-time distributed storage systems and concurrent database caching layers`
- `Implementation of a lock-free thread-safe concurrent SimHash index using atomic bit-distance-calculation and fingerprint-clustering CAS primitives alongside hazard pointer memory reclamation for high-throughput near-duplicate document detection and multi-core web crawling deduplication in real-time search engine ingestion pipelines and concurrent plagiarism checking systems`
- `Implementation of a lock-free thread-safe concurrent Bloom-Lookup (Cuckoo-Hashing) Hybrid Index using atomic bucket-relocation and fingerprint-stamping CAS primitives alongside hazard pointer memory reclamation for high-throughput memory-mapped data ingestion and multi-core high-speed record validation in real-time fraud detection systems and concurrent security audit logging pipelines`
- `Implementation of a lock-free thread-safe concurrent Count-Min Sketch using atomic frequency-cell-incrementing and hash-bucket-updating CAS primitives alongside hazard pointer memory reclamation for high-throughput heavy hitters stream processing and multi-core frequency estimation in real-time network traffic monitoring systems and concurrent stream analytics engines`
- `Implementation of a lock-free thread-safe concurrent Skip Graph using atomic peer-pointer-routing and randomized-membership-vector CAS primitives alongside hazard pointer memory reclamation for high-throughput distributed peer-to-peer searching and multi-core decentralized key lookup in real-time distributed hash tables and concurrent cloud storage systems`

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
