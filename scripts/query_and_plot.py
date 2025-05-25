import pandas as pd
import matplotlib.pyplot as plt
from sqlalchemy import create_engine

# PostgreSQL connection
engine = create_engine("postgresql+psycopg2://chenti:@localhost:5432/job_explorer")

# === 1. Query: Top 10 Job Titles ===
query = """
SELECT title, COUNT(*) as count
FROM jobs
GROUP BY title
ORDER BY count DESC
LIMIT 10;
"""

df = pd.read_sql(query, engine)
print(df)

# === 2. Plot the results ===
plt.figure(figsize=(10, 6))
plt.barh(df['title'], df['count'], color='skyblue')
plt.xlabel("Number of Listings")
plt.title("Top 10 Job Titles")
plt.gca().invert_yaxis()
plt.tight_layout()
plt.savefig("output/top_job_titles.png")
print("✅ Chart saved to output/top_job_titles.png")

