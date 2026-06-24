# Job Market Intelligence Platform

An end-to-end data analytics platform analyzing 123,842 LinkedIn job postings to uncover skill demand, salary trends, and geographic opportunities.

**Live Dashboard:** https://job-market-intelligence-kaif.streamlit.app/

## Key Findings
- **Excel dominates** with 18,107 job postings — 3.5x more than Python or SQL
- **Python + SQL** is the most common skill combination, appearing in 1,978 jobs together
- **Deep Learning skills** command the highest salaries at $185K average
- **San Francisco Bay Area** leads in salary at $160K despite lower job volume than New York
- Only **29% of job postings** disclose salary — all salary analysis reflects this limitation

## Tech Stack
| Layer | Tool | Why |
|-------|------|-----|
| Data Processing | Python + Pandas | ETL pipeline |
| Analytics | DuckDB + SQL | In-process analytics on parquet files |
| Storage | Apache Parquet | Columnar format, fast analytical queries |
| Dashboard | Streamlit + Plotly | Python-native, free deployment |
| Deployment | Streamlit Community Cloud | Zero DevOps, GitHub integration |

## Architecture
Raw CSV (123K rows)

↓

raw_loader.py     → Load CSV, select 12 columns, validate schema

↓

cleaner.py        → Drop nulls, remove duplicates, fix timestamps

↓

salary_parser.py  → Convert to numeric, filter unrealistic values

↓

skill_extractor.py → Keyword matching against 50+ skill taxonomy

↓

Parquet Files     → jobs.parquet + skills.parquet

↓

DuckDB SQL        → 4 analytical queries

↓

Streamlit Dashboard → 4 interactive pages

## Data Model

Two parquet files forming a simple star schema:

- **jobs.parquet** — one row per job posting (40K rows in deployed version, 123K full dataset)
- **skills.parquet** — one row per skill per job (bridge table, ~63K rows)

Connected by `job_id`. This enables skill frequency, salary analysis, and co-occurrence queries.

## ETL Pipeline

| Module | Job | Key Decision |
|--------|-----|--------------|
| `raw_loader.py` | Load CSV, select columns | Load as `dtype=str` to prevent silent type coercion |
| `cleaner.py` | Drop nulls, dedup, fix dates | Use `errors='coerce'` — bad values become null, not crashes |
| `salary_parser.py` | Normalize salary | Filter <$10K and >$1M as data errors |
| `skill_extractor.py` | Extract skills from descriptions | Regex with `\b` word boundaries — prevents 'R' matching 'requirements' |

## Data Quality Notes

- 71% of job postings have no salary data — salary analysis reflects disclosed compensation only
- 'Go' keyword removed from skill taxonomy — matched false positives like "go-getter" in non-tech roles
- Dataset is US-centric — geographic analysis reflects US job market
- Deployed version uses 40K row sample — full 123K dataset runs locally

## How to Run Locally

```bash
# Clone the repo
git clone https://github.com/kaif-adil/job-market-intelligence.git
cd job-market-intelligence

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Download dataset from Kaggle
# https://www.kaggle.com/datasets/arshkon/linkedin-job-postings
# Place postings.csv in data/raw/

# Run ETL pipeline
python run_etl.py

# Launch dashboard
streamlit run app/app.py
```

## Dataset
LinkedIn Job Postings 2023–2024 via Kaggle (CC0 License)
123,842 job postings across 31 columns including title, company, location, salary, and description.