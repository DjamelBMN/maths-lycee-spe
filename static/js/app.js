/**
 * Application d'entraînement aux Mathématiques du Lycée
 * Conforme au programme de Terminale Spécialité Mathématiques (Post-réforme)
 */

document.addEventListener("DOMContentLoaded", () => {
    // État de l'application
    const state = {
        chapters: [],
        exercises: [],
        currentChapter: "all",
        currentDifficulty: "all",
        currentIndex: 0,
        selectedAnswer: null,
        isAnswerSubmitted: false,
        stats: {
            attempted: 0,
            correct: 0,
            points: 0,
            completedIds: new Set()
        }
    };

    // Éléments DOM
    const chaptersListContainer = document.getElementById("chaptersListContainer");
    const currentChapterHeading = document.getElementById("currentChapterHeading");
    const currentChapterSub = document.getElementById("currentChapterSub");
    const totalChaptersBadge = document.getElementById("totalChaptersBadge");

    const exerciseCard = document.getElementById("exerciseCard");
    const emptyState = document.getElementById("emptyState");
    const exChapterBadge = document.getElementById("exChapterBadge");
    const exDiffBadge = document.getElementById("exDiffBadge");
    const exPointsBadge = document.getElementById("exPointsBadge");
    const exPagination = document.getElementById("exPagination");
    const exTitle = document.getElementById("exTitle");
    const exStatement = document.getElementById("exStatement");
    const dynamicInputZone = document.getElementById("dynamicInputZone");

    const hintAccordion = document.getElementById("hintAccordion");
    const btnToggleHint = document.getElementById("btnToggleHint");
    const hintText = document.getElementById("hintText");

    const methodAccordion = document.getElementById("methodAccordion");
    const btnToggleMethod = document.getElementById("btnToggleMethod");
    const methodText = document.getElementById("methodText");

    const feedbackBanner = document.getElementById("feedbackBanner");
    const feedbackHeader = document.getElementById("feedbackHeader");
    const feedbackIcon = document.getElementById("feedbackIcon");
    const feedbackTitle = document.getElementById("feedbackTitle");
    const feedbackExplanation = document.getElementById("feedbackExplanation");

    const btnCheckAnswer = document.getElementById("btnCheckAnswer");
    const btnRevealSolution = document.getElementById("btnRevealSolution");
    const btnNextExercise = document.getElementById("btnNextExercise");

    const statsCorrect = document.getElementById("statsCorrect");
    const statsPoints = document.getElementById("statsPoints");
    const statsRate = document.getElementById("statsRate");
    const btnResetProgress = document.getElementById("btnResetProgress");

    // Modal éléments
    const curriculumModal = document.getElementById("curriculumModal");
    const btnOpenCurriculumModal = document.getElementById("btnOpenCurriculumModal");
    const btnCloseCurriculumModal = document.getElementById("btnCloseCurriculumModal");
    const btnCloseCurriculumModal2 = document.getElementById("btnCloseCurriculumModal2");
    const curriculumTreeContainer = document.getElementById("curriculumTreeContainer");

    // Responsive menu
    const menuToggle = document.getElementById("menuToggle");
    const sidebar = document.getElementById("sidebar");

    // -------------------------------------------------------------------------
    // KaTeX Helper
    // -------------------------------------------------------------------------
    function triggerKaTeX(element = document.body) {
        if (window.renderMathInElement) {
            window.renderMathInElement(element, {
                delimiters: [
                    { left: "$$", right: "$$", display: true },
                    { left: "$", right: "$", display: false },
                    { left: "\\(", right: "\\)", display: false },
                    { left: "\\[", right: "\\]", display: true }
                ],
                throwOnError: false
            });
        }
    }

    // -------------------------------------------------------------------------
    // Initialisation & Chargement des données
    // -------------------------------------------------------------------------
    loadSavedStats();
    fetchChapters();
    fetchExercises();

    // -------------------------------------------------------------------------
    // Gestion des stats (localStorage)
    // -------------------------------------------------------------------------
    function loadSavedStats() {
        try {
            const saved = localStorage.getItem("maths_spe_stats");
            if (saved) {
                const parsed = JSON.parse(saved);
                state.stats.attempted = parsed.attempted || 0;
                state.stats.correct = parsed.correct || 0;
                state.stats.points = parsed.points || 0;
                state.stats.completedIds = new Set(parsed.completedIds || []);
            }
        } catch (e) {
            console.error("Erreur lecture stats:", e);
        }
        updateStatsUI();
    }

    function saveStats() {
        try {
            const dataToSave = {
                attempted: state.stats.attempted,
                correct: state.stats.correct,
                points: state.stats.points,
                completedIds: Array.from(state.stats.completedIds)
            };
            localStorage.setItem("maths_spe_stats", JSON.stringify(dataToSave));
        } catch (e) {
            console.error("Erreur sauvegarde stats:", e);
        }
        updateStatsUI();
    }

    function updateStatsUI() {
        statsCorrect.textContent = state.stats.correct;
        statsPoints.textContent = state.stats.points;
        const rate = state.stats.attempted > 0 
            ? Math.round((state.stats.correct / state.stats.attempted) * 100) 
            : 0;
        statsRate.textContent = `${rate}%`;
    }

    btnResetProgress.addEventListener("click", () => {
        if (confirm("Voulez-vous réinitialiser votre progression et vos points ?")) {
            state.stats = { attempted: 0, correct: 0, points: 0, completedIds: new Set() };
            saveStats();
        }
    });

    // -------------------------------------------------------------------------
    // Chapitres (API)
    // -------------------------------------------------------------------------
    async function fetchChapters() {
        try {
            const res = await fetch("/api/chapters?stream=spe_maths");
            const data = await res.json();
            if (data.status === "success") {
                state.chapters = data.chapters;
                totalChaptersBadge.textContent = data.chapters.length;
                renderChaptersMenu();
            }
        } catch (err) {
            console.error("Erreur chargement chapitres:", err);
        }
    }

    function renderChaptersMenu() {
        chaptersListContainer.innerHTML = "";
        state.chapters.forEach(ch => {
            const btn = document.createElement("button");
            btn.className = "chapter-item";
            btn.dataset.chapter = ch.id;

            const iconClass = ch.icon || "fa-book-open";
            btn.innerHTML = `
                <div class="chapter-icon"><i class="fa-solid ${iconClass}"></i></div>
                <div class="chapter-text">
                    <span class="chapter-title">${ch.title}</span>
                    <span class="chapter-meta">${ch.theme}</span>
                </div>
            `;

            btn.addEventListener("click", () => {
                document.querySelectorAll(".chapter-item").forEach(b => b.classList.remove("active"));
                btn.classList.add("active");
                state.currentChapter = ch.id;
                state.currentIndex = 0;
                currentChapterHeading.textContent = ch.title;
                currentChapterSub.textContent = ch.summary;
                if (window.innerWidth <= 900) {
                    sidebar.classList.remove("open");
                }
                fetchExercises();
            });

            chaptersListContainer.appendChild(btn);
        });

        // Gestion du bouton "Tous les chapitres"
        const allBtn = document.querySelector('.chapter-item[data-chapter="all"]');
        if (allBtn) {
            allBtn.addEventListener("click", () => {
                document.querySelectorAll(".chapter-item").forEach(b => b.classList.remove("active"));
                allBtn.classList.add("active");
                state.currentChapter = "all";
                state.currentIndex = 0;
                currentChapterHeading.textContent = "Tous les chapitres";
                currentChapterSub.textContent = "Terminale Spécialité Mathématiques — Conforme aux épreuves du Bac";
                if (window.innerWidth <= 900) {
                    sidebar.classList.remove("open");
                }
                fetchExercises();
            });
        }
    }

    // -------------------------------------------------------------------------
    // Filtres de difficulté
    // -------------------------------------------------------------------------
    const diffButtons = document.querySelectorAll("#difficultyFilters .filter-pill");
    diffButtons.forEach(btn => {
        btn.addEventListener("click", () => {
            diffButtons.forEach(b => b.classList.remove("active"));
            btn.classList.add("active");
            state.currentDifficulty = btn.dataset.diff;
            state.currentIndex = 0;
            fetchExercises();
        });
    });

    const btnResetFilters = document.getElementById("btnResetFilters");
    if (btnResetFilters) {
        btnResetFilters.addEventListener("click", () => {
            state.currentChapter = "all";
            state.currentDifficulty = "all";
            document.querySelectorAll(".chapter-item").forEach(b => b.classList.remove("active"));
            document.querySelector('.chapter-item[data-chapter="all"]').classList.add("active");
            diffButtons.forEach(b => b.classList.remove("active"));
            document.querySelector('#difficultyFilters [data-diff="all"]').classList.add("active");
            fetchExercises();
        });
    }

    // -------------------------------------------------------------------------
    // Chargement des Exercices (API)
    // -------------------------------------------------------------------------
    async function fetchExercises() {
        let url = `/api/exercises?chapter=${state.currentChapter}`;
        if (state.currentDifficulty && state.currentDifficulty !== "all") {
            url += `&difficulty=${state.currentDifficulty}`;
        }

        try {
            const res = await fetch(url);
            const data = await res.json();
            if (data.status === "success") {
                state.exercises = data.exercises;
                if (state.currentIndex >= state.exercises.length) {
                    state.currentIndex = 0;
                }
                renderCurrentExercise();
            }
        } catch (err) {
            console.error("Erreur chargement exercices:", err);
        }
    }

    // -------------------------------------------------------------------------
    // Affichage de l'Exercice Courant
    // -------------------------------------------------------------------------
    function renderCurrentExercise() {
        if (!state.exercises || state.exercises.length === 0) {
            exerciseCard.classList.add("hidden");
            emptyState.classList.remove("hidden");
            return;
        }

        exerciseCard.classList.remove("hidden");
        emptyState.classList.add("hidden");

        const ex = state.exercises[state.currentIndex];
        state.selectedAnswer = null;
        state.isAnswerSubmitted = false;

        // Pagination
        exPagination.textContent = `Exercice ${state.currentIndex + 1} sur ${state.exercises.length}`;

        // Titre & Enoncé
        exTitle.textContent = ex.title;
        exStatement.innerHTML = ex.statement;

        // Badges
        const chapterObj = state.chapters.find(c => c.id === ex.chapter_id);
        exChapterBadge.textContent = chapterObj ? chapterObj.title : "Spé Maths";

        exDiffBadge.className = "badge-diff";
        if (ex.difficulty === 1) {
            exDiffBadge.classList.add("level-1");
            exDiffBadge.textContent = "🟢 Niveau 1 : Socle";
        } else if (ex.difficulty === 2) {
            exDiffBadge.classList.add("level-2");
            exDiffBadge.textContent = "🟡 Niveau 2 : Entraînement";
        } else {
            exDiffBadge.classList.add("level-3");
            exDiffBadge.textContent = "🔴 Niveau 3 : Type Bac";
        }

        exPointsBadge.innerHTML = `<i class="fa-solid fa-award"></i> ${ex.points} pts`;

        // Indice & Méthode
        hintAccordion.classList.remove("open");
        hintText.innerHTML = ex.hint || "Aucun indice disponible pour cet exercice.";

        methodAccordion.classList.remove("open");
        methodText.innerHTML = ex.method || "Rappel de méthode standard pour le Bac.";

        // Feedback
        feedbackBanner.className = "feedback-banner hidden";
        feedbackExplanation.innerHTML = "";

        // Boutons
        btnCheckAnswer.disabled = true;
        btnCheckAnswer.classList.remove("hidden");
        btnNextExercise.classList.add("hidden");
        btnRevealSolution.disabled = false;

        // Construction de la zone de réponse (QCM ou Input libre)
        renderAnswerZone(ex);

        // Typeset Math avec KaTeX
        setTimeout(() => triggerKaTeX(exerciseCard), 50);
    }

    function renderAnswerZone(ex) {
        dynamicInputZone.innerHTML = "";

        if (ex.type === "qcm") {
            const list = document.createElement("div");
            list.className = "qcm-options-list";

            ex.options.forEach(opt => {
                const card = document.createElement("div");
                card.className = "qcm-option-card";
                card.dataset.optionId = opt.id;

                card.innerHTML = `
                    <div class="option-badge">${opt.id}</div>
                    <div class="option-text">${opt.text}</div>
                `;

                card.addEventListener("click", () => {
                    if (state.isAnswerSubmitted) return;
                    document.querySelectorAll(".qcm-option-card").forEach(c => c.classList.remove("selected"));
                    card.classList.add("selected");
                    state.selectedAnswer = opt.id;
                    btnCheckAnswer.disabled = false;
                });

                list.appendChild(card);
            });

            dynamicInputZone.appendChild(list);
        } else {
            // Saisie libre / numérique
            const box = document.createElement("div");
            box.className = "input-answer-box";
            box.innerHTML = `
                <div class="input-row">
                    <input type="text" class="math-input" id="freeAnswerInput" placeholder="Ex: 2, 0.25, 300..." autocomplete="off">
                </div>
                <span class="input-hint-text"><i class="fa-solid fa-info-circle"></i> Saisissez un entier ou une valeur décimale exacte.</span>
            `;

            dynamicInputZone.appendChild(box);

            const inputElem = document.getElementById("freeAnswerInput");
            inputElem.addEventListener("input", (e) => {
                state.selectedAnswer = e.target.value.trim();
                btnCheckAnswer.disabled = state.selectedAnswer.length === 0;
            });

            inputElem.addEventListener("keydown", (e) => {
                if (e.key === "Enter" && !btnCheckAnswer.disabled && !state.isAnswerSubmitted) {
                    btnCheckAnswer.click();
                }
            });

            inputElem.focus();
        }
    }

    // Accordions Toggle
    btnToggleHint.addEventListener("click", () => {
        hintAccordion.classList.toggle("open");
        if (hintAccordion.classList.contains("open")) {
            setTimeout(() => triggerKaTeX(hintContent), 30);
        }
    });

    btnToggleMethod.addEventListener("click", () => {
        methodAccordion.classList.toggle("open");
        if (methodAccordion.classList.contains("open")) {
            setTimeout(() => triggerKaTeX(methodContent), 30);
        }
    });

    // -------------------------------------------------------------------------
    // Validation de la réponse
    // -------------------------------------------------------------------------
    btnCheckAnswer.addEventListener("click", async () => {
        if (!state.selectedAnswer || state.isAnswerSubmitted) return;

        const currentEx = state.exercises[state.currentIndex];
        btnCheckAnswer.disabled = true;

        try {
            const res = await fetch("/api/check-answer", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({
                    exercise_id: currentEx.id,
                    answer: state.selectedAnswer
                })
            });

            const result = await res.json();
            if (result.status === "success") {
                state.isAnswerSubmitted = true;
                handleVerificationResult(result);
            }
        } catch (err) {
            console.error("Erreur vérification:", err);
            btnCheckAnswer.disabled = false;
        }
    });

    function handleVerificationResult(result) {
        state.stats.attempted++;

        // Mise à jour visuelle des options QCM
        if (document.querySelectorAll(".qcm-option-card").length > 0) {
            document.querySelectorAll(".qcm-option-card").forEach(card => {
                card.classList.add("disabled");
                const optId = card.dataset.optionId;
                if (optId === result.correct_answer) {
                    card.classList.add("is-correct");
                } else if (optId === result.user_answer && !result.is_correct) {
                    card.classList.add("is-wrong");
                }
            });
        }

        // Affichage du bandeau de feedback
        feedbackBanner.classList.remove("hidden");
        if (result.is_correct) {
            feedbackBanner.className = "feedback-banner success";
            feedbackIcon.className = "feedback-icon fa-solid fa-circle-check";
            feedbackTitle.textContent = `Excellent ! Réponse exacte (+${result.points_earned} points)`;
            
            if (!state.stats.completedIds.has(result.exercise_id)) {
                state.stats.correct++;
                state.stats.points += result.points_earned;
                state.stats.completedIds.add(result.exercise_id);
            }
        } else {
            feedbackBanner.className = "feedback-banner error";
            feedbackIcon.className = "feedback-icon fa-solid fa-circle-xmark";
            feedbackTitle.textContent = `Ce n'est pas tout à fait ça. Réponse attendue : ${result.correct_answer}`;
        }

        feedbackExplanation.innerHTML = `
            <div style="margin-bottom: 8px;"><strong>Explication mathématique détaillée :</strong></div>
            ${result.explanation}
        `;

        saveStats();

        // Réorganisation des boutons
        btnCheckAnswer.classList.add("hidden");
        btnNextExercise.classList.remove("hidden");

        setTimeout(() => triggerKaTeX(feedbackExplanation), 50);
    }

    // -------------------------------------------------------------------------
    // Révéler la solution directement
    // -------------------------------------------------------------------------
    btnRevealSolution.addEventListener("click", async () => {
        const currentEx = state.exercises[state.currentIndex];
        try {
            const res = await fetch("/api/reveal-solution", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ exercise_id: currentEx.id })
            });
            const result = await res.json();
            if (result.status === "success") {
                state.isAnswerSubmitted = true;
                btnCheckAnswer.classList.add("hidden");
                btnNextExercise.classList.remove("hidden");

                // Mettre en évidence la bonne option
                document.querySelectorAll(".qcm-option-card").forEach(card => {
                    card.classList.add("disabled");
                    if (card.dataset.optionId === result.correct_answer) {
                        card.classList.add("is-correct");
                    }
                });

                feedbackBanner.className = "feedback-banner error";
                feedbackIcon.className = "feedback-icon fa-solid fa-lightbulb";
                feedbackTitle.textContent = `Solution complète (Réponse : ${result.correct_answer})`;
                feedbackExplanation.innerHTML = result.explanation;
                feedbackBanner.classList.remove("hidden");

                setTimeout(() => triggerKaTeX(feedbackExplanation), 50);
            }
        } catch (err) {
            console.error("Erreur reveal:", err);
        }
    });

    // -------------------------------------------------------------------------
    // Navigation : Exercice suivant
    // -------------------------------------------------------------------------
    btnNextExercise.addEventListener("click", () => {
        if (state.currentIndex < state.exercises.length - 1) {
            state.currentIndex++;
        } else {
            state.currentIndex = 0; // Boucle au début
        }
        renderCurrentExercise();
    });

    // -------------------------------------------------------------------------
    // Modal Curriculum Lycée (Roadmap)
    // -------------------------------------------------------------------------
    btnOpenCurriculumModal.addEventListener("click", async () => {
        curriculumModal.classList.remove("hidden");
        try {
            const res = await fetch("/api/curriculum");
            const data = await res.json();
            if (data.status === "success") {
                renderCurriculumTree(data.curriculum);
            }
        } catch (err) {
            console.error("Erreur curriculum modal:", err);
        }
    });

    function renderCurriculumTree(curriculum) {
        curriculumTreeContainer.innerHTML = "";
        curriculum.forEach(level => {
            const card = document.createElement("div");
            card.className = "level-card";

            let streamsHTML = "";
            level.streams.forEach(st => {
                const isActive = st.active;
                streamsHTML += `
                    <div class="stream-item ${isActive ? 'active-stream' : ''}">
                        <div class="stream-meta">
                            <h5>${st.label} ${isActive ? '<i class="fa-solid fa-circle-check text-blue"></i>' : ''}</h5>
                            <p>${st.description}</p>
                        </div>
                        <span class="stream-tag ${isActive ? 'active' : 'pending'}">
                            ${isActive ? 'Actif (Spécialité)' : 'Prochaine étape'}
                        </span>
                    </div>
                `;
            });

            card.innerHTML = `
                <div class="level-title">
                    <i class="fa-solid fa-graduation-cap"></i> ${level.label}
                </div>
                ${streamsHTML}
            `;

            curriculumTreeContainer.appendChild(card);
        });
    }

    btnCloseCurriculumModal.addEventListener("click", () => curriculumModal.classList.add("hidden"));
    btnCloseCurriculumModal2.addEventListener("click", () => curriculumModal.classList.add("hidden"));
    curriculumModal.addEventListener("click", (e) => {
        if (e.target === curriculumModal) curriculumModal.classList.add("hidden");
    });

    // Mobile Toggle
    if (menuToggle) {
        menuToggle.addEventListener("click", () => {
            sidebar.classList.toggle("open");
        });
    }
});

