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

### L'approche V1 : Les "grandes villes" (Un premier pas trompeur)
Au début, j'ai visé large : Paris, Lyon, Marseille. Résultat ? **Seulement 10%** des restaurants n'avaient pas de site web. 
*Le piège ?* L'algorithme de Google met naturellement en avant ceux qui sont déjà digitalisés. C’est le "biais de survie" : on ne voit que ceux qui font déjà du bruit sur le web.

### L'approche V2 : Le "quartier par quartier" (Le déclic)
J'ai changé de lunettes. Au lieu de chercher des grandes métropoles, j'ai zoomé sur les quartiers et les bistrots de proximité (Belleville, Saint-Denis, commerces de quartier). 
**Bingo : Le taux de restaurants sans site est monté à 22% !**
C’est là que se trouve la vraie opportunité : chez les indépendants qui font vivre nos quartiers mais qui restent invisibles sur smartphone.

---

##  Le "Digital Opportunity Score" : Mon filtre à opportunités
Identifier l'absence de site web ne suffit pas. Pour savoir quels établissements ont le plus besoin d'un coup de pouce, j'ai créé un score sur-mesure basé sur trois piliers simples :

*   **L'absence de site (50%)** : C'est le critère n°1. Sans site web, un restaurant est coupé d'une grande partie de ses clients potentiels. C'est la base de ma recherche.
*   **La note Google (20%)** : Une note moyenne est souvent le signe que l'image en ligne n'est pas gérée. Le restaurateur subit sa réputation au lieu de la piloter.
*   **Le volume d'avis (30%)** : Très peu d'avis = une visibilité quasi nulle. Même avec une bonne cuisine, le restaurant reste dans l'ombre des algorithmes.

**Verdict ?** Dès que le score dépasse **0.7**, on tient un profil **"Haute Priorité"**. C'est l'établissement qui a le plus gros potentiel de croissance grâce à une simple mise à jour digitale.

---

## Ce que les données m'ont appris
*   **Le paradoxe de l'ombre** : Les restaurants sans site web ont souvent beaucoup moins d'avis. Ils sont coincés dans un "angle mort numérique" : parce qu'ils sont moins visibles, ils attirent moins de retours, ce qui les rend encore moins visibles.
*   **Les zones oubliées** : La digitalisation chute dès qu'on s'éloigne des centres-villes touristiques. C'est dans les zones périurbaines et les quartiers populaires que l'impact d'un site web serait le plus spectaculaire.
*   **Le talent invisible** : J'ai trouvé énormément de pépites avec des notes excellentes (4.5+) qui n'ont pourtant aucun site. Ils font un travail formidable en cuisine, mais leur talent s'arrête à la porte de leur établissement.

---

##  Visualisation : La carte interactive

> [!TIP]
> Le résultat final est une **carte interactive HTML** qui ne peut pas être affichée directement comme une image. Vous pouvez l'ouvrir avec n'importe quel navigateur.

[ Ouvrir la carte interactive (reports/interactive_map.html)](reports/interactive_map.html)

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

##  Conclusion & Prochaines étapes
Ce projet montre que la **Data Analysis** est un outil redoutable pour le terrain. Ce n'est pas juste des chiffres, c'est une boussole pour aider les commerçants à se faire connaître.

**L'étape d'après ?** Automatiser l'envoi de rapports personnalisés. Imaginez un restaurateur recevant un petit diagnostic gratuit lui montrant exactement ce qu'il gagnerait à être en ligne. C'est ça, la puissance de la donnée au service de l'humain.

---
*Projet réalisé avec passion par un analyste qui aime autant la donnée que la bonne cuisine.* 
