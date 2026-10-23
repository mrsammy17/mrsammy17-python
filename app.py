import pandas as pd
import plotly.express as px
import streamlit as st

st.title("My First Dashboard")

df = pd.read_csv("data.csv", parse_dates=["date"])

category = st.sidebar.multiselect("Category", df["category"].unique())
if category:
    df = df[df["category"].isin(category)]

st.metric("Total", f"{df['amount'].sum():,.2f}")
st.plotly_chart(px.line(df, x="date", y="amount", title="Over time"))
st.dataframe(df)