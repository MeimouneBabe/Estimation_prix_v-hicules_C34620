# 🚗 Estimation du Prix des Véhicules d'Occasion — CarDekho

<div align="center">

![Python](https://img.shields.io/badge/Python-3.11-3776AB?logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-1.57-FF4B4B?logo=streamlit&logoColor=white)
![XGBoost](https://img.shields.io/badge/XGBoost-3.2-FF6600?logo=xgboost&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-1.6-F7931E?logo=scikit-learn&logoColor=white)
![pandas](https://img.shields.io/badge/pandas-2.2-150458?logo=pandas&logoColor=white)
![License](https://img.shields.io/badge/Licence-MIT-22C55E)
![Status](https://img.shields.io/badge/Status-Déployé-0D6E68)

<br>

**Projet Python · Régression supervisée par Machine Learning**

*Meimoune Baba Cheikh Sidiya — Matricule C34620*
*Professeur Ezyn SEGNANE*

<br>

[**Application en ligne**](https://estimationprixv-hiculesc34620.streamlit.app/) &nbsp;·&nbsp;
[**Dataset Kaggle**](https://www.kaggle.com/datasets/nehalbirla/vehicle-dataset-from-cardekho) &nbsp;·&nbsp;
[**Rapport Word**](reports/report.docx) &nbsp;·&nbsp;
[**Présentation**](reports/presentation.pptx)

</div>

---

##  Présentation du projet

Ce projet vise à **prédire automatiquement le prix de vente d'un véhicule d'occasion** à partir de ses caractéristiques techniques et commerciales, en s'appuyant sur le dataset **CarDekho** — la plus grande plateforme de vente de voitures d'occasion en Inde.

### Problématique

> *Comment estimer de manière fiable le prix de vente d'un véhicule d'occasion à partir de ses caractéristiques, en utilisant des algorithmes de Machine Learning supervisé ?*

### Cas d'usage réel

Un acheteur ou un vendeur saisit les informations d'un véhicule et obtient instantanément une **estimation de prix basée sur 8 128 annonces réelles** du marché indien.

---

##  Application déployée

👉 **[https://estimationprixv-hiculesc34620.streamlit.app/](https://estimationprixv-hiculesc34620.streamlit.app/)**

| Onglet | Fonctionnalité |
|--------|---------------|
| ✏️ **Saisie Manuelle** | Entrer les caractéristiques d'une voiture → prix en ₹ et € instantanément |
| 📂 **Import CSV / Excel** | Importer un fichier multi-véhicules → prédictions en masse + export |
| 📊 **Comparaison Modèles** | Tableau des 4 algorithmes + importance des variables |

---

## 📁 Structure du projet

```
python_estimation/
│
├── 📂 app/                          # Application web Streamlit
│   ├── app.py                       # Code principal — logique et interface
│   └── cardekho_styles.py           # Design CSS — couleurs et mise en page
│
├── 📂 data/
│   ├── raw/                         # Données brutes originales (ne pas modifier)
│   │   └── CAR DETAILS FROM CAR DEKHO.csv
│   └── processed/                   # Données nettoyées prêtes pour la modélisation
│
├── 📂 models/                       # Modèles et artefacts entraînés
│   ├── model_xgb.pkl                # Modèle XGBoost ⭐ meilleur
│   ├── model_rf.pkl                 # Modèle Random Forest
│   ├── model_lr.pkl                 # Modèle Régression Linéaire
│   ├── model_svr.pkl                # Modèle SVR
│   ├── model_best.pkl               # Meilleur modèle (XGBoost) — utilisé par l'app
│   ├── model_metrics.json           # Métriques R², MAE, RMSE de chaque modèle
│   ├── scaler.pkl                   # StandardScaler (variables numériques)
│   ├── scaler_svr.pkl               # StandardScaler dédié SVR
│   ├── label_encoder.pkl            # LabelEncoder (marques)
│   └── columns.pkl                  # Ordre exact des 15 colonnes d'entrée
│
├── 📂 notebooks/                    # Analyse et modélisation (Jupyter)
│   ├── 01_EDA.ipynb                 # Exploration des données
│   ├── 02_preprocessing.ipynb       # Nettoyage et encodage
│   ├── 03_modeling.ipynb            # Entraînement et évaluation
│   └── CarDekho_Projet.ipynb        # Pipeline complet consolidé
│
├── 📂 src/                          # Scripts Python réutilisables
│   ├── data_preprocessing.py        # Fonctions de nettoyage
│   ├── feature_engineering.py       # Création de car_age, extraction marque
│   ├── train_model.py               # Entraînement + GridSearchCV
│   └── evaluate_model.py            # Calcul des métriques
│
├── 📂 reports/                      # Livrables finaux
│   ├── report.docx                  # Rapport Word complet
│   ├── presentation.pptx            # Présentation PowerPoint
│   └── figures/                     # Graphiques générés (PNG)
│
├── requirements.txt                 # Dépendances Python
└── README.md                        # Ce fichier
```

---

## Pipeline Machine Learning — 11 étapes

```
┌─────────────────────────────────────────────────────────────────────┐
│  01  Chargement & EDA          → Exploration, statistiques, graphiques
│  02  Nettoyage                 → Doublons supprimés (763 = 17.6%)
│  03  Valeurs manquantes        → Imputation médiane / mode
│  04  Feature Engineering       → car_age = 2024 − year, brand extraite
│  05  Outliers (IQR)            → 276 valeurs plafonnées (Winsorisation)
│  06  Encodage                  → One-Hot, Ordinal, Label Encoding
│  07  Standardisation           → Z-score + log1p sur la cible
│  08  Split Train / Test        → 80% / 20% — random_state=42
│  09  Modélisation              → 4 algorithmes comparés
│  10  Validation croisée        → K-Fold k=5 + GridSearch / RandomizedSearch
│  11  Déploiement               → Application Streamlit en ligne
└─────────────────────────────────────────────────────────────────────┘
```

---

##  Résultats et performances

### Comparaison des 4 algorithmes

| Modèle | R² Test | MAE (₹) | RMSE (₹) | CV R² | CV Std |
|--------|:-------:|--------:|--------:|:-----:|:------:|
| Régression Linéaire *(baseline)* | 0.613 | 131 500 | 189 400 | 0.664 | ±0.021 |
| Random Forest | 0.691 | 113 100 | 169 400 | 0.735 | ±0.017 |
| **XGBoost**  | **0.723** | **109 300** | **160 400** | **0.752** | **±0.012** |
| SVR (RBF) | 0.580 | 124 500 | 197 300 | 0.656 | ±0.013 |

### Après optimisation des hyperparamètres

| Modèle | R² Test (Tuned) | MAE (₹) | RMSE (₹) |
|--------|:--------------:|--------:|--------:|
| Random Forest (GridSearchCV) | 0.697 | 111 500 | 167 500 |
| **XGBoost (RandomizedSearchCV)** | **0.740** | **107 100** | **155 300** |

###  Meilleur modèle : XGBoost Tuned

```
R² Test = 0.740   →  74% de la variance des prix expliquée
MAE     = 107 100 ₹  →  erreur moyenne ≈ ±1 190 €
RMSE    = 155 300 ₹
CV R²   = 0.771 ± 0.012  →  modèle stable, pas d'overfitting
```

**Hyperparamètres optimaux :**
```
learning_rate = 0.1  |  max_depth = 4  |  n_estimators = 200
subsample = 0.7  |  colsample_bytree = 0.8  |  reg_alpha = 0  |  reg_lambda = 1
```

---

## Importance des variables (XGBoost)

| Rang | Variable | Importance | Interprétation |
|------|----------|:----------:|----------------|
| 1 | `car_age` | 22.2% | L'âge est le 1er facteur de dépréciation (~15-20%/an) |
| 2 | `year` | 17.7% | Corrélé à car_age — voitures récentes valent plus |
| 3 | `fuel_Diesel` | 17.0% | Diesel valorisé pour son efficacité en Inde |
| 4 | `transmission_Automatic` | 13.4% | Automatique = premium (prix moyen +103%) |
| 5 | `seller_type_Individual` | 5.0% | Particulier = prix légèrement plus bas |
| 6 | `brand_encoded` | 4.6% | Marque = indicateur du segment de marché |
| 7 | `km_driven` | 1.7% | Kilométrage = facteur d'usure |

---

## Installation locale

### Prérequis
- Python 3.10 ou supérieur
- Git

### Étapes

```bash
# 1. Cloner le dépôt
git clone https://github.com/MeimouneBabe/Estimation_prix_v-hicules_C34620.git
cd Estimation_prix_v-hicules_C34620

# 2. Créer un environnement virtuel
python -m venv venv

# Activer — Windows
venv\Scripts\activate

# Activer — Linux / macOS
source venv/bin/activate

# 3. Installer les dépendances
pip install -r requirements.txt

# 4. Lancer l'application
streamlit run app/app.py
```

L'application s'ouvre sur **`http://localhost:8501`**

---

##  Dépendances

```
streamlit==1.57.0
pandas==2.2.2
numpy==2.0.2
scikit-learn==1.6.1
xgboost==3.2.0
joblib==1.5.3
openpyxl
```

---

##  Dataset

**Source :** [Vehicle Dataset from CarDekho — Kaggle](https://www.kaggle.com/datasets/nehalbirla/vehicle-dataset-from-cardekho)

| Caractéristique | Valeur |
|----------------|--------|
| Annonces brutes | 4 340 |
| Après nettoyage | 3 577 |
| Doublons supprimés | 763 (17.6%) |
| Variables | 8 brutes → 15 features après encodage |
| Variable cible | `selling_price` (prix en ₹) |

### Variables du dataset

| Variable | Type | Description |
|----------|------|-------------|
| `name` | Textuel | Nom complet (marque + modèle) |
| `year` | Numérique | Année de fabrication |
| `selling_price` | Numérique | **Prix de vente en ₹ — variable cible** |
| `km_driven` | Numérique | Kilométrage total |
| `fuel` | Catégoriel | Petrol / Diesel / CNG / LPG / Electric |
| `seller_type` | Catégoriel | Individual / Dealer / Trustmark Dealer |
| `transmission` | Catégoriel | Manual / Automatic |
| `owner` | Ordinal | 1st / 2nd / 3rd / 4th+ Owner |

### Features créées

| Feature | Formule / Méthode | Justification |
|---------|-------------------|---------------|
| `car_age` | `2024 − year` | Âge = facteur de dépréciation direct |
| `brand_encoded` | Label Encoding | Marque extraite du nom — 29 marques |
| `owner_encoded` | Ordinal (1→5) | Ordre logique : 1er > 2ème > 3ème |
| `fuel_*` | One-Hot Encoding | Variable nominale — pas d'ordre |
| `seller_type_*` | One-Hot Encoding | Variable nominale — pas d'ordre |
| `transmission_*` | One-Hot Encoding | Variable nominale — pas d'ordre |

---

## Format du fichier CSV pour l'import en masse

```csv
name,year,km_driven,fuel,seller_type,transmission,owner
Maruti Swift VXI,2015,50000,Petrol,Individual,Manual,First Owner
Hyundai i20 Asta,2018,30000,Diesel,Dealer,Manual,Second Owner
Toyota Fortuner,2020,20000,Diesel,Dealer,Automatic,First Owner
```

Un fichier exemple est téléchargeable directement depuis l'onglet **Import CSV / Excel** de l'application.

---

## Algorithmes utilisés

### Régression Linéaire — Baseline
Modèle le plus simple. Suppose une relation linéaire entre les features et le prix. Sert de référence minimale : tout algorithme complexe doit le surpasser.

### Random Forest — Ensemble Bagging
200 arbres de décision construits en parallèle sur des sous-échantillons aléatoires. Capture les relations non-linéaires. Robuste aux outliers.

### XGBoost — Gradient Boosting ⭐
Arbres construits séquentiellement — chaque arbre corrige les erreurs du précédent. Régularisation L1/L2 intégrée. Meilleur algorithme pour les données tabulaires.

### SVR — Support Vector Regression
Cherche un hyperplan optimal dans un espace de haute dimension. Très sensible à l'échelle — StandardScaler obligatoire. Limité sur les grands datasets avec forte variance.

---

##  Métriques d'évaluation

| Métrique | Formule | Interprétation |
|----------|---------|----------------|
| **R²** | `1 - SS_res/SS_tot` | % de variance expliquée. 1 = parfait, 0 = inutile |
| **MAE** | `mean(\|y_réel - y_prédit\|)` | Erreur moyenne en ₹ — directement interprétable |
| **RMSE** | `√mean((y_réel - y_prédit)²)` | Pénalise les grosses erreurs — toujours ≥ MAE |

---

## Auteur

| | |
|---|---|
| **Nom** | Meimoune Baba Cheikh Sidiya |
| **Matricule** | C34620 |
| **Cours** | Projet Python — Machine Learning appliqué |
| **Professeur** | Ezyn SEGNANE |
| **Année** | 2024 – 2025 |
| **Application** | [estimationprixv-hiculesc34620.streamlit.app](https://estimationprixv-hiculesc34620.streamlit.app/) |

---

##  Licence

Projet réalisé dans un cadre académique.
Dataset sous licence [CC0 — Domaine public](https://creativecommons.org/publicdomain/zero/1.0/).

---

<div align="center">

*Fait avec ❤️ et Python · CarDekho Dataset · Streamlit Community Cloud*

</div>
