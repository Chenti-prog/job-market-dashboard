# streamlit_app.py

import streamlit as st
import pandas as pd
from sqlalchemy import create_engine
import matplotlib.pyplot as plt

# PostgreSQL connection
engine = create_engine("postgresql+psycopg2://chenti:@localhost:5432/job_explorer")

st.set_page_config(page_title="Job Market Dashboard", layout="wide")
st.title("📊 Interactive Job Market Dashboard")

# --- Sidebar Filters ---
st.sidebar.header("🔍 Filter Options")
region = st.sidebar.selectbox("Select Region", ["All"] + [r[0] for r in engine.execute("SELECT DISTINCT region FROM jobs;")])
job_type = st.sidebar.selectbox("Select Job Type", ["All", "remote", "onsite", "hybrid"])

# --- SQL Query with Filters ---
query = "SELECT * FROM jobs"
conditions = []
if region != "All":
    conditions.append(f"region = '{region}'")
if job_type != "All":
    conditions.append(f"LOWER(onsite_remote) = '{job_type}'")
if conditions:
    query += " WHERE " + " AND ".join(conditions)

# --- Load Data ---
df = pd.read_sql(query, engine)
st.write(f"### {len(df)} job listings found")
st.dataframe(df)

# --- Chart 1: Top Job Titles ---
top_titles = df['title'].value_counts().head(10)
fig1, ax1 = plt.subplots()
top_titles.plot(kind='barh', ax=ax1, color='skyblue')
ax1.set_title("Top 10 Job Titles")
ax1.set_xlabel("Count")
ax1.invert_yaxis()
st.pyplot(fig1)

# --- Chart 2: Region Breakdown ---
region_counts = df['region'].value_counts()
fig2, ax2 = plt.subplots()
region_counts.plot(kind='bar', ax=ax2, color='coral')
ax2.set_title("Job Listings by Region")
ax2.set_ylabel("Count")
st.pyplot(fig2)

# --- Chart 3: Remote vs Onsite ---
job_mode = df['onsite_remote'].str.lower().value_counts()
fig3, ax3 = plt.subplots()
ax3.pie(job_mode, labels=job_mode.index, autopct="%1.1f%%", startangle=140)
ax3.set_title("Remote vs Onsite Job Distribution")
ax3.axis("equal")
st.pyplot(fig3)

