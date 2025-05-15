 # Global-COVID-Insights-Pipeline

A unified preprocessing and exploratory analysis framework for the JHU-CSSE COVID-19 datasets, enriched with vaccination metrics to surface dynamic infection hotspots, mortality correlations, and seasonal patterns.

---

## 🚀 Features

- **Data Ingestion & Cleaning**  
  - Loads JHU-CSSE time-series for confirmed cases, deaths, and recoveries  
  - Integrates vaccination data from Our World in Data  
  - Handles missing values: drops sparse columns (>30% missing) and forward-fills time series

- **Exploratory Data Analysis (EDA)**  
  - Descriptive statistics: mean, median, mode, standard deviation, skewness  
  - Distribution plots: histograms, KDE, boxplots  
  - Temporal trends: global & country-level line charts  
  - Relationship analysis: correlation matrices & pairplots  
  - Geographic visualization examples (choropleth mapping stubs)

- **Foundation for Question Answering**  
  - Dynamic ranking of infection hotspots (per-capita)  
  - Correlation & mixed-effects modeling for vaccine–mortality analysis  
  - Time-series decomposition (STL) for recovery vs. death trends & seasonality  
  - Threshold analysis for identifying lagging regions

## 📚 Data Sources & Citations

- **JHU CSSE COVID-19**  
  - **Confirmed Cases**: `time_series_covid19_confirmed_global.csv`  
  - **Deaths**: `time_series_covid19_deaths_global.csv`  
  - **Recoveries**: `time_series_covid19_recovered_global.csv`  
  - Repository: [CSSEGISandData/COVID-19](https://github.com/CSSEGISandData/COVID-19)

- **Our World in Data — COVID-19 Vaccinations**  
  - **Vaccination Data**: `owid-covid-data.csv`  
  - Source: <https://covid.ourworldindata.org/data/owid-covid-data.csv>


