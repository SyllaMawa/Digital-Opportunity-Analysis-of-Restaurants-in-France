# 🍽️ Où se cachent les restaurants non-digitalisés ? 
### *Analyse d'opportunités pour booster la visibilité locale en France*

##  Le constat de départ
L'idée est simple : beaucoup de pépites culinaires en France sont invisibles en ligne. En tant que Data Analyst, j'ai voulu transformer cette intuition en données exploitables. Pourquoi ? Parce qu'un restaurant sans site web, c'est un commerçant qui passe à côté de clients, et une opportunité pour nous de les accompagner dans leur digitalisation.

---

##  Organisation du projet
Pour que le projet soit aussi propre que les données, j'ai structuré l'espace de travail ainsi :

```text
.
├── data/
│   ├── raw/             # Les extractions brutes (V1 et V2)
│   └── processed/       # Le dataset final enrichi de mes scores
├── notebooks/           # Ma logique de collecte, d'analyse et de scoring
├── reports/             # Le résultat visuel (ma carte interactive)
├── README.md            # Ce que vous lisez
└── requirements.txt     # Les outils utilisés
```

---

##  Le défi : De la théorie à la réalité du terrain

##  Le défi : De la théorie à la réalité du terrain

### L'approche V1 : Les "grandes villes" (Un premier pas trompeur)
Au début, j'ai visé large : Paris, Lyon, Marseille. Résultat ? **Seulement 10%** des restaurants n'avaient pas de site web. 
*Pourquoi ?* Parce que l'algorithme de Google met en avant ceux qui sont déjà digitalisés. C’est le "biais de survie" du web : on ne voit que ceux qui existent déjà.

### L'approche V2 : Le "quartier par quartier" (Le déclic)
J'ai donc changé de méthode. Au lieu de chercher des "villes", j'ai cherché des "quartiers" et des contextes locaux (Belleville, Saint-Denis, bistrot de quartier). 
**Résultat : Le taux de restaurants sans site est monté à 22% !**
C’est là que se trouve la vraie opportunité business : chez les indépendants et les commerces de proximité.

---

##  Le "Digital Opportunity Score" : Ma méthode de tri
Identifier l'absence de site web ne suffit pas. Pour savoir *qui* contacter en priorité, j'ai créé un algorithme de scoring maison basé sur 3 piliers :

1.  **Absence de site (50%)** : Le critère éliminatoire.
2.  **Note Google (20%)** : Une note moyenne indique souvent un manque de gestion de l'e-réputation.
3.  **Volume d'avis (30%)** : Peu d'avis = déficit de visibilité flagrant.

**Score > 0.7 ?** C’est un prospect "High Priority" qui a tout à gagner à se digitaliser.

---

##  Ce que les données m'ont appris (Insights)

*   **Le paradoxe de la visibilité** : Les restaurants sans site web ont en moyenne beaucoup moins d'avis que les autres. Ils sont dans un angle mort numérique.
*   **Les zones d'ombre** : La digitalisation est beaucoup plus faible dans les zones périurbaines et les quartiers populaires. C'est là que l'impact d'une solution web serait le plus fort.
*   **Qualité vs Visibilité** : Beaucoup de restaurants avec d'excellentes notes (4.5+) n'ont pas de site. Ils font un travail formidable en cuisine mais sont invisibles pour les nouveaux clients.

---

##  Visualisation : La carte interactive

> [!TIP]
> Le résultat final est une **carte interactive HTML** qui ne peut pas être affichée directement comme une image. Vous pouvez l'ouvrir avec n'importe quel navigateur.

[👉 Ouvrir la carte interactive (reports/interactive_map.html)](reports/interactive_map.html)

Pour rendre ces données vivantes, j'ai généré une carte interactive complète :
- **Rouge** : Haute priorité (Fort besoin digital).
- **Orange** : Potentiel moyen.
- **Vert** : Déjà bien positionné.

C'est un véritable outil de prospection : on peut zoomer sur un quartier et voir instantanément qui appeler.

---

##  Ma boîte à outils
- **Python & Pandas** : Pour manipuler et nettoyer les données.
- **Google Places API** : Ma source de données brute.
- **Folium** : Pour la cartographie interactive.
- **Matplotlib** : Pour les analyses statistiques.

---

## 🏁 Conclusion & Ouverture
Ce projet n'est pas qu'un exercice technique. C'est une démonstration de la façon dont la **Data Analysis** peut servir une stratégie de **Sales Ops** ou de **Growth Hacking**. 

**Prochaine étape ?** Automatiser l'envoi de rapports personnalisés aux restaurateurs pour leur montrer leur potentiel de croissance grâce à un site web.

---
*Projet réalisé avec passion par un analyste qui aime autant la donnée que la bonne cuisine.* 
