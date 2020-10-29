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

print("J1 - {}".format(moi.pokemon.name))

