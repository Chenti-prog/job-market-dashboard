# 📊 Job Market Data Analysis Dashboard

An end-to-end data analysis and visualization project using real-world job listings from the US, Canada, and Africa. This project demonstrates the use of **PostgreSQL**, **pandas**, **matplotlib**, and **Streamlit** to analyze, visualize, and interact with job market data.

---

## ✅ Project Goals

* Clean and combine job listing datasets from multiple regions
* Store and query data efficiently using PostgreSQL
* Analyze trends by region, role, and job type
* Build visual summaries using Python
* Deliver insights through an interactive Streamlit dashboard

---

## 🧱 Tech Stack

* **Python** (pandas, matplotlib, SQLAlchemy)
* **PostgreSQL** (local database)
* **Streamlit** (dashboard UI)
* **Jupyter** (exploratory notebooks)

---

## 🗂️ Project Structure

```
JobMarketDash/
├── data/
│   ├── raw/                # Original CSVs (US, Canada, Africa)
│   └── processed/          # Combined and cleaned data
├── db/
│   └── schema.sql          # Table schema for PostgreSQL
├── scripts/
│   ├── combine_data.py
│   ├── load_to_postgres.py
│   ├── query_and_plot.py
│   └── region_mode_charts.py
├── notebooks/
│   └── job_insights.ipynb  # Exploratory analysis and findings
├── output/                 # Saved charts and summary
├── streamlit_app.py        # 📈 Interactive dashboard
├── requirements.txt        # Python dependencies
├── .gitignore
└── README.md
```

---

## 🚀 How to Run This Project

### 1. Clone the Repo and Set Up Virtual Environment

```bash
git clone https://github.com/your-username/JobMarketDash.git
cd JobMarketDash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 2. Set Up PostgreSQL

```bash
createdb job_explorer
psql -U <your_username> -d job_explorer -f db/schema.sql
```

### 3. Load and Process Data

```bash
python scripts/combine_data.py
python scripts/load_to_postgres.py
```

### 4. Generate Visuals

```bash
python scripts/query_and_plot.py
python scripts/region_mode_charts.py
```

### 5. Run Dashboard

```bash
streamlit run streamlit_app.py
```

---

## 📊 Key Insights

* **Top Job Titles** vary by region but "Data Analyst" dominates overall
* **Remote work** is most common in US listings
* **Africa** shows a growing share of hybrid opportunities

---

## 📌 Future Improvements

* Add authentication for user-specific dashboards
* Include salary normalization and histogram analysis
* Connect live job APIs for continuous updates

---

## 📬 Contact

Made with ❤️ by \[Your Name]
\[Your LinkedIn] | \[Your GitHub] | \[Your Portfolio]

---

> *This project is intended as a portfolio showcase for data analysis, SQL, and dashboard development using open tools and real-world data.*

