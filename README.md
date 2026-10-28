# 🧠 Gemini Coding Brain

> An autonomous AI agent that learns coding concepts every day using the Gemini API,
> commits its growing knowledge base to GitHub automatically, and builds a fine-tuning
> dataset for future offline model training.

<!-- STATS_START -->
## 📊 Live Stats

| Metric | Value |
|---|---|
| Total Topics Learned | **4095** |
| Last Updated | `2026-10-28T19:30:27.061525+00:00` |
| Dataset Size | `4095 entries` |

## 📂 Categories Learned

| Category | Topics |
|---|---|
| data-structures | 2816 |
| algorithms | 248 |
| trading-strategies | 228 |
| crypto-blockchain | 178 |
| technical-analysis | 147 |
| system-design | 120 |
| market-analysis | 114 |
| stocks-markets | 71 |
| databases | 45 |
| security | 34 |
| probability-math | 27 |
| networking | 21 |
| machine-learning | 18 |
| web-dev | 9 |
| language-specific | 7 |
| devops | 7 |
| best-practices | 2 |
| data-visualization | 2 |
| testing | 1 |

## 🕐 Last 5 Topics Learned

- `Implementation of a lock-free thread-safe concurrent Skip Graph using atomic pointer-routing and peer-node-linking CAS primitives alongside hazard pointer memory reclamation for high-throughput distributed peer-to-peer lookups and multi-core parallel decentralized routing in real-time content delivery networks and concurrent distributed file sharing systems`
- `Implementation of a lock-free thread-safe concurrent B-tree using atomic node-splitting and structural-merging CAS primitives alongside hazard pointer memory reclamation for high-throughput disk-backed indexing and multi-core parallel range queries in real-time relational database management systems and concurrent storage engines`
- `Implementation of a lock-free thread-safe concurrent Radix Tree using atomic child-node-allocation and prefix-compression CAS primitives alongside hazard pointer memory reclamation for high-throughput IP routing table lookups and multi-core parallel string key-value storage in real-time software-defined networking platforms and concurrent network routing engines`
- `Implementation of a lock-free thread-safe concurrent Fenwick Tree (Binary Indexed Tree) using atomic prefix-sum-updating and index-masking CAS primitives alongside hazard pointer memory reclamation for high-throughput cumulative frequency queries and multi-core parallel point update operations in real-time streaming analytics platforms and concurrent leaderboard ranking engines`
- `Implementation of a lock-free thread-safe concurrent Bounding Volume Hierarchy (BVH) using atomic child-node-swapping and ray-box-intersection CAS primitives alongside hazard pointer memory reclamation for high-throughput ray tracing and multi-core parallel collision detection in real-time computer graphics rendering engines and concurrent physics simulation platforms`

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
