# 🧠 Gemini Coding Brain

> An autonomous AI agent that learns coding concepts every day using the Gemini API,
> commits its growing knowledge base to GitHub automatically, and builds a fine-tuning
> dataset for future offline model training.

<!-- STATS_START -->
## 📊 Live Stats

| Metric | Value |
|---|---|
| Total Topics Learned | **1661** |
| Last Updated | `2026-09-24T22:15:30.219231+00:00` |
| Dataset Size | `1661 entries` |

## 📂 Categories Learned

| Category | Topics |
|---|---|
| data-structures | 740 |
| trading-strategies | 228 |
| technical-analysis | 147 |
| market-analysis | 114 |
| crypto-blockchain | 105 |
| system-design | 83 |
| stocks-markets | 71 |
| algorithms | 53 |
| databases | 28 |
| probability-math | 27 |
| security | 15 |
| networking | 12 |
| machine-learning | 11 |
| web-dev | 9 |
| language-specific | 7 |
| devops | 7 |
| data-visualization | 2 |
| best-practices | 1 |
| testing | 1 |

## 🕐 Last 5 Topics Learned

- `Implementation of a lock-free thread-safe concurrent Blocking Queue using atomic node-linking and condition-variable-signaling CAS primitives alongside hazard pointer memory reclamation for high-throughput producer-consumer task coordination and multi-core thread synchronization in real-time enterprise messaging systems and asynchronous task execution runtimes`
- `Implementation of a lock-free thread-safe concurrent Lock-Free Ring Buffer using atomic head-tail-advancing and sequence-number-validating CAS primitives alongside hazard pointer memory reclamation for high-throughput single-producer multi-consumer message passing and multi-core inter-thread communication in real-time low-latency trading systems and high-performance actor runtimes`
- `Implementation of a lock-free thread-safe concurrent Priority Queue using atomic heap-node-promoting and batched-enqueue-CAS primitives alongside hazard pointer memory reclamation for high-throughput asynchronous task scheduling and multi-core work-stealing execution in real-time distributed thread pool engines and high-performance computing schedulers`
- `Implementation of a lock-free thread-safe concurrent Suffix Automaton using atomic state-transition-linking and string-extension CAS primitives alongside hazard pointer memory reclamation for high-throughput substring matching and multi-core text indexing in real-time string processing and information retrieval engines`
- `Implementation of a lock-free thread-safe concurrent Cuckoo Filter using atomic bucket-kicking and fingerprint-swapping CAS primitives alongside hazard pointer memory reclamation for high-throughput space-efficient dynamic set membership verification and multi-core duplicate removal in real-time distributed storage systems and high-frequency network packet inspection engines`

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
