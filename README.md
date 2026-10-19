# Plateforme d'Entraînement en Mathématiques — Lycée (Post-Réforme)

Application web interactive (Frontend **HTML5 / CSS3 / JavaScript** + Backend **Python Flask**) conçue pour permettre aux lycéens de s'entraîner en mathématiques selon les programmes officiels du Ministère de l'Éducation Nationale (réforme du Baccalauréat).

[![Deploy to Render](https://render.com/images/deploy-to-render-button.svg)](https://render.com/deploy?repo=https://github.com/DjamelBMN/maths-lycee-spe)
[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https://github.com/DjamelBMN/maths-lycee-spe)

Phase actuelle : **Terminale Spécialité Mathématiques** (Épreuve écrite coefficient 16).  
*Une fois cette phase validée, les autres filières et niveaux (Première Spécialité, Seconde Générale, Maths Expertes, Maths Complémentaires, STMG/STI2D) seront débloqués via l'architecture modulaire existante.*

---

## 🎯 Fonctionnalités Clés

1. **Programme Officiel de Terminale Spécialité Mathématiques** :
   - **Suites & Récurrence** : raisonnement par récurrence, limites, théorèmes de comparaison et théorème des gendarmes, suites arithmético-géométriques.
   - **Continuité, Dérivation & Convexité** : TVI et corollaire de bijection, dérivées de composées, convexité, concavité et points d'inflexion ($f''$).
   - **Fonction Logarithme népérien** : propriétés algébriques, limites fondamentales, croissances comparées, dérivée de $\ln(u)$.
   - **Primitives & Équations différentielles** : recherche de primitives, équations $y' = ay$ et $y' = ay + b$ avec problème de Cauchy.
   - **Calcul intégral & Intégration par parties** : relation de Chasles, théorème fondamental, formule d'IPP, calcul d'aires entre courbes, valeur moyenne.
   - **Fonctions trigonométriques** : dérivation de fonctions composées avec $\cos$ et $\sin$, parité, périodicité, encadrement.
   - **Géométrie dans l'espace** : produit scalaire dans l'espace, orthogonalité, équation cartésienne de plan, représentation paramétrique de droite, intersections.
   - **Probabilités & Variables aléatoires** : loi binomiale $\mathcal{B}(n, p)$, somme de variables indépendantes, inégalité de Bienaymé-Tchebychev.

2. **Moteur Mathématique & Pédagogique** :
   - **Rendu LaTeX parfait** via **KaTeX** (équations aérées, fractions, intégrales, vecteurs, matrices).
   - **Double niveau d'aide** :
     - 💡 *Besoin d'un indice ?* (débloque une piste de recherche sans dévoiler le résultat).
     - 📘 *Rappel de cours & Méthode* (synthèse du théorème clé du programme officiel).
   - **Correction détaillée pas à pas** avec démonstrations rigoureuses et justifications attendues au Baccalauréat.
   - **Modes de questions variés** : QCM interactifs et saisie libre (nombres entiers, décimaux, fractions).
   - **Suivi de la progression** en local (points gagnés, exercices réussis, taux de réussite) sauvegardé automatiquement.

3. **Architecture Évolutive** :
   - Fichier de configuration [`data/curriculum.py`](file:///C:/Users/nanod/.gemini/antigravity/scratch/maths-lycee-app/data/curriculum.py) structurant tout le cursus du lycée.
   - Banque de questions modulaire prête à accueillir `data/premiere_spe.py`, `data/seconde.py`, etc.

---

## 🚀 Démarrage Rapide

### 1. Activer l'espace de travail
Nous vous recommandons d'ouvrir ce dossier comme espace de travail actif :
```text
C:\Users\nanod\.gemini\antigravity\scratch\maths-lycee-app
```

### 2. Installer les dépendances
```bash
pip install -r requirements.txt
```

### 3. Lancer l'application Flask
```bash
python app.py
```
L'application sera accessible dans votre navigateur à l'adresse :  
👉 **`http://127.0.0.1:5000`**

### 4. Lancer les tests unitaires
```bash
python test_app.py
```

---

## 📂 Structure du Projet

```text
maths-lycee-app/
├── app.py                     # Serveur Flask et API REST (/api/exercises, /api/check-answer...)
├── requirements.txt           # Dépendances Python (Flask)
├── test_app.py                # Tests unitaires automatisés
├── data/
│   ├── __init__.py
│   ├── curriculum.py          # Structure générale du lycée et état des filières
│   └── terminale_spe.py       # Banque d'exercices conformes au BO Terminale Spé
├── static/
│   ├── css/
│   │   └── style.css          # Design moderne, responsive et adapté aux formules KaTeX
│   └── js/
│       └── app.js             # Moteur interactif (validation, rendu KaTeX, scores)
└── templates/
    └── index.html             # Interface utilisateur monopage (SPA)
```

