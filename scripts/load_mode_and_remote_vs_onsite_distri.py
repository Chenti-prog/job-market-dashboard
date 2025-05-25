# scripts/region_mode_charts.py

import pandas as pd
import matplotlib.pyplot as plt
from sqlalchemy import create_engine

# === PostgreSQL connection setup ===
engine = create_engine("postgresql+psycopg2://chenti:@localhost:5432/job_explorer")

# === Chart 1: Job Listings by Region ===
query_region = """
SELECT region, COUNT(*) as count
FROM jobs
GROUP BY region
ORDER BY count DESC;
"""

region_df = pd.read_sql(query_region, engine)

plt.figure(figsize=(6, 4))
plt.bar(region_df['region'], region_df['count'], color='coral')
plt.title("Job Listings by Region")
plt.xlabel("Region")
plt.ylabel("Number of Listings")
plt.tight_layout()
plt.savefig("output/jobs_by_region.png")
print("✅ Chart saved to output/jobs_by_region.png")

# === Chart 2: Remote vs Onsite Job Distribution ===
query_mode = """
SELECT LOWER(onsite_remote) AS job_type, COUNT(*) as count
FROM jobs
GROUP BY job_type
ORDER BY count DESC;
"""

mode_df = pd.read_sql(query_mode, engine)

plt.figure(figsize=(6, 4))
plt.pie(mode_df['count'], labels=mode_df['job_type'], autopct='%1.1f%%', startangle=140)
plt.title("Remote vs Onsite Job Distribution")
plt.axis('equal')
plt.tight_layout()
plt.savefig("output/job_mode_pie.png")
print("✅ Chart saved to output/job_mode_pie.png")

