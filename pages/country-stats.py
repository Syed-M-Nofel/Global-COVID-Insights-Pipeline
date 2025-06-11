import streamlit as st
import pandas as pd

st.title("🌍 Country-Specific COVID-19 Statistics")

@st.cache_data
def load_data():
    return pd.read_csv("data/processed_covid_data.csv", parse_dates=["Date"])

df = load_data()

# Sidebar filter to select a country
country_list = sorted(df["Country/Region"].unique())
selected_country = st.selectbox("Select a country to view", country_list)

# Filter the data
country_df = df[df["Country/Region"] == selected_country]

# Line chart for Cases and Deaths
st.subheader(f"Case and Death Trends - {selected_country}")
st.line_chart(country_df.set_index("Date")[["Cases", "Deaths"]])