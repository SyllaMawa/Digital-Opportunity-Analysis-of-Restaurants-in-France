# Databricks notebook source
# ================================
#  IMPORTS
# ================================
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# ================================
#  CHARGEMENT DES DONNÉES
# ================================
df_v1 = pd.read_csv("../data/raw/restaurants_v1.csv")
df_v2 = pd.read_csv("../data/raw/restaurants_v2.csv")

# ================================
#  UNIFICATION DES DATASETS
# ================================
df_v1["version"] = "V1"
df_v2["version"] = "V2"

df = pd.concat([df_v1, df_v2], ignore_index=True)

print(" Taille du dataset combiné :", df.shape)

# ================================
#  APERÇU GÉNÉRAL
# ================================
print("\n Aperçu du dataset :")
display(df.head())

print("\n Info dataset :")
df.info()

# ================================
#  VALEURS MANQUANTES
# ================================
print("\n Valeurs manquantes :")
display(df.isna().sum())

# ================================
#  CLEANING IMPORTANT
# ================================

# Nettoyage colonne city (extraction propre)
df["city"] = df["address"].str.extract(r"\d{5}\s+([^,]+)")

# Nettoyage espaces
df["city"] = df["city"].str.strip()

# Gestion des valeurs manquantes rating/reviews
df["rating"] = df["rating"].fillna(df["rating"].median())
df["reviews"] = df["reviews"].fillna(0)

# ================================
#  ANALYSE NO WEBSITE
# ================================
print("\n Répartition no_website :")
display(df["no_website"].value_counts(normalize=True))

# ================================
# COMPARAISON V1 vs V2
# ================================
print(" % no website par version :")
display(df.groupby("version")["no_website"].mean())

# ================================
#  TOP ZONES (VILLE)
# ================================
print(" Top villes avec le plus de restaurants sans site web :")

top_zones = (
    df[df["no_website"] == True]
    .groupby("city")
    .size()
    .sort_values(ascending=False)
    .head(10)
)

display(top_zones)

# ================================
#  TAUX PAR VILLE 
# ================================
print("\n Taux de restaurants sans site web par ville :")

city_rate = (
    df.groupby("city")["no_website"]
    .mean()
    .sort_values(ascending=False)
    .head(10)
)

display(city_rate)

# ================================
#  ANALYSE DES RATINGS
# ================================
print(" Analyse des ratings :")
display(df["rating"].describe())

# ================================
#  RELATION REVIEWS / WEBSITE
# ================================
print(" Moyenne reviews selon présence site web :")
display(df.groupby("no_website")["reviews"].mean())

# ================================
# VISUALISATION SIMPLE
# ================================
plt.figure(figsize=(6,4))
df["no_website"].value_counts().plot(kind="bar")
plt.title("Restaurants avec ou sans site web")
plt.xticks(rotation=0)
plt.show()

# ================================
# INSIGHT FINAL
# ================================
print("\n💡 INSIGHT :")
print("""
Les zones périphériques et certaines villes présentent une proportion plus élevée
de restaurants sans site web, ce qui indique un fort potentiel de digitalisation.

Les restaurants sans site web ont généralement moins de reviews,
ce qui suggère une visibilité en ligne plus faible.
""")