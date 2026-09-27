alert("Bienvenue sur AnimeFreak !");

/* Barre de recherche */

/*1)  Récupérer les éléments*/
const searchBar = document.getElementById("SearchBar");
const animeCards = document.querySelectorAll(".anime_card")

/*2)  Détecter quand on tape */
searchBar.addEventListener("input", function () 
	{
	/*3)  Récupérer ce que l'utilisateur a écrit*/
	let recherche =
	searchBar.value.toLowerCase();
		/*4)  Parourir toutes les cartes*/
		animeCards.forEach(function(card)
		{
			/*5)  Récupérer le titre de chaque carte*/
			let titre =
			card.querySelector(".titre_anime").textContent.toLowerCase();
				/*6)  Comparer*/ 
				if (titre.includes(recherche)) {
					card.style.display = "";
				}
				else {
					card.style.display = "none";
				}
		});
	});


/* Favoris */

/*4)  Ajouter un bouton étoile */
const favoriteButtons =
document.querySelectorAll(".favorite-btn");
favoriteButtons.forEach(button => {
	button.addEventListener("click", function () {
		button.classList.toggle("active");
	});
});


/* 5)  Récupérer les favoris sauvegardés*/
let favoris =
JSON.parse(localStorage.getItem("favoris") || "[]");

const boutonsFavoris =
document.querySelectorAll(".favorite-btn");

boutonsFavoris.forEach(button => {
	if
(favoris.includes(button.dataset.anime)) { 
	button.style.color="gold";
}

			button.addEventListener("click",
			function(){
				let anime =
				this.dataset.anime;

			if
	(favoris.includes(anime)) {
				favoris =
			favoris.filter(item => item !== anime);
			this.style.color = "gray";					
			}
			
			else {
				favoris.push(anime);
				this.style.color = "gold";
				}
localStorage.setItem("favoris", JSON.stringify(favoris)
			);
		});
	});

/*function mafonction() {
	alert("Yuji le plus sexy");
}*/