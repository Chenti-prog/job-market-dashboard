# scripts/load_to_mongo.py

import pandas as pd
from pymongo import MongoClient

# MongoDB connection string from Atlas (update your username/password/cluster)
MONGO_URI = "mongodb+srv://chentiyakub:ZZsz4AAdyroG4AyT@potential0.vwabawn.mongodb.net/?%0AretryWrites=true&w=majority&appName=Potential0"

# Connect to MongoDB
client = MongoClient(MONGO_URI)
db = client["job_dashboard"]           # Database name
collection = db["jobs"]                # Collection name

# Load the CSV
df = pd.read_csv("data/processed/all_jobs.csv")

# Convert DataFrame rows to dictionaries and insert into MongoDB
records = df.to_dict(orient="records")
collection.delete_many({})             # Optional: clear previous entries
collection.insert_many(records)

print(f"✅ Loaded {len(records)} records into MongoDB collection 'jobs'")

