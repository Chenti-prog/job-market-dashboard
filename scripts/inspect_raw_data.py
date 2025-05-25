import pandas as pd

# Load raw datasets
us_df = pd.read_csv("/Users/chenti/Documents/JobMarketDash/data/raw/linkedin-jobs-usa.csv")
canada_df = pd.read_csv("/Users/chenti/Documents/JobMarketDash/data/raw/linkedin-jobs-canada.csv")
africa_df = pd.read_csv("/Users/chenti/Documents/JobMarketDash/data/raw/linkedin-jobs-africa.csv")

# Preview shapes and column names
print("🇺🇸 US Dataset Shape:", us_df.shape)
print("Columns:", us_df.columns.tolist())
print("\n🇨🇦 Canada Dataset Shape:", canada_df.shape)
print("Columns:", canada_df.columns.tolist())
print("\n🌍 Africa Dataset Shape:", africa_df.shape)
print("Columns:", africa_df.columns.tolist())

