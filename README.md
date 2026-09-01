# 🌍 EU Socio-Economic Indicators Map

An interactive Streamlit application for exploring and visualizing socio-economic indicators across European Union countries.

The project combines Python-based data analysis with static and interactive geospatial visualizations using GeoPandas, Matplotlib, and Folium.

---

## ✨ Key Features

- Interactive visualization of socio-economic indicators across EU countries
- Static choropleth maps using GeoPandas and Matplotlib
- Interactive maps with zoom, popups, and country highlighting using Folium
- Indicator selection through an interactive Streamlit interface
- Country-level filtering and exploration
- Integration of CSV indicator data with GeoJSON country geometries

---

## 🧰 Technologies Used

- **Python**
- **Streamlit**
- **pandas**
- **GeoPandas**
- **Matplotlib**
- **Folium**
- **GeoJSON**

---

## 📊 Indicators

The application includes the following socio-economic indicators:

- Unemployment Rate
- GDP per Capita
- Employment Rate
- Average Salary
- Education Level
- Life Expectancy
- Public Spending

---

## 📁 Project Structure

| File | Description |
|---|---|
| `main.py` | Main Streamlit application |
| `Unemployment_rate_2023_EU.csv` | Country-level socio-economic indicator data |
| `countries.geo.json` | GeoJSON geometries used for map visualization |
| `requirements.txt` | Python dependencies |
| `README.md` | Project overview and setup instructions |

---

## ▶️ Running the Application

### Prerequisites

Python 3.8 or later is required.

### Installation

Clone the repository:

```bash
git clone https://github.com/mihaeladivoiu/eu-socioeconomic-map.git
cd eu-socioeconomic-map
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

### Start the Application

```bash
streamlit run main.py
```

The application will be available locally at:

```text
http://localhost:8501
```

---

## 📚 Data Sources

Country geometry data is based on the [World GeoJSON dataset](https://github.com/johan/world.geo.json).

Socio-economic indicator data was compiled from Eurostat and other public sources.

---

## 👩‍💻 Authors

**Mihaela-Irina Divoiu**  
**Daria-Mihaela Ducu**

Academic project developed at the Bucharest University of Economic Studies, Faculty of Economic Cybernetics, Statistics and Informatics.
