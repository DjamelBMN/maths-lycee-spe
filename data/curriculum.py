"""
Structure des programmes de mathématiques du lycée (Post-réforme).
Actuellement activé : Terminale Spécialité Mathématiques.
Prêt pour l'extension future : Première Spé, Seconde Générale, Maths Expertes, Maths Complémentaires, STMG, STI2D.
"""

CURRICULUM = {
    "terminale": {
        "label": "Terminale",
        "description": "Préparation aux épreuves du Baccalauréat et à l'enseignement supérieur.",
        "streams": {
            "spe_maths": {
                "id": "spe_maths",
                "label": "Spécialité Mathématiques",
                "badge": "Épreuve coefficient 16",
                "active": True,
                "description": "Programme officiel conforme au Bulletin Officiel (BO) post-réforme.",
                "chapters": [
                    {
                        "id": "suites_recurrence",
                        "title": "Suites & Raisonnement par récurrence",
                        "theme": "Analyse",
                        "icon": "fa-arrow-trend-up",
                        "summary": "Raisonnement par récurrence, limites finies/infinies, théorèmes de comparaison, convergence des suites monotones.",
                        "keywords": ["Récurrence", "Limites", "Théorème des gendarmes", "Suite géométrique", "Majorant"]
                    },
                    {
                        "id": "continuite_convexite",
                        "title": "Continuité, Dérivation & Convexité",
                        "theme": "Analyse",
                        "icon": "fa-chart-line",
                        "summary": "Théorème des Valeurs Intermédiaires (TVI), bijection, dérivées de composées, convexité, concavité et points d'inflexion.",
                        "keywords": ["TVI", "Bijection", "Dérivée seconde", "Point d'inflexion", "Tangente"]
                    },
                    {
                        "id": "logarithme",
                        "title": "Fonction Logarithme népérien",
                        "theme": "Analyse",
                        "icon": "fa-superscript",
                        "summary": "Définition, propriétés algébriques, limites fondamentales, croissances comparées, dérivée de ln(u).",
                        "keywords": ["ln(x)", "Croissances comparées", "Équations", "ln(u)' = u'/u"]
                    },
                    {
                        "id": "primitives_equa_diff",
                        "title": "Primitives & Équations différentielles",
                        "theme": "Analyse",
                        "icon": "fa-wave-square",
                        "summary": "Calcul de primitives usuelles et composées, équations différentielles y' = ay et y' = ay + b avec condition initiale.",
                        "keywords": ["Primitives", "Équation différentielle", "y' = ay + b", "Problème de Cauchy"]
                    },
                    {
                        "id": "calcul_integral",
                        "title": "Calcul intégral & Intégration par parties",
                        "theme": "Analyse",
                        "icon": "fa-infinity",
                        "summary": "Définition de l'intégrale, théorème fondamental, linéarité, intégration par parties (IPP), calcul d'aires.",
                        "keywords": ["Intégrale", "Intégration par parties", "Aire", "Valeur moyenne"]
                    },
                    {
                        "id": "trigonometrie",
                        "title": "Fonctions trigonométriques",
                        "theme": "Analyse",
                        "icon": "fa-circle-notch",
                        "summary": "Dérivation de sin et cos, étude de fonctions composées, symétries et périodicité.",
                        "keywords": ["cos", "sin", "Périodicité", "Dérivées trigonométriques"]
                    },
                    {
                        "id": "geometrie_espace",
                        "title": "Géométrie dans l'espace",
                        "theme": "Géométrie",
                        "icon": "fa-cube",
                        "summary": "Produit scalaire dans l'espace, équations cartésiennes de plans, représentations paramétriques de droites, orthogonalité.",
                        "keywords": ["Produit scalaire", "Vecteur normal", "Équation de plan", "Représentation paramétrique"]
                    },
                    {
                        "id": "probabilites",
                        "title": "Probabilités & Variables aléatoires",
                        "theme": "Probabilités",
                        "icon": "fa-dice",
                        "summary": "Épreuves de Bernoulli indépendantes, loi binomiale, somme de variables aléatoires, inégalité de Bienaymé-Tchebychev.",
                        "keywords": ["Loi binomiale", "Espérance", "Variance", "Bienaymé-Tchebychev", "Concentration"]
                    }
                ]
            },
            "maths_expertes": {
                "id": "maths_expertes",
                "label": "Option Maths Expertes",
                "badge": "Optionnel (3h)",
                "active": False,
                "description": "Nombres complexes, arithmétique et matrices/graphes. (Prochaine étape après validation de la Spé)",
                "chapters": []
            },
            "maths_comp": {
                "id": "maths_comp",
                "label": "Option Maths Complémentaires",
                "badge": "Optionnel (3h)",
                "active": False,
                "description": "Pour les élèves ayant arrêté la Spé en 1ère. (Prochaine étape)",
                "chapters": []
            }
        }
    },
    "premiere": {
        "label": "Première",
        "description": "Classes de Première Générale et Technologique.",
        "streams": {
            "spe_maths_1ere": {
                "id": "spe_maths_1ere",
                "label": "Spécialité Mathématiques 1ère",
                "badge": "Enseignement de spécialité",
                "active": False,
                "description": "Second degré, dérivation, exponentielle, trigonométrie, probabilités conditionnelles. (À venir)",
                "chapters": []
            }
        }
    },
    "seconde": {
        "label": "Seconde Générale",
        "description": "Classe de Seconde Générale et Technologique.",
        "streams": {
            "tronc_commun": {
                "id": "tronc_commun",
                "label": "Tronc Commun Seconde",
                "badge": "Tronc commun",
                "active": False,
                "description": "Nombres et calculs, fonctions, géométrie, statistiques et probabilités. (À venir)",
                "chapters": []
            }
        }
    }
}


def get_curriculum_summary():
    """Retourne la structure organisée du cursus pour le menu de navigation."""
    summary = []
    for level_key, level_val in CURRICULUM.items():
        streams_list = []
        for stream_key, stream_val in level_val["streams"].items():
            streams_list.append({
                "id": stream_val["id"],
                "label": stream_val["label"],
                "badge": stream_val["badge"],
                "active": stream_val["active"],
                "description": stream_val["description"],
                "chapter_count": len(stream_val["chapters"])
            })
        summary.append({
            "id": level_key,
            "label": level_val["label"],
            "description": level_val["description"],
            "streams": streams_list
        })
    return summary


def get_chapters(stream_id="spe_maths"):
    """Retourne les chapitres d'une filière donnée."""
    for level in CURRICULUM.values():
        if stream_id in level["streams"]:
            return level["streams"][stream_id]["chapters"]
    return []

