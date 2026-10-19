from flask import Flask, render_template, request, jsonify
import re
from data.curriculum import CURRICULUM, get_curriculum_summary, get_chapters
from data.terminale_spe import TERMINALE_SPE_EXERCISES, get_all_exercises, get_exercise_by_id

app = Flask(__name__)


def normalize_text_answer(ans: str) -> str:
    """Normalise la saisie de l'élève (espaces, virgule décimale, casse)."""
    if not ans:
        return ""
    cleaned = ans.strip().lower()
    cleaned = cleaned.replace(" ", "")
    cleaned = cleaned.replace(",", ".")
    return cleaned


@app.route("/")
def index():
    """Page d'accueil de l'application."""
    return render_template("index.html")


@app.route("/api/curriculum", methods=["GET"])
def api_curriculum():
    """Retourne la hiérarchie complète du lycée (classes, filières, état d'activation)."""
    return jsonify({
        "status": "success",
        "curriculum": get_curriculum_summary()
    })


@app.route("/api/chapters", methods=["GET"])
def api_chapters():
    """Retourne la liste des chapitres pour la filière sélectionnée."""
    stream_id = request.args.get("stream", "spe_maths")
    chapters = get_chapters(stream_id)
    return jsonify({
        "status": "success",
        "stream_id": stream_id,
        "chapters": chapters
    })


@app.route("/api/exercises", methods=["GET"])
def api_exercises():
    """
    Retourne la liste des exercices filtrés par chapitre et difficulté.
    Pour préserver la pédagogie, la réponse correcte et l'explication complète
    sont exclues du flux initial et fournies lors de la validation.
    """
    chapter_id = request.args.get("chapter", "all")
    difficulty = request.args.get("difficulty", None)

    exercises = get_all_exercises(chapter_id, difficulty)

    # Préparation d'une version publique (sans spoiler)
    public_exercises = []
    for ex in exercises:
        public_exercises.append({
            "id": ex["id"],
            "chapter_id": ex["chapter_id"],
            "title": ex["title"],
            "difficulty": ex["difficulty"],
            "type": ex["type"],
            "points": ex.get("points", 10),
            "statement": ex["statement"],
            "hint": ex.get("hint", ""),
            "method": ex.get("method", ""),
            "options": ex.get("options", [])
        })

    return jsonify({
        "status": "success",
        "total": len(public_exercises),
        "exercises": public_exercises
    })


@app.route("/api/check-answer", methods=["POST"])
def api_check_answer():
    """
    Vérifie la réponse envoyée par l'élève, calcule les points et renvoie
    la correction complète avec les explications mathématiques.
    """
    data = request.get_json() or {}
    exercise_id = data.get("exercise_id")
    user_answer = data.get("answer", "")

    exercise = get_exercise_by_id(exercise_id)
    if not exercise:
        return jsonify({"status": "error", "message": "Exercice introuvable"}), 404

    ex_type = exercise.get("type", "qcm")
    is_correct = False
    expected = exercise.get("correct_answer", "")

    if ex_type == "qcm":
        is_correct = (str(user_answer).strip().upper() == str(expected).strip().upper())
    else:
        # Réponse libre / numérique / algébrique
        norm_user = normalize_text_answer(str(user_answer))
        accepted = [normalize_text_answer(a) for a in exercise.get("accepted_answers", [expected])]
        is_correct = (norm_user in accepted) or (norm_user == normalize_text_answer(expected))

    points_earned = exercise.get("points", 10) if is_correct else 0

    return jsonify({
        "status": "success",
        "exercise_id": exercise_id,
        "is_correct": is_correct,
        "points_earned": points_earned,
        "max_points": exercise.get("points", 10),
        "correct_answer": expected,
        "user_answer": user_answer,
        "explanation": exercise.get("explanation", ""),
        "method": exercise.get("method", "")
    })


@app.route("/api/reveal-solution", methods=["POST"])
def api_reveal_solution():
    """Permet à l'élève d'afficher directement la solution en cas de blocage."""
    data = request.get_json() or {}
    exercise_id = data.get("exercise_id")

    exercise = get_exercise_by_id(exercise_id)
    if not exercise:
        return jsonify({"status": "error", "message": "Exercice introuvable"}), 404

    return jsonify({
        "status": "success",
        "exercise_id": exercise_id,
        "correct_answer": exercise.get("correct_answer", ""),
        "explanation": exercise.get("explanation", ""),
        "method": exercise.get("method", "")
    })


@app.route("/api/stats", methods=["GET"])
def api_stats():
    """Retourne les métriques globales du programme Terminale Spé Maths."""
    chapters = get_chapters("spe_maths")
    total_exercises = len(TERMINALE_SPE_EXERCISES)
    by_chapter = {}
    for ch in chapters:
        by_chapter[ch["id"]] = len([e for e in TERMINALE_SPE_EXERCISES if e["chapter_id"] == ch["id"]])

    return jsonify({
        "status": "success",
        "total_exercises": total_exercises,
        "total_chapters": len(chapters),
        "chapters_stats": by_chapter
    })


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)

