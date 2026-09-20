import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="Mental Health in Tech Survey", layout="wide")

@st.cache_data
def load_data():
    df = pd.read_csv("survey.csv")
    df["Timestamp"] = pd.to_datetime(df["Timestamp"], errors="coerce")
    df["Age_clean"] = df["Age"].where(df["Age"].between(18, 100))
    return df

df = load_data()

st.title("Mental Health in Tech Survey — EDA Dashboard")
st.caption("2014 survey dataset | Exploratory analysis")

# Sidebar filters
st.sidebar.header("Filters")

countries = sorted(df["Country"].dropna().unique())
selected_country = st.sidebar.selectbox("Country", ["All"] + countries)

treatment_filter = st.sidebar.selectbox("Treatment", ["All", "Yes", "No"])

filtered = df.copy()
if selected_country != "All":
    filtered = filtered[filtered["Country"] == selected_country]
if treatment_filter != "All":
    filtered = filtered[filtered["treatment"] == treatment_filter]

# KPIs
c1, c2, c3, c4 = st.columns(4)
c1.metric("Responses", len(filtered))
c2.metric("Treatment: Yes", int((filtered["treatment"] == "Yes").sum()))
c3.metric("Family History: Yes", int((filtered["family_history"] == "Yes").sum()))
c4.metric("Remote Work: Yes", int((filtered["remote_work"] == "Yes").sum()))

st.divider()

left, right = st.columns(2)

with left:
    st.subheader("Treatment Distribution")
    fig, ax = plt.subplots(figsize=(6, 4))
    filtered["treatment"].value_counts().plot(kind="bar", ax=ax)
    ax.set_xlabel("Treatment")
    ax.set_ylabel("Respondents")
    ax.set_title("Treatment Responses")
    st.pyplot(fig)

with right:
    st.subheader("Treatment by Family History")
    ct = pd.crosstab(filtered["family_history"], filtered["treatment"], normalize="index") * 100
    fig, ax = plt.subplots(figsize=(6, 4))
    ct.plot(kind="bar", ax=ax)
    ax.set_ylabel("Percentage")
    ax.set_xlabel("Family History")
    ax.set_title("Treatment % by Family History")
    ax.legend(title="Treatment")
    st.pyplot(fig)

st.subheader("Workplace Support")
support_cols = ["benefits", "care_options", "wellness_program", "seek_help"]
support = pd.DataFrame({
    col: filtered[col].value_counts()
    for col in support_cols
}).fillna(0)

st.dataframe(support.astype(int), use_container_width=True)

st.subheader("Age Distribution")
fig, ax = plt.subplots(figsize=(10, 4))
ax.hist(filtered["Age_clean"].dropna(), bins=20, edgecolor="black")
ax.set_xlabel("Age")
ax.set_ylabel("Respondents")
ax.set_title("Cleaned Age Distribution")
st.pyplot(fig)

st.info("Note: This dashboard is based on the 2014 survey and is descriptive; relationships shown should not be interpreted as causal.")
