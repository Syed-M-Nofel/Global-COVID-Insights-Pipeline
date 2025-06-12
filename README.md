# 🌐 Global COVID-19 Insights Pipeline

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![Streamlit App](https://img.shields.io/badge/View%20App-LIVE-green)](https://global-covid-insights-pipeline.streamlit.app/)
[![GitHub last commit](https://img.shields.io/github/last-commit/Syed-M-Nofel/Global-COVID-Insights-Pipeline)](https://github.com/Syed-M-Nofel/Global-COVID-Insights-Pipeline)
[![Visitors](https://visitor-badge.laobi.icu/badge?page_id=Syed-M-Nofel.Global-COVID-Insights-Pipeline)](https://github.com/Syed-M-Nofel)

An interactive, end-to-end data science pipeline and dashboard for analyzing **COVID-19 trends globally**, using up-to-date data from trusted public sources.

Users can explore interactive visualizations covering infections, mortality, recoveries, seasonal analysis, and vaccine coverage for different countries and timelines. Deployed using **Streamlit Cloud**.

> 🔗 **Live App**: [https://global-covid-insights-pipeline.streamlit.app](https://global-covid-insights-pipeline.streamlit.app)

---

## 📌 Project Overview

The goal of this project is to extract meaningful insights from global COVID-19 data using Python-based data science techniques and render them through an intuitive web-based dashboard for public or decision-maker use.

The process includes:
- Data cleaning and transformation
- Exploratory data analysis
- Time-series decomposition (STL)
- Correlation and statistical insight discovery
- Web app development for interaction and presentation

---

## 📊 Key Features

- 📈 **Global trend visualizations** for COVID-19 cases, deaths, recoveries
- 💉 **Vaccination gap analysis** by country with dynamic charts
- 📉 **Recovery ratio trends** using STL time-series decomposition
- 🌍 **Country-specific dashboards** with case & death comparison
- 📊 Clean and professional **Streamlit-based UI**, responsive layout

---

## 🗺️ Real-World Impact

Understanding how COVID-19 has spread and how different regions responded is essential for pandemic response, future planning, and public health awareness.

This tool can assist:
- Researchers analyzing pandemic trends
- Journalists visualizing country gaps in vaccination or deaths
- Public health educators showcasing dynamic pandemic dashboards
- Students and professionals demonstrating full-stack data science

---

## 📷 Screenshots

### Global Trend Visualization
![Global Cases - Screenshot](https://raw.githubusercontent.com/Syed-M-Nofel/Global-COVID-Insights-Pipeline/main/screenshots/global-trends.jpg)

### Vaccination Progress by Country
![Vaccination Gap - Screenshot](https://raw.githubusercontent.com/Syed-M-Nofel/Global-COVID-Insights-Pipeline/main/screenshots/vaccination-analysis.jpg)

---

## 🌐 Application Structure

```
covid19-global-insights-app/
├── app.py
├── requirements.txt
├── data/
│   └── processed_covid_data.csv
│   └── external/owid-covid-data.csv
├── pages/
│   ├── about.py
│   └── country-stats.py
├── utils/
│   ├── data_loader.py
│   ├── analysis.py
│   └── visualizations.py
├── README.md
└── LICENSE
```

---

## 💾 How to Run Locally

1. **Clone the repository:**

```bash
git clone https://github.com/Syed-M-Nofel/Global-COVID-Insights-Pipeline.git
cd Global-COVID-Insights-Pipeline/covid19-global-insights-app
```

2. **Install dependencies:**

```bash
pip install -r requirements.txt
```

3. **Run the Streamlit app:**

```bash
streamlit run app.py
```

---

## 📈 Dataset Sources

| Dataset | Description | Source |
|---------|-------------|--------|
| **Johns Hopkins University** | Global COVID-19 case and death data | [JHU CSSE GitHub](https://github.com/CSSEGISandData/COVID-19) |
| **Our World in Data (OWID)** | Vaccination data + population + metadata | [OWID](https://ourworldindata.org/coronavirus-source-data) |

---

## 🛡️ License

This project is licensed under the [MIT License](LICENSE).  
You are free to use, modify, and distribute this code with appropriate credit to the original author.

---

## 🤝 How to Contribute / Fork

1. Fork the repository
2. Clone your fork
3. Create a new working branch
4. Make your changes
5. Push and submit a Pull Request

---

## 📬 Contact

**Author:** Syed M. Nofel  
**GitHub:** [@Syed-M-Nofel](https://github.com/Syed-M-Nofel)  
**Live App:** [Streamlit Link](https://global-covid-insights-pipeline.streamlit.app)

