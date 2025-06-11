import streamlit as st
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import STL

def stl_recovery_trend(covid_df):
    st.subheader("Recovery Ratio Trend (STL Decomposition)")

    covid_df['Recovered'] = covid_df['Cases'] - covid_df['Deaths']
    stats_df = covid_df.groupby('Date')[['Recovered', 'Deaths']].sum().reset_index()
    stats_df['Recovery_Ratio'] = stats_df['Recovered'] / (stats_df['Recovered'] + stats_df['Deaths'])

    series = stats_df['Recovery_Ratio']
    stl = STL(series, period=30).fit()

    fig, ax = plt.subplots(figsize=(12, 5))
    ax.plot(stats_df['Date'], stl.trend, label="Trend", color='green')
    ax.set_title("STL Decomposition of Recovery Ratio")
    ax.set_xlabel("Date")
    ax.set_ylabel("Recovery Ratio")
    ax.legend()
    st.pyplot(fig)