const questions = document.querySelectorAll(".question");
const boutonValider = document.querySelector("#valider-quiz");
const resultat = document.querySelector("#resultat");

let score = 0;

// Permet de sélectionner une seule réponse par question
questions.forEach(question => {

    const reponses = question.querySelectorAll(".reponse");

    reponses.forEach(reponse => {

        reponse.addEventListener("click", function() {

            // Enlève la sélection précédente
            reponses.forEach(r => {
                r.classList.remove("selectionnee");
            });

            // Sélectionne la réponse cliquée
            this.classList.add("selectionnee");
        });

    });

});


// Vérification du quiz
boutonValider.addEventListener("click", function() {

    score = 0;

    questions.forEach(question => {

        const reponses = question.querySelectorAll(".reponse");

        reponses.forEach(reponse => {

            reponse.classList.remove("correcte");
            reponse.classList.remove("fausse");

            // Affiche la bonne réponse
            if (reponse.dataset.correct === "true") {
                reponse.classList.add("correcte");
            }

            // Vérifie la réponse choisie
            if (
                reponse.classList.contains("selectionnee") &&
                reponse.dataset.correct === "false"
            ) {
                reponse.classList.add("fausse");
            }

            if (
                reponse.classList.contains("selectionnee") &&
                reponse.dataset.correct === "true"
            ) {
                score++;
            }

        });

    });

    resultat.textContent =
        `Tu as obtenu ${score} / ${questions.length} !`;
        
    const toutesLesReponses = document.querySelectorAll(".reponse");

toutesLesReponses.forEach(reponse => {
    reponse.disabled = true;
});
});