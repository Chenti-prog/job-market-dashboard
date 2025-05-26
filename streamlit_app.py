# streamlit_app.py

import streamlit as st
import pandas as pd
from pymongo import MongoClient
import matplotlib.pyplot as plt

# --- Streamlit Config ---
st.set_page_config(page_title="Job Market Dashboard", layout="wide")
st.title("📊 Interactive Job Market Dashboard")

# --- MongoDB Connection ---
# MONGO_URI = st.secrets["mongo"]["uri"]
# client = MongoClient(MONGO_URI)
# db = client["job_dashboard"]
# collection = db["jobs"]

try:
    MONGO_URI = st.secrets["mongo"]["uri"]
    client = MongoClient(MONGO_URI, serverSelectionTimeoutMS=5000)
    db = client["job_dashboard"]
    collection = db["jobs"]
    client.server_info()  # 🔍 Force connection to test
except Exception as e:
    st.error(f"❌ MongoDB Connection Error: {e}")
    st.stop()

# --- Load Data ---
data = list(collection.find({}, {"_id": 0}))
df = pd.DataFrame(data)

if df.empty:
    st.error("❌ No job data found in MongoDB.")
    st.stop()

# --- Sidebar Filters ---
st.sidebar.header("🔍 Filter Options")

# Region filter
region_options = ["All"] + sorted(df["region"].dropna().unique().tolist())
selected_region = st.sidebar.selectbox("Select Region", region_options)

# Job type filter
job_type_options = ["All"] + sorted(df["onsite_remote"].dropna().str.lower().unique().tolist())
selected_job_type = st.sidebar.selectbox("Select Job Type", job_type_options)

# --- Apply Filtering Logic ---
filtered_df = df.copy()

if selected_region != "All":
    filtered_df = filtered_df[filtered_df["region"] == selected_region]

if selected_job_type != "All":
    filtered_df = filtered_df[
        filtered_df["onsite_remote"].str.lower() == selected_job_type.lower()
    ]

# --- Main Output ---
st.write(f"### {len(filtered_df)} job listings found")
st.dataframe(filtered_df)

# --- Chart 1: Top Job Titles ---
# if not filtered_df.empty:
#     top_titles = filtered_df["title"].value_counts().head(10)
#     fig1, ax1 = plt.subplots()
#     top_titles.plot(kind='bar', ax=ax1, color='skyblue')
#     ax1.set_title("Top 10 Job Titles")
#     ax1.set_xlabel("Count")
#     ax1.invert_yaxis()
#     st.pyplot(fig1)
if "title" in filtered_df.columns and not filtered_df["title"].isna().all():
    top_titles = filtered_df["title"].value_counts().head(10)
    fig1, ax1 = plt.subplots()
    top_titles.plot(kind='barh', ax=ax1, color='skyblue')
    ax1.set_title("Top 10 Job Titles")
    ax1.set_xlabel("Count")
    ax1.invert_yaxis()
    st.pyplot(fig1)

    # --- Chart 2: Region Breakdown ---
    # region_counts = filtered_df["region"].value_counts()
    # fig2, ax2 = plt.subplots()
    # region_counts.plot(kind='bar', ax=ax2, color='coral')
    # ax2.set_title("Job Listings by Region")
    # ax2.set_ylabel("Count")
    # st.pyplot(fig2)
   
    region_counts = filtered_df["region"].value_counts()
    fig2, ax2 = plt.subplots()
    region_counts.plot(kind='bar', ax=ax2, color='coral')
    ax2.set_title("Job Listings by Region")
    ax2.set_ylabel("Count")
    ax2.tick_params(axis='x', rotation=45)
    fig2.tight_layout()
    st.pyplot(fig2)

    # --- Chart 3: Remote vs Onsite ---
    # job_mode = filtered_df["onsite_remote"].str.lower().value_counts()
    # fig3, ax3 = plt.subplots()
    # ax3.pie(job_mode, labels=job_mode.index, autopct="%1.1f%%", startangle=140)
    # ax3.set_title("Remote vs Onsite Job Distribution")
    # ax3.axis("equal")
    # st.pyplot(fig3)

    job_mode = filtered_df["onsite_remote"].dropna().str.lower().value_counts()
    fig3, ax3 = plt.subplots()
    ax3.pie(job_mode, labels=job_mode.index, autopct="%1.1f%%", startangle=140)
    ax3.set_title("Remote vs Onsite Job Distribution")
    ax3.axis("equal")
    st.pyplot(fig3)
else:
    st.warning("No results match the selected filters.")

