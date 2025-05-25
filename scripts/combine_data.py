import pandas as pd

# Load all three datasets
us_df = pd.read_csv("data/raw/linkedin-jobs-usa.csv")
canada_df = pd.read_csv("data/raw/linkedin-jobs-canada.csv")
africa_df = pd.read_csv("data/raw/linkedin-jobs-africa.csv")

# Add region labels
us_df["region"] = "US"
canada_df["region"] = "Canada"
africa_df["region"] = "Africa"

# Combine them
combined_df = pd.concat([us_df, canada_df, africa_df], ignore_index=True)

# Save to processed folder
combined_df.to_csv("data/processed/all_jobs.csv", index=False)

print("✅ Combined dataset saved to data/processed/all_jobs.csv")

