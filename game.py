from class_custom.pokemon import Pokemon
from class_custom.type import Type
from class_custom.attaques import Attaque
from class_custom.joueur import Joueur

# Création des types
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

# Création des attaques
deflagration = Attaque("Déflagration", feu, 110, 0.85, "special")
vent_violent = Attaque("Vent violent", vol, 110, 0.70, "special")
seisme = Attaque("Séisme", sol, 100, 1, "physique")
tempete_verte = Attaque("Tempête verte", plante, 90, 1, "special")

# Création des pokémons
dracaufeu = Pokemon("Dracaufeu", [feu, vol], 78, 84, 78, 109, 85, 100)
ectoplasma = Pokemon("Ectoplasma", [spectre, poison], 60, 65, 60, 130, 75, 110)
tortank = Pokemon("Tortank", [eau], 79, 83, 100, 85, 105, 78)
pikachu = Pokemon("Pikachu", [electrique], 35, 55, 40, 50, 50, 90)

## Apprentissage des attaques
dracaufeu.apprendre_attaques([deflagration, vent_violent, seisme, tempete_verte])

# Création joueur
moi = Joueur("Chen", "j1")
lui = Joueur("Olga", "j2")

##############################################################
# GAME

# Affichage Pokés
u = 0
for i in Pokemon.pokedex:
    print("{} - {}".format(u, i.name))
    u += 1

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
    
    # Qui commence ?
    while lui.action == 1 || moi.action == 1:
        # Plus rapide !
        if lui.action == 1 && moi.action == 1:
            if moi.pokemon.vitesse > lui.pokemon.vitesse:
                moi.action = 0
                lui.pokemon.degats = lui.pokemon.degats + moi.pokemon.attaques[attaque_j1].puissance
                if lui.pokemon.degats >= lui.pokemon.pv:
                    lui.pokemon.status = 0
            elif moi.pokemon.vitesse < lui.pokemon.vitesse:
                lui.action = 0
                moi.pokemon.degats = moi.pokemon.degats + lui.pokemon.attaques[attaque_j2].puissance
                if moi.pokemon.degats >= moi.pokemon.pv:
                    moi.pokemon.status = 0
            else:
                moi.action = 0
                lui.pokemon.degats = lui.pokemon.degats + moi.pokemon.attaques[attaque_j1].puissance
                if lui.pokemon.degats >= lui.pokemon.pv:
                    lui.pokemon.status = 0
        # Moins rapide !
        else:
            if moi.action == 1:
                moi.action = 0
                lui.pokemon.degats = lui.pokemon.degats + moi.pokemon.attaques[attaque_j1].puissance
                if lui.pokemon.degats >= lui.pokemon.pv:
                    lui.pokemon.status = 0

            else:
                lui.action = 0
                moi.pokemon.degats = moi.pokemon.degats + lui.pokemon.attaques[attaque_j2].puissance
                if moi.pokemon.degats >= moi.pokemon.pv:
                    moi.pokemon.status = 0




    if moi.pokemon.status == 0 || lui.pokemon.status == 0:
        play = 0

print("Combat fini")
