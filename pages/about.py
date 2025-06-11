import streamlit as st

st.title("📄 About This Project")

st.markdown(
    """
    This application is a COVID-19 Data Insights Dashboard, built using **Streamlit**.

    It visualizes global trends, analyzes vaccination progress, and examines recovery patterns over time.

    **What this app includes:**
    - 📈 Infection, death, and recovery visualizations
    - 💉 Vaccination rate analysis country-by-country
    - 🔍 Time-series recovery ratio (STL Decomposition)
    - 🌐 Country-level stats (interactive)

    **Data Sources:**
    - [Our World in Data (OWID)](https://ourworldindata.org/coronavirus)
    - [JHU CSSE COVID-19 Data](https://github.com/CSSEGISandData/COVID-19)

    -----
    Made with ❤️ by Syed Nofel | `Data Scientist`
    """
)