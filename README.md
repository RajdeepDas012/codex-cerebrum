# 🧠 Gemini Coding Brain

> An autonomous AI agent that learns coding concepts every day using the Gemini API,
> commits its growing knowledge base to GitHub automatically, and builds a fine-tuning
> dataset for future offline model training.

<!-- STATS_START -->
## 📊 Live Stats

| Metric | Value |
|---|---|
| Total Topics Learned | **3389** |
| Last Updated | `2026-10-19T20:57:07.015982+00:00` |
| Dataset Size | `3389 entries` |

## 📂 Categories Learned

| Category | Topics |
|---|---|
| data-structures | 2197 |
| trading-strategies | 228 |
| algorithms | 207 |
| crypto-blockchain | 157 |
| technical-analysis | 147 |
| system-design | 114 |
| market-analysis | 114 |
| stocks-markets | 71 |
| databases | 40 |
| security | 27 |
| probability-math | 27 |
| machine-learning | 16 |
| networking | 16 |
| web-dev | 9 |
| language-specific | 7 |
| devops | 7 |
| best-practices | 2 |
| data-visualization | 2 |
| testing | 1 |

## 🕐 Last 5 Topics Learned

- `Implementation of a lock-free thread-safe concurrent SimHash index using atomic fingerprint-bit-masking and similarity-distance-calculating CAS primitives alongside hazard pointer memory reclamation for high-throughput near-duplicate document detection and multi-core parallel web crawling deduplication in real-time search engine pipelines and concurrent content moderation platforms`
- `Implementation of a lock-free thread-safe concurrent Leaky Bucket rate limiter using atomic drop-counter-incrementing and leak-rate-accumulating CAS primitives alongside hazard pointer memory reclamation for high-throughput traffic shaping and multi-core parallel bandwidth enforcement in real-time API gateways and concurrent cloud ingress controllers`
- `Implementation of a lock-free thread-safe concurrent Vantage-Point Tree using atomic metric-space-partitioning and radius-bounding CAS primitives alongside hazard pointer memory reclamation for high-throughput high-dimensional nearest-neighbor searches and multi-core parallel similarity queries in real-time machine learning inference engines and concurrent vector database indexing systems`
- `Implementation of a lock-free thread-safe concurrent Spatial Hashing grid using atomic bucket-chaining and coordinate-quantization CAS primitives alongside hazard pointer memory reclamation for high-throughput broad-phase collision detection and multi-core parallel neighbor searches in real-time particle simulation engines and concurrent game development frameworks`
- `Implementation of a lock-free thread-safe concurrent Disjoint-Set (Union-Find) data structure using atomic path-compression and rank-union CAS primitives alongside hazard pointer memory reclamation for high-throughput connected components finding and multi-core parallel equivalence relation querying in real-time graph processing frameworks and concurrent network connectivity analysis systems`

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
