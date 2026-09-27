#========================================================================================================

#----------------------------------AnimeFreak : Animes recommandations-----------------------------------

#========================================================================================================

animes_par_genre = {
    "1": {"nom" : "Action / Aventure / Combats",
        "animes" : ["Jujutsu Kaisen", "Hunter X Hunter", "Demon Slayer", "Ousama Ranking",
                    "Tokyo Revengers", "Dororo", "Hell's Paradise", "Gachiakuta", "Dandadan", "ZOM 100"]
          },
    "2": {
        "nom" : "Psychologie / Dark / Surnaturel",
        "animes" : ["Shingeki no kyojin", "The Promised Neverland", "Mushishi", "Death Note",
                    "Chainsaw Man", "Tatami Galaxy", "Tomodachi Game", "Takopi's original sin",
                    "Bunny girl senpai", "Oshi no ko", "Tengoku daimakyo" "Devilman Crybaby",
                    "The summer Hikaru died", "Elfen lied", "Angel Beats", "Needy girl overdose"
                    , "Kiznaiver", "Beastars", "Death Parade"]
        },

    "3": {
        "nom" : "Romance",
        "animes" : ["Raeliana", "Garçon d'à côté", "Sign of affection", "Criminelles fiançailles"
                    , "A girl and her guard dog", "Maid-sama", "Nana", "Paradise Kiss", "Nana",
                    "Tomo-chan is a girl", "Horimiya", "Tamon's B-side", "Ton visage au clair de lune",
                    "Toumei otoko and ningen onna", "Dark moon", "You and I are polar opposite",
                    "Kaguya-sama love is war", "The fragant flower blooms with dignity",
                    "Your lie in april", "Yuri on ice", "Gambare Nakamura-kun !!", "Ao haru ride",
                    "Given", "Hana-Kimi"]
        },

    "4" : {
        "nom" : "Sport",
        "animes" : ["Blue Lock", "Captain Tsubasa", "Haikyuu !", "Kuroko no Basket"]
        },




    "5": {
        "nom" : "Ghibli / Film d'animation",
        "animes" : ["Princesse Mononoke", "Totoro", "Le royaume des chats", "Le voyage de Chihiro",
                    "Le chateau ambulant", "Le chateau dans le ciel", "Arrietty",
                    "La colline aux coquelicots", "Your name", "Perfect Blue", "Suzume",
                    "Cosmic princess kaguya", "Porco Rosso", "Colorful"]
        },
    }


groupes_similaires = {
    "Hunter X Hunter" : ["L'atelier des sorciers"],
    "Jujutsu Kaisen" : ["Gachiakuta"],
    "Death Note" : ["Erased"], 
    "Tokyo Revengers" : ["Wind Breaker"],
    "Chainsaw Man" : ["Dandadan"],
    "Tomodachi Game" : ["Death Parade"] ,
    "The Promised Neverland" : ["Tengoku Daimokyo"],
    "The Summer Hikaru Died" : ["Takopi's original sin"],
    "Made in abyss" : ["Sérieux ? T'as kiffé ce vieux truc ?"],
    "Nana" : ["Paradise Kiss"],
    }

def recommander_par_genre():
    print("\n🎌 Choisis ton genre préféré :")
    
    for numéro, catégorie in animes_par_genre.items():
        print(numéro + " - " + catégorie["nom"])

    choix = input("\nTon choix : ")

    if choix in animes_par_genre:
        catégorie = animes_par_genre[choix]

        print("\n✨ Voici quelques recommandations :")
        
        for anime in catégorie["animes"]:
            print("- " + anime)

    else:
        print("\n Ce choix n'existe pas.")


def recommander_similaire():
    anime = input("\nEntre le nom d'un anime que tu aimes : ")

    if anime in groupes_similaires:
        print("\n✨ Si tu aimes " + anime + ", tu pourrais aimer :")

        for recommandation in groupes_similaires[anime]:
            print("- " + recommandation)

    else:
        print("\n Sorry, cet anime n'est pas dans notre base de données.")


print("===================================")
print("       🎌 ANIME FREAK")
print("       RECOMMANDATEUR")
print("===================================")

print("\nQue veux-tu faire ?")
print("1 - Trouver des animes par genre")
print("2 - Trouver des animes similaires à un anime")

choix = input("\nTon choix : ")

if choix == "1":
    recommander_par_genre()

elif choix == "2":
    recommander_similaire()

else:
    print("\n Choix invalide.")
