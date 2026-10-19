"""
Banque d'exercices de mathématiques pour la classe de Terminale Spécialité Mathématiques.
Conforme aux programmes officiels du Baccalauréat général (réforme du lycée).
"""

TERMINALE_SPE_EXERCISES = [
    # =========================================================================
    # CHAPITRE 1 : SUITES & RAISONNEMENT PAR RÉCURRENCE
    # =========================================================================
    {
        "id": "spe_suite_01",
        "chapter_id": "suites_recurrence",
        "title": "Démontrer une inégalité par récurrence",
        "difficulty": 1,
        "type": "qcm",
        "points": 10,
        "statement": "Soit la suite $(u_n)$ définie par $u_0 = 1$ et pour tout $n \\in \\mathbb{N}$, $u_{n+1} = \\sqrt{2u_n + 3}$.<br>On souhaite prouver par récurrence que pour tout $n \\in \\mathbb{N}$, $0 \\le u_n \\le 3$.<br>Quelle est l'hypothèse de récurrence $\\mathcal{P}(n)$ et l'étape d'hérédité correcte ?",
        "hint": "Pour l'hérédité, appliquez la fonction $f(x) = \\sqrt{2x+3}$ à l'encadrement $0 \\le u_n \\le 3$ en justifiant qu'elle est strictement croissante sur $[0, +\\infty[$.",
        "method": "Principe du raisonnement par récurrence :<br>1. Initialisation : vérifier $\\mathcal{P}(0)$.<br>2. Hérédité : supposer $\\mathcal{P}(n)$ vrai pour un rang $n \\ge 0$ fixé, et démontrer $\\mathcal{P}(n+1)$.<br>3. Conclusion : pour tout $n \\in \\mathbb{N}$, $\\mathcal{P}(n)$ est vraie.",
        "options": [
            {
                "id": "A",
                "text": "L'initialisation donne $u_0=1 \\in [0, 3]$. Par croissance de $x \\mapsto \\sqrt{2x+3}$ sur $[0, 3]$, $0 \\le u_n \\le 3 \\implies \\sqrt{3} \\le u_{n+1} \\le 3$, donc $0 \\le u_{n+1} \\le 3$."
            },
            {
                "id": "B",
                "text": "L'hérédité nécessite de calculer $u_{n+1} - u_n$ pour prouver que la suite est constante égale à 3."
            },
            {
                "id": "C",
                "text": "L'initialisation échoue car $u_0 = 1 \\ne 0$, donc la propriété ne peut pas être prouvée par récurrence."
            },
            {
                "id": "D",
                "text": "Comme $\\sqrt{2u_n+3} \\ge 0$, alors $u_{n+1}$ dépasse obligatoirement 3 dès le rang $n=2$."
            }
        ],
        "correct_answer": "A",
        "explanation": "<strong>Démonstration rigoureuse :</strong><br>1. <strong>Initialisation :</strong> Pour $n = 0$, $u_0 = 1$. On a bien $0 \\le 1 \\le 3$. $\\mathcal{P}(0)$ est donc vraie.<br>2. <strong>Hérédité :</strong> Soit $n \\in \\mathbb{N}$ un entier fixé. Supposons que $0 \\le u_n \\le 3$.<br>Alors $2 \\times 0 + 3 \\le 2u_n + 3 \\le 2 \\times 3 + 3$, soit $3 \\le 2u_n + 3 \\le 9$.<br>La fonction racine carrée étant strictement croissante sur $[0, +\\infty[$, on en déduit :<br>$$\\sqrt{3} \\le \\sqrt{2u_n + 3} \\le \\sqrt{9}$$<br>Comme $\\sqrt{3} \\ge 0$ et $\\sqrt{9} = 3$, il vient : $0 \\le u_{n+1} \\le 3$. L'hérédité est établie.<br>3. <strong>Conclusion :</strong> Par le principe de récurrence, pour tout $n \\in \\mathbb{N}$, $0 \\le u_n \\le 3$."
    },
    {
        "id": "spe_suite_02",
        "chapter_id": "suites_recurrence",
        "title": "Limite par encadrement (Théorème des gendarmes)",
        "difficulty": 2,
        "type": "qcm",
        "points": 15,
        "statement": "Soit la suite $(u_n)$ définie pour tout entier $n \\ge 1$ par :<br>$$u_n = \\frac{3n + (-1)^n \\cos(n)}{2n + 5}$$<br>Quelle est la limite de la suite $(u_n)$ quand $n \\to +\\infty$ ?",
        "hint": "Pour tout réel $x$, $-1 \\le \\cos(x) \\le 1$. Que peut-on dire de $(-1)^n \\cos(n)$ ? Encadrez le numérateur puis factorisez par $n$.",
        "method": "Théorème d'encadrement (dit « des gendarmes ») :<br>Si pour tout $n \\ge n_0$, on a $v_n \\le u_n \\le w_n$ et si $\\lim v_n = \\lim w_n = L$, alors $(u_n)$ converge et $\\lim u_n = L$.",
        "options": [
            {
                "id": "A",
                "text": "La suite n'admet pas de limite en raison de l'oscillation de $(-1)^n \\cos(n)$."
            },
            {
                "id": "B",
                "text": "$\\lim_{n \\to +\\infty} u_n = \\frac{3}{2}$"
            },
            {
                "id": "C",
                "text": "$\\lim_{n \\to +\\infty} u_n = 0$"
            },
            {
                "id": "D",
                "text": "$\\lim_{n \\to +\\infty} u_n = 3$"
            }
        ],
        "correct_answer": "B",
        "explanation": "<strong>Résolution :</strong><br>Pour tout $n \\ge 1$, on a $-1 \\le \\cos(n) \\le 1$, donc $|(-1)^n \\cos(n)| \\le 1$, ce qui implique :<br>$$-1 \\le (-1)^n \\cos(n) \\le 1$$<br>En ajoutant $3n$ :<br>$$3n - 1 \\le 3n + (-1)^n \\cos(n) \\le 3n + 1$$<br>Comme $2n + 5 > 0$ pour tout $n \\ge 1$ :<br>$$\\frac{3n - 1}{2n + 5} \\le u_n \\le \\frac{3n + 1}{2n + 5}$$<br>Or, $\\lim_{n \\to +\\infty} \\frac{3n - 1}{2n + 5} = \\lim_{n \\to +\\infty} \\frac{n(3 - 1/n)}{n(2 + 5/n)} = \\frac{3}{2}$.<br>De même, $\\lim_{n \\to +\\infty} \\frac{3n + 1}{2n + 5} = \\frac{3}{2}$.<br>D'après le <strong>théorème des gendarmes</strong>, la suite $(u_n)$ converge et $\\lim_{n \\to +\\infty} u_n = \\frac{3}{2}$."
    },
    {
        "id": "spe_suite_03",
        "chapter_id": "suites_recurrence",
        "title": "Suite arithmético-géométrique et convergence",
        "difficulty": 2,
        "type": "input",
        "points": 15,
        "statement": "Soit la suite $(u_n)$ définie par $u_0 = 50$ et pour tout $n \\in \\mathbb{N}$ :<br>$$u_{n+1} = 0{,}8 u_n + 60$$<br>On pose pour tout $n \\in \\mathbb{N}$, $v_n = u_n - 300$.<br>Quelle est la valeur de la limite $\\lim_{n \\to +\\infty} u_n$ ? (Entrez un nombre entier)",
        "hint": "Montrez que $(v_n)$ est une suite géométrique de raison $q = 0{,}8$. Quelle est sa limite sachant que $|q| < 1$ ?",
        "method": "Pour une suite arithmético-géométrique $u_{n+1} = a u_n + b$ avec $a \\ne 1$, on résout le point fixe $L = a L + b$, d'où $L = \\frac{b}{1 - a}$.<br>La suite auxiliaire $v_n = u_n - L$ est géométrique de raison $a$.",
        "correct_answer": "300",
        "accepted_answers": ["300", "300.0", "L=300"],
        "explanation": "<strong>Calcul pas à pas :</strong><br>1. Exprimons $v_{n+1}$ en fonction de $v_n$ :<br>$$v_{n+1} = u_{n+1} - 300 = (0{,}8 u_n + 60) - 300 = 0{,}8 u_n - 240 = 0{,}8 (u_n - 300) = 0{,}8 v_n$$<br>2. $(v_n)$ est donc une suite géométrique de raison $q = 0{,}8$ et de premier terme $v_0 = u_0 - 300 = 50 - 300 = -250$.<br>3. Son terme général est $v_n = -250 \\times 0{,}8^n$.<br>4. Comme $-1 < 0{,}8 < 1$, on a $\\lim_{n \\to +\\infty} 0{,}8^n = 0$, donc $\\lim_{n \\to +\\infty} v_n = 0$.<br>5. Puisque $u_n = v_n + 300$, on en déduit par somme :<br>$$\\lim_{n \\to +\\infty} u_n = 300$$"
    },

    # =========================================================================
    # CHAPITRE 2 : CONTINUITÉ, DÉRIVATION & CONVEXITÉ
    # =========================================================================
    {
        "id": "spe_cont_01",
        "chapter_id": "continuite_convexite",
        "title": "Théorème des Valeurs Intermédiaires (TVI)",
        "difficulty": 1,
        "type": "qcm",
        "points": 10,
        "statement": "Soit la fonction $f$ définie sur $\\mathbb{R}$ par $f(x) = x^3 + 3x - 5$.<br>Parmi les affirmations suivantes, laquelle est correcte concernant l'équation $f(x) = 0$ sur l'intervalle $[1, 2]$ ?",
        "hint": "Calculez la dérivée $f'(x)$ pour étudier la stricte monotonie de $f$, puis calculez les images des bornes $f(1)$ et $f(2)$.",
        "method": "Corollaire du TVI (Théorème de la bijection) :<br>Si $f$ est continue et strictement monotone sur $[a, b]$, et si $0$ est compris entre $f(a)$ et $f(b)$ (c'est-à-dire $f(a) \\times f(b) < 0$), alors l'équation $f(x) = 0$ admet une unique solution $\\alpha \\in ]a, b[$.",
        "options": [
            {
                "id": "A",
                "text": "L'équation admet une infinité de solutions car $f$ est une fonction polynomiale de degré 3."
            },
            {
                "id": "B",
                "text": "$f$ est continue, strictement croissante sur $[1, 2]$, avec $f(1) = -1 < 0$ et $f(2) = 9 > 0$, donc l'équation admet une unique solution $\\alpha \\in [1, 2]$."
            },
            {
                "id": "C",
                "text": "L'équation n'admet aucune solution sur $[1, 2]$ car $f'(x) > 0$ partout."
            },
            {
                "id": "D",
                "text": "On ne peut pas conclure car la dérivée seconde s'annule en 0."
            }
        ],
        "correct_answer": "B",
        "explanation": "<strong>Démonstration :</strong><br>1. $f$ est une fonction polynôme, elle est donc dérivable (donc continue) sur $[1, 2]$.<br>2. Pour tout $x \\in [1, 2]$, $f'(x) = 3x^2 + 3$. Or $x^2 \\ge 0$, donc $f'(x) \\ge 3 > 0$. $f$ est strictement croissante sur $[1, 2]$.<br>3. $f(1) = 1^3 + 3(1) - 5 = -1 < 0$ et $f(2) = 2^3 + 3(2) - 5 = 8 + 6 - 5 = 9 > 0$.<br>4. Le nombre 0 est strictement compris entre $f(1)$ et $f(2)$.<br>D'après le <strong>corollaire du théorème des valeurs intermédiaires</strong>, l'équation $f(x) = 0$ possède une unique solution $\\alpha$ dans l'intervalle $[1, 2]$."
    },
    {
        "id": "spe_cont_02",
        "chapter_id": "continuite_convexite",
        "title": "Convexité et point d'inflexion",
        "difficulty": 2,
        "type": "input",
        "points": 15,
        "statement": "Soit la fonction $f$ définie sur $\\mathbb{R}$ par $f(x) = (x^2 - 4x + 2)e^x$.<br>La courbe représentative $\\mathcal{C}_f$ admet un point d'inflexion en un point d'abscisse strictement positive.<br>Quelle est la valeur de cette abscisse ? (Entrez un nombre entier)",
        "hint": "Calculez $f'(x)$ puis $f''(x)$ en factorisant à chaque étape par $e^x$. Cherchez ensuite la valeur positive où $f''(x)$ s'annule en changeant de signe.",
        "method": "Un point $A(x_0, f(x_0))$ est un point d'inflexion de $\\mathcal{C}_f$ si et seulement si la dérivée seconde $f''$ s'annule et change de signe en $x_0$.",
        "correct_answer": "2",
        "accepted_answers": ["2", "x=2", "2.0"],
        "explanation": "<strong>Calcul détaillé :</strong><br>1. <strong>Calcul de la dérivée première $f'(x)$ :</strong><br>On utilise $(uv)' = u'v + uv'$ avec $u(x) = x^2 - 4x + 2 \\implies u'(x) = 2x - 4$ et $v(x) = e^x \\implies v'(x) = e^x$.<br>$$f'(x) = (2x - 4)e^x + (x^2 - 4x + 2)e^x = (x^2 - 2x - 2)e^x$$<br>2. <strong>Calcul de la dérivée seconde $f''(x)$ :</strong><br>On pose $w(x) = x^2 - 2x - 2 \\implies w'(x) = 2x - 2$.<br>$$f''(x) = (2x - 2)e^x + (x^2 - 2x - 2)e^x = (x^2 - 4)e^x = (x - 2)(x + 2)e^x$$<br>3. <strong>Recherche des points d'inflexion :</strong><br>Pour tout réel $x$, $e^x > 0$.<br>Le signe de $f''(x)$ est donc celui de $(x - 2)(x + 2)$, qui s'annule et change de signe en $x = -2$ et en $x = 2$.<br>L'abscisse strictement positive du point d'inflexion est donc <strong>$x = 2$</strong>."
    },
    {
        "id": "spe_cont_03",
        "chapter_id": "continuite_convexite",
        "title": "Dérivée seconde et positions relatives",
        "difficulty": 2,
        "type": "qcm",
        "points": 15,
        "statement": "Soit $g$ une fonction deux fois dérivable sur $[-2, 5]$. On sait que pour tout $x \\in [-2, 5]$, $g''(x) \\ge 0$.<br>Que peut-on en déduire pour la courbe $\\mathcal{C}_g$ et ses tangentes ?",
        "hint": "Reliez le signe de la dérivée seconde à la convexité, puis la convexité à la position de la courbe par rapport à ses tangentes.",
        "method": "Propriété fondamentale de convexité :<br>Une fonction est convexe sur un intervalle $I \\iff f''(x) \\ge 0$ sur $I \\iff$ sa courbe représentative est située <strong>au-dessus</strong> de toutes ses tangentes.",
        "options": [
            {
                "id": "A",
                "text": "$g$ est concave et sa courbe est située au-dessous de toutes ses tangentes."
            },
            {
                "id": "B",
                "text": "$g$ est convexe et sa courbe est située au-dessus de toutes ses tangentes sur $[-2, 5]$."
            },
            {
                "id": "C",
                "text": "$g$ est strictement croissante sur $[-2, 5]$."
            },
            {
                "id": "D",
                "text": "La courbe admet obligatoirement au moins un point d'inflexion sur $[-2, 5]$."
            }
        ],
        "correct_answer": "B",
        "explanation": "<strong>Justification :</strong><br>Par théorème du cours de Terminale :<br>1. Pour une fonction deux fois dérivable sur un intervalle $I$, $g''(x) \\ge 0$ équivaut à dire que $g$ est <strong>convexe</strong> sur $I$ (ce qui signifie aussi que sa dérivée $g'$ est croissante).<br>2. Une fonction convexe a sa courbe représentative entièrement située <strong>au-dessus de chacune de ses tangentes</strong>.<br>Attention : la convexité ne dit rien sur le sens de variation de $g$ (par exemple $x \\mapsto x^2$ est convexe sur $\\mathbb{R}$ mais décroissante puis croissante)."
    },

    # =========================================================================
    # CHAPITRE 3 : FONCTION LOGARITHME NÉPÉRIEN
    # =========================================================================
    {
        "id": "spe_ln_01",
        "chapter_id": "logarithme",
        "title": "Résolution d'inéquation dans le domaine de validité",
        "difficulty": 2,
        "type": "qcm",
        "points": 15,
        "statement": "On considère l'inéquation : $\\ln(2x - 4) \\le \\ln(x + 3)$.<br>Quel est l'ensemble des solutions de cette inéquation dans $\\mathbb{R}$ ?",
        "hint": "N'oubliez jamais de déterminer en premier lieu l'ensemble de définition des expressions : $\\ln(u)$ n'existe que si $u > 0$ !",
        "method": "Méthode pour les équations/inéquations avec $\\ln$ :<br>1. Ensemble de validité $\\mathcal{D}$ : $2x-4 > 0$ ET $x+3 > 0$.<br>2. Par stricte croissance de la fonction logarithme : $\\ln(A) \\le \\ln(B) \\iff A \\le B$.<br>3. Intersection des solutions obtenues avec $\\mathcal{D}$.",
        "options": [
            {
                "id": "A",
                "text": "$S = ]-\\infty, 7]$"
            },
            {
                "id": "B",
                "text": "$S = ]2, 7]$"
            },
            {
                "id": "C",
                "text": "$S = [-3, 7]$"
            },
            {
                "id": "D",
                "text": "$S = [2, 7]$"
            }
        ],
        "correct_answer": "B",
        "explanation": "<strong>Étapes de résolution :</strong><br>1. <strong>Domaine de définition $\\mathcal{D}$ :</strong><br>$2x - 4 > 0 \\iff 2x > 4 \\iff x > 2$<br>$x + 3 > 0 \\iff x > -3$<br>Donc $\\mathcal{D} = ]2, +\\infty[$.<br><br>2. <strong>Résolution sur $\\mathcal{D}$ :</strong><br>Comme la fonction $\\ln$ est strictement croissante sur $]0, +\\infty[$ :<br>$$\\ln(2x - 4) \\le \\ln(x + 3) \\iff 2x - 4 \\le x + 3 \\iff x \\le 7$$<br>3. <strong>Conclusion :</strong><br>En intersectant avec $\\mathcal{D} = ]2, +\\infty[$, on obtient :<br>$$S = ]2, 7]$$<br>Remarque : 2 est exclu car $\\ln(0)$ n'est pas défini !"
    },
    {
        "id": "spe_ln_02",
        "chapter_id": "logarithme",
        "title": "Limite et croissances comparées",
        "difficulty": 2,
        "type": "qcm",
        "points": 15,
        "statement": "Quelle est la limite suivante :<br>$$\\lim_{x \\to +\\infty} \\frac{\\ln(x)}{x^3 + 2x} $$",
        "hint": "Factorisez le dénominateur par $x^3$ et utilisez la limite de cours des croissances comparées : $\\lim_{x \\to +\\infty} \\frac{\\ln x}{x^n} = 0$ pour tout $n \\ge 1$.",
        "method": "Croissances comparées au programme de Terminale :<br>Pour tout entier $n \\ge 1$ :<br>$$\\lim_{x \\to +\\infty} \\frac{\\ln x}{x^n} = 0 \\quad \\text{et} \\quad \\lim_{x \\to 0^+} x^n \\ln x = 0$$",
        "options": [
            {
                "id": "A",
                "text": "$+\\infty$"
            },
            {
                "id": "B",
                "text": "$1$"
            },
            {
                "id": "C",
                "text": "$0$"
            },
            {
                "id": "D",
                "text": "La limite n'existe pas car c'est une forme indéterminée indépassable."
            }
        ],
        "correct_answer": "C",
        "explanation": "<strong>Démonstration :</strong><br>Pour tout $x > 0$ :<br>$$\\frac{\\ln x}{x^3 + 2x} = \\frac{\\ln x}{x^3 \\left(1 + \\frac{2}{x^2}\\right)} = \\frac{1}{1 + \\frac{2}{x^2}} \\times \\frac{\\ln x}{x^3}$$<br>Or d'après le théorème des <strong>croissances comparées</strong> :<br>$$\\lim_{x \\to +\\infty} \\frac{\\ln x}{x^3} = 0$$<br>Et d'autre part :<br>$$\\lim_{x \\to +\\infty} \\left(1 + \\frac{2}{x^2}\\right) = 1 \\implies \\lim_{x \\to +\\infty} \\frac{1}{1 + \\frac{2}{x^2}} = 1$$<br>Par produit de limites :<br>$$\\lim_{x \\to +\\infty} \\frac{\\ln x}{x^3 + 2x} = 1 \\times 0 = 0$$"
    },
    {
        "id": "spe_ln_03",
        "chapter_id": "logarithme",
        "title": "Plus petit entier n (Seuil avec logarithme)",
        "difficulty": 1,
        "type": "input",
        "points": 10,
        "statement": "On cherche le plus petit entier naturel $n$ vérifiant l'inéquation :<br>$$0{,}7^n \\le 0{,}01$$<br>Données : $\\ln(0{,}7) \\approx -0{,}3567$ et $\\ln(0{,}01) \\approx -4{,}6052$.<br>Quelle est la valeur de l'entier $n$ ?",
        "hint": "Appliquez la fonction $\\ln$ aux deux membres. Attention : comme $0{,}7 < 1$, $\\ln(0{,}7) < 0$, donc diviser par $\\ln(0{,}7)$ change le sens de l'inégalité !",
        "method": "Résolution d'inéquation géométrique $q^n \\le k$ avec $0 < q < 1$ :<br>$$\\ln(q^n) \\le \\ln(k) \\iff n \\ln(q) \\le \\ln(k) \\iff n \\ge \\frac{\\ln(k)}{\\ln(q)}$$ car $\\ln(q) < 0$.",
        "correct_answer": "13",
        "accepted_answers": ["13", "n=13"],
        "explanation": "<strong>Calcul :</strong><br>1. Comme $0{,}7^n > 0$ et $0{,}01 > 0$, on applique le logarithme népérien (strictement croissant sur $\\mathbb{R}_+^*$) :<br>$$\\ln(0{,}7^n) \\le \\ln(0{,}01) \\iff n \\ln(0{,}7) \\le \\ln(0{,}01)$$<br>2. Puisque $0{,}7 < 1$, on a $\\ln(0{,}7) < 0$. En divisant par ce nombre négatif, on <strong>change le sens de l'inégalité</strong> :<br>$$n \\ge \\frac{\\ln(0{,}01)}{\\ln(0{,}7)}$$<br>3. Application numérique :<br>$$\\frac{-4{,}6052}{-0{,}3567} \\approx 12{,}91$$<br>Comme $n$ est un entier naturel, le plus petit entier supérieur ou égal à 12,91 est <strong>$n = 13$</strong>."
    },

    # =========================================================================
    # CHAPITRE 4 : PRIMITIVES & ÉQUATIONS DIFFÉRENTIELLES
    # =========================================================================
    {
        "id": "spe_equadiff_01",
        "chapter_id": "primitives_equa_diff",
        "title": "Équation différentielle y' = ay + b avec condition initiale",
        "difficulty": 2,
        "type": "qcm",
        "points": 15,
        "statement": "On considère l'équation différentielle $(E) : y' + 2y = 6$.<br>Quelle est la solution $f$ de cette équation vérifiant la condition initiale $f(0) = 5$ ?",
        "hint": "Écrivez d'abord $(E)$ sous la forme standard $y' = -2y + 6$. Une solution particulière constante est $y_p = -b/a = 6/2 = 3$. Les solutions générales sont $f(x) = C e^{-2x} + 3$. Utilisez ensuite $f(0) = 5$.",
        "method": "Théorème : Les solutions sur $\\mathbb{R}$ de l'équation $y' = ay + b$ (avec $a \\ne 0$) sont les fonctions de la forme :<br>$$f(x) = C e^{ax} - \\frac{b}{a}, \\quad C \\in \\mathbb{R}$$",
        "options": [
            {
                "id": "A",
                "text": "$f(x) = 2e^{-2x} + 3$"
            },
            {
                "id": "B",
                "text": "$f(x) = 5e^{2x} + 6$"
            },
            {
                "id": "C",
                "text": "$f(x) = 3e^{-2x} + 2$"
            },
            {
                "id": "D",
                "text": "$f(x) = 2e^{2x} + 3$"
            }
        ],
        "correct_answer": "A",
        "explanation": "<strong>Résolution complète :</strong><br>1. On réécrit l'équation sous la forme canonique :<br>$$y' = -2y + 6$$<br>Ici $a = -2$ et $b = 6$.<br>2. Une solution particulière constante est :<br>$$y_0 = -\\frac{b}{a} = -\\frac{6}{-2} = 3$$<br>3. L'ensemble des solutions sur $\\mathbb{R}$ est donné par :<br>$$f(x) = C e^{-2x} + 3, \\quad \\text{avec } C \\in \\mathbb{R}$$<br>4. Détermination de la constante $C$ avec $f(0) = 5$ :<br>$$f(0) = C e^0 + 3 = C + 3 = 5 \\implies C = 2$$<br>La solution unique est donc <strong>$f(x) = 2e^{-2x} + 3$</strong>."
    },
    {
        "id": "spe_equadiff_02",
        "chapter_id": "primitives_equa_diff",
        "title": "Primitive de la forme u'/u",
        "difficulty": 1,
        "type": "qcm",
        "points": 10,
        "statement": "Soit la fonction $f$ définie sur $]1, +\\infty[$ par :<br>$$f(x) = \\frac{2x - 3}{x^2 - 3x + 5}$$<br>Quelle est une primitive $F$ de $f$ sur $]1, +\\infty[$ ?",
        "hint": "Remarquez que le numérateur est exactement la dérivée du dénominateur : $(x^2 - 3x + 5)' = 2x - 3$.",
        "method": "Reconnaissance de formes usuelles :<br>Si $u(x) > 0$, la fonction $\\frac{u'(x)}{u(x)}$ admet pour primitive $\\ln(u(x)) + k$.",
        "options": [
            {
                "id": "A",
                "text": "$F(x) = (2x - 3) \\ln(x^2 - 3x + 5)$"
            },
            {
                "id": "B",
                "text": "$F(x) = \\ln(x^2 - 3x + 5)$"
            },
            {
                "id": "C",
                "text": "$F(x) = \\frac{1}{x^2 - 3x + 5}$"
            },
            {
                "id": "D",
                "text": "$F(x) = e^{x^2 - 3x + 5}$"
            }
        ],
        "correct_answer": "B",
        "explanation": "<strong>Démonstration :</strong><br>Posons $u(x) = x^2 - 3x + 5$.<br>Le discriminant de ce trinôme est $\\Delta = (-3)^2 - 4(1)(5) = 9 - 20 = -11 < 0$. Comme le coefficient de $x^2$ est $1 > 0$, pour tout réel $x$, $u(x) > 0$.<br>La dérivée est $u'(x) = 2x - 3$.<br>Ainsi, la fonction s'écrit sous la forme exacte :<br>$$f(x) = \\frac{u'(x)}{u(x)}$$<br>Une primitive sur $]1, +\\infty[$ est donc :<br>$$F(x) = \\ln(|u(x)|) = \\ln(x^2 - 3x + 5)$$"
    },

    # =========================================================================
    # CHAPITRE 5 : CALCUL INTÉGRAL & INTÉGRATION PAR PARTIES
    # =========================================================================
    {
        "id": "spe_integ_01",
        "chapter_id": "calcul_integral",
        "title": "Intégration par parties (IPP)",
        "difficulty": 3,
        "type": "qcm",
        "points": 20,
        "statement": "On souhaite calculer l'intégrale suivante à l'aide d'une intégration par parties :<br>$$I = \\int_1^e x \\ln(x) \\, dx$$<br>Quelle est la valeur exacte de $I$ ?",
        "hint": "Posez $u'(x) = x$ et $v(x) = \\ln(x)$. Trouvez $u(x)$ et $v'(x)$, puis appliquez la formule $[uv]_1^e - \\int_1^e u v'$.",
        "method": "Formule d'intégration par parties :<br>Si $u$ et $v$ sont deux fonctions de classe $\\mathcal{C}^1$ sur $[a, b]$ :<br>$$\\int_a^b u'(x)v(x)dx = [u(x)v(x)]_a^b - \\int_a^b u(x)v'(x)dx$$",
        "options": [
            {
                "id": "A",
                "text": "$I = \\frac{e^2 + 1}{4}$"
            },
            {
                "id": "B",
                "text": "$I = \\frac{e^2 - 1}{2}$"
            },
            {
                "id": "C",
                "text": "$I = \\frac{e^2}{2}$"
            },
            {
                "id": "D",
                "text": "$I = \\frac{3e^2 - 1}{4}$"
            }
        ],
        "correct_answer": "A",
        "explanation": "<strong>Calcul détaillé de l'IPP :</strong><br>On pose :<br>$\\begin{cases} u'(x) = x \\implies u(x) = \\frac{x^2}{2} \\\\ v(x) = \\ln(x) \\implies v'(x) = \\frac{1}{x} \\end{cases}$<br>Les fonctions $u$ et $v$ sont continûment dérivables sur $[1, e]$.<br>Par la formule d'intégration par parties :<br>$$I = \\left[ \\frac{x^2}{2} \\ln(x) \\right]_1^e - \\int_1^e \\frac{x^2}{2} \\times \\frac{1}{x} \\, dx$$<br>1. Calcul du crochet :<br>$$\\left[ \\frac{x^2}{2} \\ln(x) \\right]_1^e = \\left( \\frac{e^2}{2} \\ln(e) \\right) - \\left( \\frac{1^2}{2} \\ln(1) \\right) = \\frac{e^2}{2} \\times 1 - 0 = \\frac{e^2}{2}$$<br>2. Calcul de la seconde intégrale :<br>$$\\int_1^e \\frac{x}{2} \\, dx = \\left[ \\frac{x^2}{4} \\right]_1^e = \\frac{e^2}{4} - \\frac{1}{4}$$<br>3. Synthèse :<br>$$I = \\frac{e^2}{2} - \\left( \\frac{e^2}{4} - \\frac{1}{4} \\right) = \\frac{2e^2 - e^2 + 1}{4} = \\frac{e^2 + 1}{4}$$"
    },
    {
        "id": "spe_integ_02",
        "chapter_id": "calcul_integral",
        "title": "Calcul d'aire entre deux courbes",
        "difficulty": 2,
        "type": "qcm",
        "points": 15,
        "statement": "Soient les fonctions $f(x) = e^x$ et $g(x) = x$ définies sur $[0, 1]$.<br>Quelle est l'aire en unités d'aire (u.a.) du domaine délimité par les courbes $\\mathcal{C}_f$, $\\mathcal{C}_g$ et les droites verticales $x = 0$ et $x = 1$ ?",
        "hint": "Vérifiez que pour tout $x \\in [0, 1]$, $e^x \\ge x$. L'aire est alors $\\int_0^1 (f(x) - g(x)) dx$.",
        "method": "Aire entre deux courbes :<br>Si pour tout $x \\in [a, b]$, $f(x) \\ge g(x)$, alors l'aire du domaine situé entre les deux courbes est :<br>$$\\mathcal{A} = \\int_a^b (f(x) - g(x)) \\, dx \\quad (\\text{en u.a.})$$",
        "options": [
            {
                "id": "A",
                "text": "$\\mathcal{A} = e - \\frac{3}{2}$"
            },
            {
                "id": "B",
                "text": "$\\mathcal{A} = e - 1$"
            },
            {
                "id": "C",
                "text": "$\\mathcal{A} = e - 2$"
            },
            {
                "id": "D",
                "text": "$\\mathcal{A} = \\frac{e - 1}{2}$"
            }
        ],
        "correct_answer": "A",
        "explanation": "<strong>Résolution :</strong><br>1. Sur $[0, 1]$, on sait que la fonction exponentielle est convexe et au-dessus de sa tangente en 0 ($y = x + 1 > x$), donc $e^x > x$.<br>2. L'aire vaut donc :<br>$$\\mathcal{A} = \\int_0^1 (e^x - x) \\, dx$$<br>3. Une primitive de $e^x - x$ sur $\\mathbb{R}$ est $F(x) = e^x - \\frac{x^2}{2}$.<br>4. On applique le théorème fondamental :<br>$$\\mathcal{A} = F(1) - F(0) = \\left( e^1 - \\frac{1^2}{2} \\right) - \\left( e^0 - \\frac{0^2}{2} \\right) = \\left( e - \\frac{1}{2} \\right) - (1 - 0) = e - \\frac{3}{2}$$"
    },
    {
        "id": "spe_integ_03",
        "chapter_id": "calcul_integral",
        "title": "Valeur moyenne d'une fonction continue",
        "difficulty": 1,
        "type": "input",
        "points": 10,
        "statement": "Soit la fonction $f$ définie sur $[0, 2]$ par $f(x) = 3x^2$.<br>Quelle est la <strong>valeur moyenne</strong> $\\mu$ de la fonction $f$ sur l'intervalle $[0, 2]$ ? (Entrez un nombre entier)",
        "hint": "Appliquez la formule de la valeur moyenne $\\mu = \\frac{1}{b - a} \\int_a^b f(x) \\, dx$. Une primitive de $3x^2$ est $x^3$.",
        "method": "Valeur moyenne d'une fonction continue sur $[a, b]$ :<br>$$\\mu = \\frac{1}{b - a} \\int_a^b f(t) \\, dt$$",
        "correct_answer": "4",
        "accepted_answers": ["4", "4.0", "mu=4"],
        "explanation": "<strong>Calcul pas à pas :</strong><br>1. D'après la formule du cours, la valeur moyenne sur $[0, 2]$ est :<br>$$\\mu = \\frac{1}{2 - 0} \\int_0^2 3x^2 \\, dx = \\frac{1}{2} \\int_0^2 3x^2 \\, dx$$<br>2. Une primitive de $x \\mapsto 3x^2$ est $F(x) = x^3$.<br>3. On évalue entre les bornes :<br>$$\\int_0^2 3x^2 \\, dx = [x^3]_0^2 = 2^3 - 0^3 = 8$$<br>4. Ainsi :<br>$$\\mu = \\frac{1}{2} \\times 8 = 4$$"
    },

    # =========================================================================
    # CHAPITRE 6 : FONCTIONS TRIGONOMÉTRIQUES
    # =========================================================================
    {
        "id": "spe_trigo_01",
        "chapter_id": "trigonometrie",
        "title": "Dérivée d'une fonction trigonométrique composée",
        "difficulty": 2,
        "type": "qcm",
        "points": 15,
        "statement": "Soit la fonction $f$ définie sur $\\mathbb{R}$ par $f(x) = \\cos^2(3x)$.<br>Quelle est l'expression de sa fonction dérivée $f'(x)$ ?",
        "hint": "Utilisez la formule de dérivation d'une puissance $(u^2)' = 2 u' u$, avec $u(x) = \\cos(3x)$. Rappel : $(\\cos(3x))' = -3 \\sin(3x)$. On peut ensuite utiliser $2\\sin(a)\\cos(a) = \\sin(2a)$.",
        "method": "Formule de dérivation de composées :<br>$(g(u(x)))' = u'(x) \\times g'(u(x))$.<br>En particulier, pour $(u^n)' = n u' u^{n-1}$ et $(\\cos(ax+b))' = -a \\sin(ax+b)$.",
        "options": [
            {
                "id": "A",
                "text": "$f'(x) = -6 \\sin(3x) \\cos(3x) = -3 \\sin(6x)$"
            },
            {
                "id": "B",
                "text": "$f'(x) = 2 \\cos(3x) \\sin(3x)$"
            },
            {
                "id": "C",
                "text": "$f'(x) = -3 \\sin^2(3x)$"
            },
            {
                "id": "D",
                "text": "$f'(x) = 6 \\sin(6x)$"
            }
        ],
        "correct_answer": "A",
        "explanation": "<strong>Calcul :</strong><br>Posons $u(x) = \\cos(3x)$.<br>Alors $f(x) = (u(x))^2$.<br>La dérivée est $f'(x) = 2 u'(x) u(x)$.<br>Or $u'(x) = -3 \\sin(3x)$.<br>Donc :<br>$$f'(x) = 2 (-3 \\sin(3x)) \\cos(3x) = -6 \\sin(3x) \\cos(3x)$$<br>En utilisant la formule de duplication trigonométrique $2 \\sin(\\theta) \\cos(\\theta) = \\sin(2\\theta)$ avec $\\theta = 3x$ :<br>$$f'(x) = -3 \\times (2 \\sin(3x) \\cos(3x)) = -3 \\sin(6x)$$"
    },
    {
        "id": "spe_trigo_02",
        "chapter_id": "trigonometrie",
        "title": "Valeur maximale d'une fonction sinusoïdale",
        "difficulty": 1,
        "type": "input",
        "points": 10,
        "statement": "Soit la fonction $g$ définie sur $\\mathbb{R}$ par $g(x) = 4 \\cos(2x) + 1$.<br>Quelle est la <strong>valeur maximale</strong> atteinte par $g(x)$ sur $\\mathbb{R}$ ? (Entrez un nombre entier)",
        "hint": "Pour tout réel $X$, $-1 \\le \\cos(X) \\le 1$. Quelle est la valeur maximale que peut prendre $\\cos(2x)$ ?",
        "method": "Encadrement trigonométrique classique :<br>Pour tout réel $x$, $-1 \\le \\cos(\\omega x + \\varphi) \\le 1$. Le maximum de $A \\cos(\\omega x) + B$ avec $A > 0$ est atteint quand le cosinus vaut 1.",
        "correct_answer": "5",
        "accepted_answers": ["5", "5.0", "max=5"],
        "explanation": "<strong>Justification :</strong><br>1. Pour tout réel $x$, la fonction cosinus est bornée :<br>$$-1 \\le \\cos(2x) \\le 1$$<br>2. En multipliant par $4 > 0$ :<br>$$-4 \\le 4\\cos(2x) \\le 4$$<br>3. En ajoutant 1 :<br>$$-3 \\le 4\\cos(2x) + 1 \\le 5$$<br>4. Pour $x = 0$, $\\cos(2 \\times 0) = \\cos(0) = 1$, donc $g(0) = 4(1) + 1 = 5$.<br>La valeur maximale atteinte est bien <strong>5</strong>."
    },

    # =========================================================================
    # CHAPITRE 7 : GÉOMÉTRIE DANS L'ESPACE
    # =========================================================================
    {
        "id": "spe_geom_01",
        "chapter_id": "geometrie_espace",
        "title": "Équation cartésienne d'un plan et vecteur normal",
        "difficulty": 1,
        "type": "qcm",
        "points": 10,
        "statement": "Dans un repère orthonormé $(O; \\vec{i}, \\vec{j}, \\vec{k})$, on considère le point $A(2, -1, 3)$ et le vecteur $\\vec{n}\\begin{pmatrix} 3 \\\\ -2 \\\\ 1 \\end{pmatrix}$.<br>Quelle est l'équation cartésienne du plan $\\mathcal{P}$ passant par $A$ et orthogonal au vecteur $\\vec{n}$ ?",
        "hint": "Un point $M(x, y, z)$ appartient au plan si et seulement si $\\vec{AM} \\cdot \\vec{n} = 0$, soit $a(x - x_A) + b(y - y_A) + c(z - z_A) = 0$.",
        "method": "Plan orthogonal à un vecteur normal $\\vec{n}(a, b, c)$ :<br>L'équation est de la forme $ax + by + cz + d = 0$. On détermine la constante $d$ en injectant les coordonnées du point $A$ : $a x_A + b y_A + c z_A + d = 0$.",
        "options": [
            {
                "id": "A",
                "text": "$3x - 2y + z - 11 = 0$"
            },
            {
                "id": "B",
                "text": "$3x - 2y + z + 11 = 0$"
            },
            {
                "id": "C",
                "text": "$2x - y + 3z - 14 = 0$"
            },
            {
                "id": "D",
                "text": "$3x - 2y + z = 0$"
            }
        ],
        "correct_answer": "A",
        "explanation": "<strong>Résolution :</strong><br>Comme $\\vec{n}(3, -2, 1)$ est un vecteur normal au plan $\\mathcal{P}$, l'équation s'écrit :<br>$$3x - 2y + z + d = 0$$<br>Comme le point $A(2, -1, 3)$ appartient au plan $\\mathcal{P}$, ses coordonnées vérifient cette équation :<br>$$3(2) - 2(-1) + (3) + d = 0 \\iff 6 + 2 + 3 + d = 0 \\iff 11 + d = 0 \\iff d = -11$$<br>L'équation cartésienne de $\\mathcal{P}$ est donc :<br>$$3x - 2y + z - 11 = 0$$"
    },
    {
        "id": "spe_geom_02",
        "chapter_id": "geometrie_espace",
        "title": "Intersection d'une droite et d'un plan",
        "difficulty": 2,
        "type": "qcm",
        "points": 15,
        "statement": "On considère le plan $\\mathcal{P}$ d'équation $2x - y + 3z - 4 = 0$ et la droite $\\mathcal{D}$ ayant pour représentation paramétrique :<br>$$\\begin{cases} x = 1 + 2t \\\\ y = 3 - t \\\\ z = -1 + t \\end{cases} \\quad (t \\in \\mathbb{R})$$<br>Quelles sont les coordonnées du point d'intersection $H$ de la droite $\\mathcal{D}$ et du plan $\\mathcal{P}$ ?",
        "hint": "Substituez $x(t), y(t), z(t)$ dans l'équation du plan $\\mathcal{P}$ pour déterminer la valeur du paramètre $t$, puis réinjectez $t$ dans le système.",
        "method": "Méthode d'intersection droite-plan :<br>1. Remplacer $x, y, z$ par leurs expressions en fonction de $t$ dans l'équation cartésienne.<br>2. Résoudre l'équation du premier degré en $t$.<br>3. Calculer les coordonnées du point $H(x(t), y(t), z(t))$.",
        "options": [
            {
                "id": "A",
                "text": "$H(3, 2, 0)$ correspondant à $t = 1$"
            },
            {
                "id": "B",
                "text": "$H(1, 3, -1)$ correspondant à $t = 0$"
            },
            {
                "id": "C",
                "text": "$H(5, 1, 1)$ correspondant à $t = 2$"
            },
            {
                "id": "D",
                "text": "La droite $\\mathcal{D}$ est strictement parallèle au plan $\\mathcal{P}$, pas d'intersection."
            }
        ],
        "correct_answer": "A",
        "explanation": "<strong>Calcul :</strong><br>Injectons les coordonnées paramétriques de $\\mathcal{D}$ dans l'équation de $\\mathcal{P}$ :<br>$$2(1 + 2t) - (3 - t) + 3(-1 + t) - 4 = 0$$<br>$$2 + 4t - 3 + t - 3 + 3t - 4 = 0$$<br>$$(4t + t + 3t) + (2 - 3 - 3 - 4) = 0$$<br>$$8t - 8 = 0 \\iff 8t = 8 \\iff t = 1$$<br>Remplaçons $t = 1$ dans la représentation paramétrique de $\\mathcal{D}$ :<br>$$\\begin{cases} x = 1 + 2(1) = 3 \\\\ y = 3 - 1 = 2 \\\\ z = -1 + 1 = 0 \\end{cases}$$<br>Le point d'intersection est bien <strong>$H(3, 2, 0)$</strong>.<br>Vérification dans le plan : $2(3) - 2 + 3(0) - 4 = 6 - 2 - 4 = 0$."
    },
    {
        "id": "spe_geom_03",
        "chapter_id": "geometrie_espace",
        "title": "Produit scalaire et orthogonalité de deux vecteurs",
        "difficulty": 1,
        "type": "input",
        "points": 10,
        "statement": "Dans un repère orthonormé $(O; \\vec{i}, \\vec{j}, \\vec{k})$, on considère les vecteurs $\\vec{u}\\begin{pmatrix} 2 \\\\ m \\\\ -3 \\end{pmatrix}$ et $\\vec{v}\\begin{pmatrix} 3 \\\\ 2 \\\\ 4 \\end{pmatrix}$ où $m \\in \\mathbb{R}$.<br>Pour quelle valeur du réel $m$ les vecteurs $\\vec{u}$ et $\\vec{v}$ sont-ils <strong>orthogonaux</strong> ? (Entrez un nombre entier)",
        "hint": "Deux vecteurs sont orthogonaux si et seulement si leur produit scalaire est nul : $\\vec{u} \\cdot \\vec{v} = x x' + y y' + z z' = 0$.",
        "method": "Expression analytique du produit scalaire dans l'espace :<br>Dans un repère orthonormé, $\\vec{u}(x, y, z) \\cdot \\vec{v}(x', y', z') = xx' + yy' + zz'$.<br>$\\vec{u} \\perp \\vec{v} \\iff \\vec{u} \\cdot \\vec{v} = 0$.",
        "correct_answer": "3",
        "accepted_answers": ["3", "3.0", "m=3"],
        "explanation": "<strong>Calcul du produit scalaire :</strong><br>Dans un repère orthonormé :<br>$$\\vec{u} \\cdot \\vec{v} = 2 \\times 3 + m \\times 2 + (-3) \\times 4 = 6 + 2m - 12 = 2m - 6$$<br>Les deux vecteurs sont orthogonaux si et seulement si :<br>$$\\vec{u} \\cdot \\vec{v} = 0 \\iff 2m - 6 = 0 \\iff 2m = 6 \\iff m = 3$$"
    },

    # =========================================================================
    # CHAPITRE 8 : PROBABILITÉS & VARIABLES ALÉATOIRES
    # =========================================================================
    {
        "id": "spe_proba_01",
        "chapter_id": "probabilites",
        "title": "Loi binomiale et probabilité au moins un succès",
        "difficulty": 1,
        "type": "qcm",
        "points": 10,
        "statement": "Un contrôle qualité teste un composant électronique. La probabilité qu'un composant soit défectueux est $p = 0{,}05$. On prélève au hasard et avec remise un lot de 20 composants.<br>Soit $X$ la variable aléatoire dénombrant les composants défectueux du lot.<br>Quelle est l'expression de la probabilité d'avoir <strong>au moins un composant défectueux</strong> $P(X \\ge 1)$ ?",
        "hint": "Pensez à l'événement contraire ! L'événement contraire de « au moins un défectueux » est « aucun défectueux », soit $X = 0$.",
        "method": "Propriété de l'événement contraire :<br>Pour une loi binomiale $X \\sim \\mathcal{B}(n, p)$ :<br>$$P(X \\ge 1) = 1 - P(X = 0) = 1 - \\binom{n}{0} p^0 (1-p)^n = 1 - (1-p)^n$$",
        "options": [
            {
                "id": "A",
                "text": "$P(X \\ge 1) = 1 - 0{,}95^{20} \\approx 0{,}642$"
            },
            {
                "id": "B",
                "text": "$P(X \\ge 1) = 20 \\times 0{,}05 \\times 0{,}95^{19}$"
            },
            {
                "id": "C",
                "text": "$P(X \\ge 1) = 1 - 0{,}05^{20}$"
            },
            {
                "id": "D",
                "text": "$P(X \\ge 1) = 0{,}05 \\times 20 = 1$"
            }
        ],
        "correct_answer": "A",
        "explanation": "<strong>Raisonnement :</strong><br>1. On répète $n = 20$ fois de manière identique et indépendante une épreuve de Bernoulli de succès « composant défectueux » avec $p = 0{,}05$.<br>La variable $X$ suit donc la <strong>loi binomiale $\\mathcal{B}(20; 0{,}05)$</strong>.<br>2. On cherche $P(X \\ge 1)$.<br>L'événement contraire de $(X \\ge 1)$ est $(X = 0)$ : aucun composant n'est défectueux.<br>3. $P(X = 0) = \\binom{20}{0} \\times 0{,}05^0 \\times (1 - 0{,}05)^{20} = 1 \\times 1 \\times 0{,}95^{20}$.<br>4. Ainsi :<br>$$P(X \\ge 1) = 1 - P(X = 0) = 1 - 0{,}95^{20} \\approx 1 - 0{,}3585 = 0{,}6415$$"
    },
    {
        "id": "spe_proba_02",
        "chapter_id": "probabilites",
        "title": "Somme de variables indépendantes et variance",
        "difficulty": 2,
        "type": "input",
        "points": 15,
        "statement": "Soient $X_1, X_2, \\dots, X_{16}$ seize variables aléatoires mutuellement indépendantes suivant la même loi de probabilité, d'espérance $E(X_i) = 10$ et de variance $V(X_i) = 4$.<br>On pose la variable aléatoire moyenne :<br>$$M_{16} = \\frac{1}{16} \\sum_{i=1}^{16} X_i$$<br>Quelle est la valeur exacte de la variance $V(M_{16})$ ? (Entrez un nombre décimal sous la forme 0.25 par exemple)",
        "hint": "Rappels sur les propriétés de la variance : $V(aX) = a^2 V(X)$ et pour des variables indépendantes, $V(X_1 + \\dots + X_n) = V(X_1) + \\dots + V(X_n)$.",
        "method": "Propriétés pour $n$ variables indépendantes et identiquement distribuées :<br>$$V(S_n) = n V(X) \\quad \\text{et} \\quad V(M_n) = V\\left(\\frac{S_n}{n}\\right) = \\frac{1}{n^2} V(S_n) = \\frac{V(X)}{n}$$",
        "correct_answer": "0.25",
        "accepted_answers": ["0.25", "0,25", "1/4"],
        "explanation": "<strong>Calcul :</strong><br>1. Soit $S_{16} = \\sum_{i=1}^{16} X_i$. Comme les variables sont indépendantes, la variance de leur somme est la somme des variances :<br>$$V(S_{16}) = \\sum_{i=1}^{16} V(X_i) = 16 \\times 4 = 64$$<br>2. On sait que pour toute variable aléatoire $Y$ et tout réel $a$ :<br>$$V(a Y) = a^2 V(Y)$$<br>3. Ici, $M_{16} = \\frac{1}{16} S_{16}$, donc :<br>$$V(M_{16}) = \\left(\\frac{1}{16}\\right)^2 V(S_{16}) = \\frac{1}{256} \\times 64 = \\frac{64}{256} = \\frac{1}{4} = 0{,}25$$"
    },
    {
        "id": "spe_proba_03",
        "chapter_id": "probabilites",
        "title": "Inégalité de Bienaymé-Tchebychev",
        "difficulty": 2,
        "type": "qcm",
        "points": 15,
        "statement": "Soit $Y$ une variable aléatoire d'espérance $\\mu = 50$ et d'écart-type $\\sigma = 4$ (soit une variance $V(Y) = 16$).<br>D'après l'inégalité de Bienaymé-Tchebychev, quelle majoration peut-on donner à la probabilité :<br>$$P(|Y - 50| \\ge 8) \\; ?$$",
        "hint": "L'inégalité s'écrit $P(|Y - E(Y)| \\ge a) \\le \\frac{V(Y)}{a^2}$ avec $a = 8$.",
        "method": "Inégalité de Bienaymé-Tchebychev au programme de Terminale :<br>Pour toute variable aléatoire admettant une espérance $E(Y)$ et une variance $V(Y)$, et pour tout réel $a > 0$ :<br>$$P(|Y - E(Y)| \\ge a) \\le \\frac{V(Y)}{a^2}$$",
        "options": [
            {
                "id": "A",
                "text": "$P(|Y - 50| \\ge 8) \\le \\frac{16}{64} = 0{,}25$"
            },
            {
                "id": "B",
                "text": "$P(|Y - 50| \\ge 8) \\le \\frac{4}{8} = 0{,}5$"
            },
            {
                "id": "C",
                "text": "$P(|Y - 50| \\ge 8) \\le \\frac{16}{8} = 2$"
            },
            {
                "id": "D",
                "text": "$P(|Y - 50| \\ge 8) \\ge 0{,}75$"
            }
        ],
        "correct_answer": "A",
        "explanation": "<strong>Application du cours :</strong><br>1. On identifie les paramètres :<br>$E(Y) = 50$, $V(Y) = \\sigma^2 = 4^2 = 16$ et $a = 8$.<br>2. On applique la formule de l'inégalité de Bienaymé-Tchebychev :<br>$$P(|Y - 50| \\ge 8) \\le \\frac{V(Y)}{8^2} = \\frac{16}{64} = \\frac{1}{4} = 0{,}25$$<br>Cela signifie qu'il y a au maximum 25 % de chances que $Y$ s'écarte de sa moyenne de 8 unités ou plus."
    }
]


def get_all_exercises(chapter_id=None, difficulty=None):
    """Retourne la liste filtrée des exercices."""
    result = TERMINALE_SPE_EXERCISES
    if chapter_id and chapter_id != "all":
        result = [ex for ex in result if ex["chapter_id"] == chapter_id]
    if difficulty:
        try:
            diff_int = int(difficulty)
            result = [ex for ex in result if ex["difficulty"] == diff_int]
        except ValueError:
            pass
    return result


def get_exercise_by_id(exercise_id):
    """Retourne un exercice par son identifiant unique."""
    for ex in TERMINALE_SPE_EXERCISES:
        if ex["id"] == exercise_id:
            return ex
    return None
