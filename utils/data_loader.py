import pandas as pd

def load_data():
    covid_df = pd.read_csv("data/processed_covid_data.csv", parse_dates=["Date"])
    owid_df = pd.read_csv("data/external/owid-covid-data.csv", parse_dates=["date"])
    
    # Standardize OWID columns
    owid_df.rename(columns={
        'location': 'Country/Region',
        'date': 'Date'
    }, inplace=True)
    
    # Calculate Recovered column once and keep it in dataframe
    covid_df['Recovered'] = covid_df['Cases'] - covid_df['Deaths']

    return covid_df, owid_df