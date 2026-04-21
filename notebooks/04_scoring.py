# Databricks notebook source
# ================================
#  IMPORTS
# ================================
import pandas as pd
import numpy as np

# ================================
#  CHARGEMENT DES DONNÉES
# ================================
df_v1 = pd.read_csv("../data/raw/restaurants_v1.csv")
df_v2 = pd.read_csv("../data/raw/restaurants_v2.csv")

# ================================
#  UNIFICATION
# ================================
df_v1["version"] = "V1"
df_v2["version"] = "V2"

df = pd.concat([df_v1, df_v2], ignore_index=True)

# ================================
#  CLEANING
# ================================

# Extraction propre de la ville
df["city"] = df["address"].str.extract(r"\d{5}\s+([^,]+)")
df["city"] = df["city"].str.strip()

# Gestion des valeurs manquantes
df["rating"] = df["rating"].fillna(df["rating"].median())
df["reviews"] = df["reviews"].fillna(0)

# ================================
#  NORMALISATION
# ================================

# Rating (0-5 → 0-1)
df["rating_norm"] = df["rating"] / 5

# Reviews → log transformation (réduction des extrêmes)
df["reviews_log"] = np.log1p(df["reviews"])

# Normalisation min-max
df["reviews_norm"] = (
    df["reviews_log"] - df["reviews_log"].min()
) / (
    df["reviews_log"].max() - df["reviews_log"].min()
)

# ================================
#  CALCUL DU SCORE
# ================================

df["opportunity_score"] = (
    df["no_website"].astype(int) * 0.5 +   # critère principal
    (1 - df["rating_norm"]) * 0.2 +        # note faible = besoin digital
    (1 - df["reviews_norm"]) * 0.3         # faible visibilité
)

# ================================
#  SEGMENTATION
# ================================

def classify(score):
    if score > 0.7:
        return "HIGH"
    elif score > 0.4:
        return "MEDIUM"
    else:
        return "LOW"

df["opportunity_level"] = df["opportunity_score"].apply(classify)

# ================================
# TOP OPPORTUNITÉS
# ================================

top_opportunities = df.sort_values(
    by="opportunity_score", ascending=False
).head(20)

print("\n TOP 20 RESTAURANTS À CONTACTER :")
display(top_opportunities[[
    "name",
    "city",
    "rating",
    "reviews",
    "no_website",
    "opportunity_score",
    "opportunity_level"
]])

# ================================
#  DISTRIBUTION DES SEGMENTS
# ================================

print("\n Répartition des niveaux d’opportunité :")
display(df["opportunity_level"].value_counts())

# ================================
#  SAUVEGARDE
# ================================

df.to_csv("../data/processed/restaurants_with_score.csv", index=False)

print(" Dataset avec score sauvegardé !")