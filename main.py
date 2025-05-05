import streamlit as st
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
import unidecode
import folium
from streamlit_folium import st_folium

st.set_page_config(layout="wide")
st.markdown("""
<div style='text-align: center;'>
    <h1>🌍 Visualization of Socio-Economic Indicators</h1>
    <h2 style='margin-top: -15px;'>on the European Map</h2>
</div>
""", unsafe_allow_html=True)

# ----- Load and clean the data -----

@st.cache_data
def load_data():
    df = pd.read_csv("Unemployment_rate_2023_EU.csv")
    world = gpd.read_file("countries.geo.json")

    # Normalize country names
    def normalize(name):
        return unidecode.unidecode(name.strip().lower())

    df["Country_norm"] = df["Country"].apply(normalize)
    world["GeoCountry"] = world["name"].apply(normalize)
    world["OriginalGeoName"] = world["name"]

    # Manual corrections for name mismatches
    name_corrections = {
        "serbia": "republic of serbia",
        "czechia": "czech republic",
        "north macedonia": "macedonia"
    }
    df["Country_norm"] = df["Country_norm"].replace(name_corrections)

    # Match and merge data
    matched = world[world["GeoCountry"].isin(df["Country_norm"])].copy()
    merged = matched.merge(df, left_on="GeoCountry", right_on="Country_norm", how="left")

    # Show unmatched countries
    unmatched = set(df["Country_norm"]) - set(world["GeoCountry"])
    if unmatched:
        st.warning(f"⚠️ Countries from CSV not found in GeoJSON: "
                   f"{[df[df['Country_norm'] == u]['Country'].values[0] for u in unmatched]}")

    return merged

# ----- Load merged data -----

gdf = load_data()

# ----- Select indicator to display -----

col_map_selector = st.columns([1, 2, 1])
with col_map_selector[1]:
    st.subheader("🗺️ Map")
    indicator = st.selectbox(
        "Select an indicator to display on the map:",
        [
            "Unemployment_Rate",
            "GDP_per_capita",
            "Employment_Rate",
            "Average_Salary",
            "Education_Level",
            "Life_Expectancy",
            "Public_Spending"
        ]
    )

# ----- Static map with matplotlib -----

fig, ax = plt.subplots(figsize=(7.5, 5))
gdf.plot(
    column=indicator,
    ax=ax,
    legend=True,
    cmap="viridis",
    edgecolor="black",
    linewidth=0.8,
    legend_kwds={'label': indicator.replace("_", " "), 'orientation': "vertical"}
)

ax.set_title(f"{indicator.replace('_', ' ')} in the European Union", fontsize=13)
ax.axis("off")
col_static_map = st.columns([1, 2, 1])
with col_static_map[1]:
    st.pyplot(fig)

# ----- Display data table -----

st.divider()
st.subheader("📊 Dataset")
st.dataframe(gdf.drop(columns=["geometry", "Country_norm", "GeoCountry", "OriginalGeoName"]))

# ----- Interactive folium map -----

st.divider()
center_cols = st.columns([1, 2, 1])
with center_cols[1]:
    st.subheader("🧭 Interactive Map with Zoom and Pop-up")
    selected_country = st.selectbox("Select a country to highlight:", gdf["Country"].sort_values())

    # Create folium map centered on Europe
    m = folium.Map(location=[50, 10], zoom_start=4, tiles="CartoDB positron")

    # Add countries to the folium map
    for _, row in gdf.iterrows():
        country_name = row["Country"]
        value = row[indicator]
        tooltip_text = f"{country_name}: {indicator.replace('_', ' ')} = {value}"

        # Highlight selected country
        color = "red" if country_name == selected_country else "blue"

        folium.GeoJson(
            row["geometry"],
            name=country_name,
            tooltip=tooltip_text,
            style_function=lambda x, color=color: {
                "fillColor": color,
                "color": "black",
                "weight": 1,
                "fillOpacity": 0.5,
            },
            popup=folium.Popup(f"<b>{country_name}</b><br>{indicator.replace('_', ' ')}: {value}", max_width=300)
        ).add_to(m)

    # Display folium map in Streamlit
    st_folium(m, width=740, height=500)
