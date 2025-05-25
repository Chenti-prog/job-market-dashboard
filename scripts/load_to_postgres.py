# load_to_postgres.py

import pandas as pd
from sqlalchemy import create_engine

# === Configuration ===
DB_USER = "chenti"
DB_PASSWORD = ""  # Leave blank if no password
DB_HOST = "localhost"
DB_PORT = "5432"
DB_NAME = "job_explorer"

CSV_PATH = "data/processed/all_jobs.csv"
TABLE_NAME = "jobs"

# === Create connection engine ===
connection_string = f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
engine = create_engine(connection_string)

# === Load CSV ===
print("📥 Reading CSV...")
df = pd.read_csv(CSV_PATH)
print(f"✅ Loaded {len(df)} records from {CSV_PATH}")

# === Insert into PostgreSQL ===
print(f"📤 Inserting into table '{TABLE_NAME}'...")
df.to_sql(TABLE_NAME, engine, if_exists="append", index=False)
print("✅ Data successfully inserted into PostgreSQL.")

