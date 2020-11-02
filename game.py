from class_custom.pokemon import Pokemon
from class_custom.type import Type
from class_custom.attaques import Attaque
from class_custom.joueur import Joueur
import function

# Création des types --> Sources : https://boutique-pokemon.com/blogs/blog-pokemon/table-types-pokemon
feu = Type("Feu")
normal = Type("Normal")
eau = Type("Eau")
plante = Type("Plante")
electrique = Type("Electrique")
vol = Type("Vol")
poison = Type("Poison")
insecte = Type("Insecte")
spectre = Type("Spectre")
sol = Type("Sol")
tenebre = Type("Ténèbre")

resistance = ["Insecte", "Plante", "Glace", "Feu", "Fée", "Acier"]
faiblesse = ["Eau", "Roche", "Sol"]
imunite = []
feu.add_info(resistance, faiblesse, imunite)

resistance = []
faiblesse = ["Combat"]
imunite = ["Spectre"]
normal.add_info(resistance, faiblesse, imunite)

resistance = ["Combat", "Plante", "Sol"]
faiblesse = ["Feu", "Vol", "Roche"]
imunite = []
insecte.add_info(resistance, faiblesse, imunite)

resistance = ["Acier", "Eau", "Feu", "Glace"]
faiblesse = ["Plante", "Electrique"]
imunite = []
eau.add_info(resistance, faiblesse, imunite)

resistance = ["Eau", "Electrique", "Plante", "Sol"]
faiblesse = ["Feu", "Glace", "Insecte", "Poison", "Vol"]
imunite = []
plante.add_info(resistance, faiblesse, imunite)

resistance = ["Acier", "Electrik", "Vol"]
faiblesse = ["Sol"]
imunite = []
electrique.add_info(resistance, faiblesse, imunite)

resistance = ["Combat", "Insecte", "Plante"]
faiblesse = ["Electrik", "Glace", "Roche"]
imunite = ["Sol"]
vol.add_info(resistance, faiblesse, imunite)

resistance = ["Spectre", "Ténèbre"]
faiblesse = ["Combat", "Fée", "Insecte"]
imunite = ["Psy"]
tenebre.add_info(resistance, faiblesse, imunite)

resistance = ["Insecte", "Poison"]
faiblesse = ["Spectre", "Ténèbre"]
imunite = ["Normal", "Combat"]
spectre.add_info(resistance, faiblesse, imunite)

resistance = ["Combat", "Fée", "Insecte", "Plante", "Poison"]
faiblesse = ["Psy", "Sol"]
imunite = ["Psy"]
poison.add_info(resistance, faiblesse, imunite)

resistance = ["Poison", "Roche"]
faiblesse = ["Eau", "Glace", "Plante"]
imunite = ["Electrique"]
sol.add_info(resistance, faiblesse, imunite)

# Création des attaques
deflagration = Attaque("Déflagration", feu, 110, 0.85, "special")
vent_violent = Attaque("Vent violent", vol, 110, 0.70, "special")
seisme = Attaque("Séisme", sol, 100, 1, "physique")
tempete_verte = Attaque("Tempête verte", plante, 90, 1, "special")
ball_ombre = Attaque("Ball'Ombre", spectre, 80, 1, "special")
bombe_beurk = Attaque("Bombe Beurk", poison, 90, 1, "special")
fatal_foudre = Attaque("Fatal-foudre", electrique, 110, 0.70, "special")
vibrobscur = Attaque("Vibrobscur", tenebre, 80, 1, "special")

# Création des pokémons --> Sources : https://www.pokepedia.fr/Pikachu#Statistiques-remarques1
dracaufeu = Pokemon("Dracaufeu", [feu, vol], 360, 267, 255, 317, 269, 299)
ectoplasma = Pokemon("Ectoplasma", [spectre, poison], 324, 229, 219, 359, 249, 319)
tortank = Pokemon("Tortank", [eau], 362, 265, 299, 269, 309, 255)
pikachu = Pokemon("Pikachu", [electrique], 294, 259, 199, 249, 219, 339)

# Apprentissage des attaques
dracaufeu.apprendre_attaques([deflagration, vent_violent, seisme, tempete_verte])
ectoplasma.apprendre_attaques([ball_ombre, bombe_beurk, fatal_foudre, vibrobscur])

# Création joueur
moi = Joueur("Chen", "j1")
lui = Joueur("Olga", "j2")

##############################################################
# GAME

# Selection du poké
u = 0
for i in Pokemon.pokedex:
    print("{} - {}".format(u, i.name))
    u += 1
pokemon_j1 = int(input("Choisi un Poké par son chiffre : "))
print(Pokemon.pokedex[pokemon_j1].name)
moi.addEquipe(Pokemon.pokedex[pokemon_j1])
lui.addEquipe(ectoplasma)

print("J1 - {}".format(moi.pokemon.name))
print("J2 - {}".format(lui.pokemon.name))

play = 1
# Tour
while play:
    # Choix attaque
    u = 0
    for i in moi.pokemon.attaques:
        print("[{}] {}  |   ".format(u, i.name))
        u += 1
    attaque_j1 = int(input("Choisi une attaque par son chiffre : "))
    attaque_j2 = 2

    lui.action = 1
    moi.action = 1

    # Qui commence ?
    while (lui.action == 1 or moi.action == 1) and (lui.pokemon.status == 1 and moi.pokemon.status == 1):
        # Le plus rapide !
        if lui.action == 1 and moi.action == 1:
            if moi.pokemon.vitesse > lui.pokemon.vitesse:
                moi.action = 0
                print("{} utilise {}".format(moi.pokemon.name, moi.pokemon.attaques[attaque_j1].name))
                lui.pokemon.degats = lui.pokemon.degats + function.calcul_dommage(moi.pokemon.attaques[attaque_j1], moi.pokemon, lui.pokemon)
                if lui.pokemon.degats >= lui.pokemon.pv:
                    lui.pokemon.status = 0
                    print("{} est KO".format(lui.pokemon.name))
                    lui.action == 0
            elif moi.pokemon.vitesse < lui.pokemon.vitesse:
                lui.action = 0
                print("{} utilise {}".format(lui.pokemon.name, lui.pokemon.attaques[attaque_j2].name))
                moi.pokemon.degats = moi.pokemon.degats + function.calcul_dommage(lui.pokemon.attaques[attaque_j2], lui.pokemon, moi.pokemon)
                if moi.pokemon.degats >= moi.pokemon.pv:
                    moi.pokemon.status = 0
                    print("{} est KO".format(moi.pokemon.name))
                    moi.action == 0
            # Speedtie
            else:
                speetie = function.quantum_fight(0.5)
                if speetie == 0:
                    moi.action = 0
                    print("{} utilise {}".format(moi.pokemon.name, moi.pokemon.attaques[attaque_j1].name))
                    lui.pokemon.degats = lui.pokemon.degats + function.calcul_dommage(moi.pokemon.attaques[attaque_j1], moi.pokemon, lui.pokemon)
                    if lui.pokemon.degats >= lui.pokemon.pv:
                        lui.pokemon.status = 0
                        print("{} est KO".format(lui.pokemon.name))
                        lui.action == 0
                else:
                    lui.action = 0
                    print("{} utilise {}".format(lui.pokemon.name, lui.pokemon.attaques[attaque_j2].name))
                    moi.pokemon.degats = moi.pokemon.degats + function.calcul_dommage(lui.pokemon.attaques[attaque_j2],
                                                                                      lui.pokemon, moi.pokemon)
                    if moi.pokemon.degats >= moi.pokemon.pv:
                        moi.pokemon.status = 0
                        print("{} est KO".format(moi.pokemon.name))
                        moi.action == 0
        # Le moins rapide !
        else:
            if moi.action == 1 and moi.pokemon.status == 1:
                moi.action = 0
                print("{} utilise {}".format(moi.pokemon.name, moi.pokemon.attaques[attaque_j1].name))
                lui.pokemon.degats = lui.pokemon.degats + function.calcul_dommage(moi.pokemon.attaques[attaque_j1], moi.pokemon, lui.pokemon)
                if lui.pokemon.degats >= lui.pokemon.pv:
                    lui.pokemon.status = 0
                    print("{} est KO".format(lui.pokemon.name))
                    lui.action == 0

            elif lui.action == 1 and lui.pokemon.status == 1:
                lui.action = 0
                print("{} utilise {}".format(lui.pokemon.name, lui.pokemon.attaques[attaque_j2].name))
                moi.pokemon.degats = moi.pokemon.degats + function.calcul_dommage(lui.pokemon.attaques[attaque_j2], lui.pokemon, moi.pokemon)
                if moi.pokemon.degats >= moi.pokemon.pv:
                    moi.pokemon.status = 0
                    print("{} est KO".format(moi.pokemon.name))
                    moi.action == 0

    if moi.pokemon.status == 0 or lui.pokemon.status == 0:
        play = 0
        if moi.pokemon.status == 1:
            print("{} a gagné !".format(moi.name))
        else:
            print("{} a gagné !".format(lui.name))

print("Combat fini")
