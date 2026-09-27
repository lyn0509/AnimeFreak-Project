// COMPTEUR

const jourSortie = 3; // 0 = dimanche, 1 = lundi, ..., 6 = samedi
const heureSortie = 18;
const minuteSortie = 0;

function mettreAJourCompteur() {
    const maintenant = new Date();

    // On crée la prochaine date de sortie
    const prochaineSortie = new Date(maintenant);

    prochaineSortie.setHours(heureSortie, minuteSortie, 0, 0);

    // Nombre de jours jusqu'au jour de sortie
    let joursJusquaSortie = jourSortie - maintenant.getDay();

    // Si le jour est déjà passé cette semaine,
    // on passe à la semaine suivante
    if (
        joursJusquaSortie < 0 ||
        (joursJusquaSortie === 0 && maintenant >= prochaineSortie)
    ) {
        joursJusquaSortie += 7;
    }

    prochaineSortie.setDate(
        maintenant.getDate() + joursJusquaSortie
    );

    const difference = prochaineSortie - maintenant;

    const jours = Math.floor(
        difference / (1000 * 60 * 60 * 24)
    );

    const heures = Math.floor(
        (difference / (1000 * 60 * 60)) % 24
    );

    const minutes = Math.floor(
        (difference / (1000 * 60)) % 60
    );

    const secondes = Math.floor(
        (difference / 1000) % 60
    );

    document.querySelector("#temps-restant").textContent =
        `${jours} j, ${heures} h, ${minutes} min, ${secondes} s`;
}

mettreAJourCompteur();

setInterval(mettreAJourCompteur, 1000);