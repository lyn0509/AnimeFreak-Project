# =======================================================================================================
#                                   🪪 ANIME FREAK - GÉNÉRATEUR DE PSEUDOS
#    Trouve un pseudo pour ton compte en quelques clics et rejoins la communauté des AnimesFreaks !
# =======================================================================================================

import random


préfixes = {
    "1": ["Yuki", "Hana", "Mika", "Ai", "Yuzu", "Yuna", "Yuri", "Yuma", "Sachi", "Sana", "Seiko", "Ume",
          "Waka", "Yae", "Kei", "Mai", "Mao", "Mari", "Hika", "Aya", "Shizu"],
    "2": ["Aki", "Ren", "Kaito", "Hiro", "Yuto", "Yuta", "Yuu", "Shin", "Shiro", "Taku", "Shota", "Taiki",
          "Taka", "Taro", "Kazu", "Koji", "Natsu", "Rei", "Haru", "Yoshi", "Haki", "Jun", "Daiki"]
}


milieux =  {
    "1": ["chi", "hita", "shita", "ka", "ra", "zu", "me", "na", "da", "mei", "no", "ne", "shi", "chi", ],
    "2": ["mi", "ka", "hito", "ta", "shito", "te", "ji", "ri", "ki", "mo", "ne", "da", "rin", "to", "no",
          "shi", "do"]
    }



suffixes = {
    "1": ["♡", "˚ ༘♡ ⋆｡˚", "☄. *. ⋆", "🌸", "☆", "༊*·˚", ".ೃ࿐", "*ೃ༄", "ღ","✿" , "♪", "✼"],
    "2": ["#", "x", "╬", "埉", "❈", "食", "㊍" ,"▆ ▅ ▄ ▂" ,"● ☆ ● ☆ ●" , "々" , "™"]
}

def choisir_style(question, choix):
    print("\n" + question)

    for numéro, style in choix.items():
        print(numéro + " - " + style)

    réponse = input("\nTon choix : ")

    while réponse not in choix:
        print("❌ Choix invalide.")
        réponse = input("Choisis un numéro valide : ")

    return réponse


print("===================================")
print("       🪪 GÉNÉRATEUR DE PSEUDOS")
print("===================================")

style_préfixe = choisir_style(
    "Quel style veux-tu pour le début de ton pseudo ?",
    {
        "1": "Féminin",
        "2": "Masculin"
    }
)

style_milieu = choisir_style(
    "Quel style veux-tu pour le milieux de ton pseudo ?",
    {
        "1": "Féminin",
        "2": "Masculin"
    }
)

style_suffixe = choisir_style(
    "Quel type de fin veux-tu ?",
    {
        "1": "Cute",
        "2": "Clean"
    }
)


début = random.choice(préfixes[style_préfixe])
milieu = random.choice(milieux[style_milieu])
fin = random.choice(suffixes[style_suffixe])

pseudo = début + milieu + fin

print("\n✨ Ton pseudo est :")
print(pseudo)
