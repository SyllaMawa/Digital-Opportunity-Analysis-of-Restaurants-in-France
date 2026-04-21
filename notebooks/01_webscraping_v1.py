# Databricks notebook source
# ================================
# 1. IMPORTS
# ================================
import requests
import pandas as pd
import time

# ================================
# 2. CONFIGURATION
# ================================

# Remplace par ta vraie clé
API_KEY = "Votre clé API"

# URLs API Google Places
search_url = "https://maps.googleapis.com/maps/api/place/textsearch/json"
details_url = "https://maps.googleapis.com/maps/api/place/details/json"

# ================================
# 3. FONCTION PRINCIPALE
# ================================

def get_restaurants(query):
    restaurants = []

    params = {
        "query": query,
        "key": API_KEY
    }

    while True:
        response = requests.get(search_url, params=params)
        data = response.json()
        print("STATUS:", data.get("status"))
        print("FULL RESPONSE:", data)

        # Parcourir les résultats
        for place in data.get("results", []):
            place_id = place.get("place_id")

            # Appel API pour détails
            details_params = {
                "place_id": place_id,
                "fields": "name,rating,user_ratings_total,formatted_address,website,types",
                "key": API_KEY
            }

            details_response = requests.get(details_url, params=details_params)
            details = details_response.json().get("result", {})

            restaurants.append({
                "name": details.get("name"),
                "address": details.get("formatted_address"),
                "rating": details.get("rating"),
                "reviews": details.get("user_ratings_total"),
                "website": details.get("website"),
                "lat": place["geometry"]["location"]["lat"],
                "lng": place["geometry"]["location"]["lng"],
                "category": ", ".join(details.get("types", [])) if details.get("types") else None
     
            })

            time.sleep(0.2)  

        # Pagination
        next_page_token = data.get("next_page_token")
        if not next_page_token:
            break

        time.sleep(2)  # obligatoire pour l'activation de notre token
        params = {
            "pagetoken": next_page_token,
            "key": API_KEY
        }

    return restaurants


# ================================
# 4. MULTI-REQUÊTES 
# ================================
#Je recupere les Grandes villes (fort potentiel business)
cities_large = [
    "Paris",
    "Marseille",
    "Lyon",
    "Toulouse",
    "Nice",
    "Nantes",
    "Strasbourg",
    "Montpellier",
    "Bordeaux",
    "Lille",
    "Rennes",
    "Reims",
    "Le Havre",
    "Saint-Étienne",
    "Toulon",
    "Grenoble"
]
#Je recupere aussi les moyenne ville qui sera tre interessant à anlyser pour notre cas de recherche de ville digitalisée
cities_medium = [
    "Angers",
    "Nîmes",
    "Villeurbanne",
    "Clermont-Ferrand",
    "Aix-en-Provence",
    "Brest",
    "Limoges",
    "Tours",
    "Amiens",
    "Perpignan",
    "Metz",
    "Besançon",
    "Orléans",
    "Mulhouse",
    "Rouen",
    "Caen",
    "Nancy"
]

#Les zones périurbaines(Les zones sous cotées)
cities_suburban = [
    "Saint-Denis",
    "Montreuil",
    "Argenteuil",
    "Vitry-sur-Seine",
    "Créteil",
    "Aubervilliers",
    "Colombes",
    "Nanterre",
    "Clermont-Ferrand",
    "Lyon Villeurbanne",
    "Marseille 15e",
    "Marseille 16e",
    "Paris 18e",
    "Paris 19e",
    "Paris 20e"
]
cities =cities_large +cities_medium +cities_suburban

queries = [f"restaurants {city}" for city in cities]

all_data = []



for q in queries:
    print(f" Collecte : {q}")
    data = get_restaurants(q)
    all_data.extend(data)

# ================================
# 5. DATAFRAME
# ================================

df = pd.DataFrame(all_data)

# suppression de nos doublons
df = df.drop_duplicates(subset=["name", "address"])

# ================================
# 6. FEATURE ENGINEERING
# ================================

# restaurant sans site web
df["no_website"] = df["website"].isna()

# ================================
# 7. VERIFICATION
# ================================

print("Taille dataset :", df.shape)
print("\n Aperçu :")
display(df.head())

print("\n Valeurs manquantes :")
display(df.isna().sum())

print("\n % restaurants sans site :")
display(df["no_website"].value_counts(normalize=True))

# ================================
# 8. SAUVEGARDE
# ================================

# version locale (ou Databricks FileStore)
df.to_csv("../data/raw/restaurants_v1.csv", index=False)

print(" Fichier sauvegardé !")

# COMMAND ----------

