import function
from class_custom.attaques import Attaque
from class_custom.joueur import Joueur
from class_custom.pokemon import Pokemon
from class_custom.type import Type
from random import *
from qiskit import Aer, IBMQ

# Init Qasm simulator backend
qasm = Aer.get_backend('qasm_simulator')

# Init Real Quantum computer
IBMQ.load_account()
provider = IBMQ.get_provider('ibm-q')
quantum_computer = provider.get_backend('ibmq_16_melbourne')

backend_sim = qasm  # Choose your backend : <quantum_computer> or <qasm>

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

resistance = ["Acier", "Electrique", "Vol"]
faiblesse = ["Sol"]
imunite = []
electrique.add_info(resistance, faiblesse, imunite)

resistance = ["Combat", "Insecte", "Plante"]
faiblesse = ["Electrique", "Glace", "Roche"]
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
    #print("{} - {}".format(u, i.name))
    u += 1
#pokemon_j1 = int(input("Choisi un Poké par son chiffre : "))
#print(Pokemon.pokedex[pokemon_j1].name)
moi.addEquipe(Pokemon.pokedex[0])
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
    attaque_j2 = randint(0, 3)

    lui.action = 1
    moi.action = 1

    # Qui commence ?
    while (lui.action == 1 or moi.action == 1) and (lui.pokemon.status == 1 and moi.pokemon.status == 1):
        # Le plus rapide !
        if lui.action == 1 and moi.action == 1:
            if moi.pokemon.vitesse > lui.pokemon.vitesse:
                function.action_attaque(moi.pokemon.attaques[attaque_j1], moi, lui, backend_sim)
            elif moi.pokemon.vitesse < lui.pokemon.vitesse:
                function.action_attaque(lui.pokemon.attaques[attaque_j2], lui, moi, backend_sim)
            # Speedtie
            else:
                speetie = function.quantum_fight(0.5)
                if speetie == 0:
                    function.action_attaque(moi.pokemon.attaques[attaque_j1], moi, lui, backend_sim)
                else:
                    function.action_attaque(lui.pokemon.attaques[attaque_j2], lui, moi, backend_sim)
        # Le moins rapide !
        else:
            if moi.action == 1 and moi.pokemon.status == 1:
                function.action_attaque(moi.pokemon.attaques[attaque_j1], moi, lui, backend_sim)

            elif lui.action == 1 and lui.pokemon.status == 1:
                function.action_attaque(lui.pokemon.attaques[attaque_j2], lui, moi, backend_sim)

    if moi.pokemon.status == 0 or lui.pokemon.status == 0:
        play = 0
        if moi.pokemon.status == 1:
            print("{} a gagné !".format(moi.name))
        else:
            print("{} a gagné !".format(lui.name))

print("Combat fini")
