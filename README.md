# 🌍 Socio-Economic Indicators Map - European Union (Streamlit App)

This project visualizes various socio-economic indicators (e.g. unemployment rate, GDP per capita, education, life expectancy) across the **European Union** using an interactive Streamlit web application.

It features:
- Static maps with color gradients using **Matplotlib + GeoPandas**
- Interactive maps with zoom, popups, and highlighting using **Folium**
- Dropdowns for selecting indicators and countries
- Pre-processed CSV data and country geometry in GeoJSON

---

## 📦 Installation

Make sure you have **Python 3.8+** installed.

1. Clone or download this repository:
```bash
git clone https://github.com/mihadiv/software-packages-maps.git
cd software-packages-maps
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

---

## ▶️ Running the App

Simply start the app with:

```bash
streamlit run main.py
```

The app will open in your default browser at [http://localhost:8501](http://localhost:8501)

---

## 📁 Files

- `main.py` – Main Streamlit app script
- `Unemployment_rate_2023_EU.csv` – Input data with indicators by country
- `countries.geo.json` – GeoJSON with country shapes
- `requirements.txt` – Python dependencies
- `README.md` – Project description

---

## ✅ Indicators Included

- Unemployment Rate
- GDP per Capita
- Employment Rate
- Average Salary
- Education Level
- Life Expectancy
- Public Spending

---

## 💡 Credits

Built with [Streamlit](https://streamlit.io), [GeoPandas](https://geopandas.org/), and [Folium](https://python-visualization.github.io/folium/).

GeoJSON map data from [Johan's World GeoJSON](https://github.com/johan/world.geo.json).

Data compiled from Eurostat and other public sources.
