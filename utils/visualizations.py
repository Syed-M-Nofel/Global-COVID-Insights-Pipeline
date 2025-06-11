import pandas as pd
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt

def show_global_trends(df, metric='Cases'):
    st.subheader(f"Global {metric} Over Time")

    daily = df.groupby("Date")[metric].sum()

    fig, ax = plt.subplots(figsize=(12, 5))
    sns.lineplot(x=daily.index, y=daily.values, ax=ax)
    ax.set_title(f"Global Daily {metric}")
    ax.set_xlabel("Date")
    ax.set_ylabel(metric)
    st.pyplot(fig)


def show_country_vax_bar(owid_df, date="2021-08-01"):
    st.subheader(f"Countries with < 50% Vaccination (As of {date})")

    target_date = pd.to_datetime(date)
    df = owid_df[owid_df['Date'] == target_date][['Country/Region', 'people_vaccinated_per_hundred']].dropna()
    low_vax = df[df['people_vaccinated_per_hundred'] < 50].sort_values('people_vaccinated_per_hundred')

    if low_vax.empty:
        st.warning("No countries found with <50% coverage on that date.")
        return

    fig, ax = plt.subplots(figsize=(14, len(low_vax) * 0.3))
    sns.barplot(
        data=low_vax,
        x='people_vaccinated_per_hundred',
        y='Country/Region',
        palette='flare',
        ax=ax
    )
    ax.set_title(f"Countries with <50% Vaccination (As of {date})")
    ax.set_xlabel("Vaccinated per 100 People")
    ax.set_ylabel("Country")
    plt.yticks(fontsize=9)
    st.pyplot(fig)