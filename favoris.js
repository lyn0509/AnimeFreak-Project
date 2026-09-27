/* 6) Afficher les favoris */

const listeFavoris = document.querySelector("#liste_favoris");

if (listeFavoris) {

    let favoris =
    JSON.parse(localStorage.getItem("favoris") || "[]");

    favoris.forEach(anime => {

        const nomAnime = document.createElement("p");

        nomAnime.textContent = anime;

        listeFavoris.appendChild(nomAnime);
    });
}