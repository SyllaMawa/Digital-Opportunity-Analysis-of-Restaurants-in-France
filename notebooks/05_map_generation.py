# Databricks notebook source

 #!pip install folium

# ================================
# . IMPORTS
# ================================
import folium
import pandas as pd 

# ================================
#  CHARGEMENT DATA
# ================================
df = pd.read_csv("../data/processed/restaurants_with_score.csv")

# ================================
#  CRÉATION CARTE
# ================================
# centre de la France
map_france = folium.Map(
    location=[46.6, 2.5],
    zoom_start=6,
    tiles="CartoDB positron",
    attr="no external API"
)

# ================================
#  COULEURS PAR NIVEAU
# ================================
def get_color(level):
    if level == "HIGH":
        return "red"
    elif level == "MEDIUM":
        return "orange"
    else:
        return "green"

# ================================
#  AJOUT DES POINTS
# ================================
for _, row in df.iterrows():
    
    # éviter erreurs si coordonnées manquantes
    if pd.isna(row.get("lat")) or pd.isna(row.get("lng")):
        continue
    
    popup_text = f"""
    <b>{row['name']}</b><br>
    Ville: {row['city']}<br>
    Rating: {row['rating']}<br>
    Reviews: {row['reviews']}<br>
    Score: {round(row['opportunity_score'], 2)}<br>
    Niveau: {row['opportunity_level']}
    """
    
    folium.CircleMarker(
        location=[row["lat"], row["lng"]],
        radius=5,
        color=get_color(row["opportunity_level"]),
        fill=True,
        fill_opacity=0.7,
        popup=popup_text
    ).add_to(map_france)


# ================================
#  SAUVEGARDE
# ================================
map_france.save("../reports/interactive_map.html")

print("Carte générée : ../reports/interactive_map.html")