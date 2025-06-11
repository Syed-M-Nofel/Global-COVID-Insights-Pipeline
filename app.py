import streamlit as st
from utils.data_loader import load_data
from utils.visualizations import show_global_trends, show_country_vax_bar
from utils.analysis import stl_recovery_trend

st.set_page_config(page_title="COVID-19 Global Insights", layout="wide")

st.title("🌍 COVID-19 Global Insights Dashboard")
st.markdown("Observe infection trends, vaccination progress, and recovery patterns across the globe.")

# Load Data
covid_df, owid_df = load_data()

# Sidebar Controls
st.sidebar.header("Filter")
metrics = ["Cases", "Deaths", "Recovered"]
selected_metric = st.sidebar.selectbox("Select Metric", metrics)

# Main Tabs
tab1, tab2, tab3 = st.tabs(["📈 Global Trends", "💉 Vaccination Analysis", "🔍 Recovery Trends"])

with tab1:
    show_global_trends(covid_df, selected_metric)

with tab2:
    show_country_vax_bar(owid_df)

with tab3:
    stl_recovery_trend(covid_df)