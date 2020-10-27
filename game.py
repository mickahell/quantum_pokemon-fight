from class_custom.pokemon import Pokemon
from class_custom.type import Type
from class_custom.attaques import Attaque

# Création des types
feu = Type("Feu")
normal = Type("Normal")
eau = Type("Eau")
plante = Type("Plante")
electrique = Type("Electrique")
vol = Type("Vol")
poison = Type("Poison")
insecte = Type("Insecte")

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
deflagration = Attaque("Déflagration", "Feu", 110, 0.85, "special")

# Création des pokémons
dracaufeu = Pokemon("Dracaufeu", ["Feu", "Vol"], 78, 84, 78, 109, 85, 100)
ectoplasma = Pokemon("Ectoplasma", ["Spectre", "Poison"], 60, 65, 60, 130, 75, 110)
tortank = Pokemon("Tortank", ["Eau"], 79, 83, 100, 85, 105, 78)
pikachu = Pokemon("Pikachu", ["Electrique"], 35, 55, 40, 50, 50, 90)

## Apprentissage des attaques
dracaufeu.apprendre_attaques(["Déflagration", "Vent violent", "Séisme", "Tempete verte"])
