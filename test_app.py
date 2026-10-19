import unittest
import json
from app import app
from data.curriculum import CURRICULUM, get_chapters, get_curriculum_summary
from data.terminale_spe import TERMINALE_SPE_EXERCISES, get_all_exercises, get_exercise_by_id


class TestMathsLyceeApp(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_homepage(self):
        """Vérifie que la page d'accueil se charge avec succès."""
        res = self.app.get("/")
        self.assertEqual(res.status_code, 200)
        self.assertIn(b"Maths", res.data)
        self.assertIn(b"Terminale Sp", res.data)

    def test_curriculum_api(self):
        """Vérifie l'API de structure du cursus."""
        res = self.app.get("/api/curriculum")
        self.assertEqual(res.status_code, 200)
        data = json.loads(res.data)
        self.assertEqual(data["status"], "success")
        self.assertTrue(len(data["curriculum"]) >= 3)  # Terminale, Première, Seconde

        # Vérifier que Terminale Spé Maths est bien active
        terminale = next(c for c in data["curriculum"] if c["id"] == "terminale")
        spe_maths = next(s for s in terminale["streams"] if s["id"] == "spe_maths")
        self.assertTrue(spe_maths["active"])
        self.assertGreaterEqual(spe_maths["chapter_count"], 8)

    def test_chapters_api(self):
        """Vérifie que tous les chapitres officiels de Spé Maths sont retournés."""
        res = self.app.get("/api/chapters?stream=spe_maths")
        self.assertEqual(res.status_code, 200)
        data = json.loads(res.data)
        self.assertEqual(data["status"], "success")
        chapter_ids = [c["id"] for c in data["chapters"]]
        expected = [
            "suites_recurrence",
            "continuite_convexite",
            "logarithme",
            "primitives_equa_diff",
            "calcul_integral",
            "trigonometrie",
            "geometrie_espace",
            "probabilites"
        ]
        for exp in expected:
            self.assertIn(exp, chapter_ids)

    def test_exercises_api_all(self):
        """Vérifie le chargement de l'ensemble des exercices."""
        res = self.app.get("/api/exercises?chapter=all")
        self.assertEqual(res.status_code, 200)
        data = json.loads(res.data)
        self.assertEqual(data["status"], "success")
        self.assertGreaterEqual(data["total"], 8)

        # Vérifier qu'aucune réponse n'est spoilée dans l'API publique
        for ex in data["exercises"]:
            self.assertNotIn("correct_answer", ex)
            self.assertNotIn("explanation", ex)

    def test_exercises_filter_by_chapter(self):
        """Vérifie le filtrage par chapitre."""
        res = self.app.get("/api/exercises?chapter=suites_recurrence")
        self.assertEqual(res.status_code, 200)
        data = json.loads(res.data)
        for ex in data["exercises"]:
            self.assertEqual(ex["chapter_id"], "suites_recurrence")

    def test_check_answer_qcm_correct_and_incorrect(self):
        """Vérifie la validation des réponses QCM."""
        ex = next(e for e in TERMINALE_SPE_EXERCISES if e["type"] == "qcm")
        correct_ans = ex["correct_answer"]
        wrong_ans = "B" if correct_ans != "B" else "C"

        # Bonne réponse
        res_ok = self.app.post("/api/check-answer", json={
            "exercise_id": ex["id"],
            "answer": correct_ans
        })
        self.assertEqual(res_ok.status_code, 200)
        data_ok = json.loads(res_ok.data)
        self.assertTrue(data_ok["is_correct"])
        self.assertEqual(data_ok["points_earned"], ex.get("points", 10))
        self.assertIn("explanation", data_ok)

        # Mauvaise réponse
        res_ko = self.app.post("/api/check-answer", json={
            "exercise_id": ex["id"],
            "answer": wrong_ans
        })
        self.assertEqual(res_ko.status_code, 200)
        data_ko = json.loads(res_ko.data)
        self.assertFalse(data_ko["is_correct"])
        self.assertEqual(data_ko["points_earned"], 0)

    def test_check_answer_numeric_input(self):
        """Vérifie la validation des réponses numériques (virgules, espaces)."""
        ex = next(e for e in TERMINALE_SPE_EXERCISES if e["type"] == "input")
        correct_ans = ex["correct_answer"]

        # Test réponse exacte
        res = self.app.post("/api/check-answer", json={
            "exercise_id": ex["id"],
            "answer": f" {correct_ans} "
        })
        data = json.loads(res.data)
        self.assertTrue(data["is_correct"])

    def test_reveal_solution(self):
        """Vérifie la route pour afficher la solution."""
        ex = TERMINALE_SPE_EXERCISES[0]
        res = self.app.post("/api/reveal-solution", json={
            "exercise_id": ex["id"]
        })
        self.assertEqual(res.status_code, 200)
        data = json.loads(res.data)
        self.assertEqual(data["status"], "success")
        self.assertEqual(data["correct_answer"], ex["correct_answer"])
        self.assertEqual(data["explanation"], ex["explanation"])


if __name__ == "__main__":
    unittest.main()

