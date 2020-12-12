import function
import ia
from class_custom.attaques import Attaque
from class_custom.joueur import Joueur
from class_custom.pokemon import Pokemon
from class_custom.type import Type
from random import *
from qiskit import Aer, QuantumCircuit, QuantumRegister, IBMQ

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
glace = Type("Glace")
acier = Type("Acier")

resistance = [insecte, plante, feu, glace, acier]
faiblesse = [eau, sol]
imunite = ["None"]
feu.add_info(resistance, faiblesse, imunite)

resistance = ["None"]
faiblesse = ["None"]
imunite = [spectre]
normal.add_info(resistance, faiblesse, imunite)

resistance = [plante, sol]
faiblesse = [feu, vol]
imunite = ["None"]
insecte.add_info(resistance, faiblesse, imunite)

resistance = [eau, feu, acier]
faiblesse = [plante, electrique]
imunite = ["None"]
eau.add_info(resistance, faiblesse, imunite)

resistance = [eau, electrique, plante, sol]
faiblesse = [feu, insecte, poison, vol, glace]
imunite = ["None"]
plante.add_info(resistance, faiblesse, imunite)

resistance = [electrique, vol, acier]
faiblesse = [sol]
imunite = ["None"]
electrique.add_info(resistance, faiblesse, imunite)

resistance = [insecte, plante]
faiblesse = [electrique, glace]
imunite = [sol]
vol.add_info(resistance, faiblesse, imunite)

resistance = [spectre, tenebre]
faiblesse = [insecte]
imunite = ["None"]
tenebre.add_info(resistance, faiblesse, imunite)

resistance = [insecte, poison]
faiblesse = [spectre, tenebre]
imunite = [normal]
spectre.add_info(resistance, faiblesse, imunite)

resistance = [insecte, plante, poison]
faiblesse = [sol]
imunite = ["None"]
poison.add_info(resistance, faiblesse, imunite)

resistance = [poison]
faiblesse = [eau, plante, glace]
imunite = [electrique]
sol.add_info(resistance, faiblesse, imunite)

resistance = [glace]
faiblesse = [feu]
imunite = ["None"]
glace.add_info(resistance, faiblesse, imunite)

resistance = [acier, glace, insecte, normal, plante, vol]
faiblesse = [feu, sol]
imunite = [poison]
acier.add_info(resistance, faiblesse, imunite)

# Création des qubits de type
feu.qubit = QuantumRegister(1, 'feu')
normal.qubit = QuantumRegister(1, 'normal')
eau.qubit = QuantumRegister(1, 'eau')
plante.qubit = QuantumRegister(1, 'plante')
electrique.qubit = QuantumRegister(1, 'electric')
vol.qubit = QuantumRegister(1, 'vol')
poison.qubit = QuantumRegister(1, 'poison')
insecte.qubit = QuantumRegister(1, 'insecte')
spectre.qubit = QuantumRegister(1, 'spectre')
sol.qubit = QuantumRegister(1, 'sol')
tenebre.qubit = QuantumRegister(1, 'tenebre')
glace.qubit = QuantumRegister(1, 'glace')
acier.qubit = QuantumRegister(1, 'acier')
qc_type = QuantumCircuit(acier.qubit, feu.qubit, normal.qubit, eau.qubit, plante.qubit, electrique.qubit, vol.qubit, poison.qubit, insecte.qubit, spectre.qubit, sol.qubit, tenebre.qubit, glace.qubit)

# Création des attaques
deflagration = Attaque("Déflagration", feu, 110, 0.85, "special")
vent_violent = Attaque("Vent violent", vol, 110, 0.70, "special")
seisme = Attaque("Séisme", sol, 100, 1, "physique")
tempete_verte = Attaque("Tempête verte", plante, 90, 1, "special")
ball_ombre = Attaque("Ball'Ombre", spectre, 80, 1, "special")
bombe_beurk = Attaque("Bombe Beurk", poison, 90, 1, "special")
fatal_foudre = Attaque("Fatal-foudre", electrique, 110, 0.70, "special")
vibrobscur = Attaque("Vibrobscur", tenebre, 80, 1, "special")
laser_glace = Attaque("Laser Glace", glace, 90, 1, "special")
hydrocanon = Attaque("Hydrocanon", eau, 110, 0.8, "special")
queue_fer = Attaque("Queue de fer", acier, 100, 0.75, "physique")
souplesse = Attaque("Souplesse", normal, 80, 0.75, "physique")
noeud_herbe = Attaque("Noeud Herbe", plante, 80, 1, "special")
luminocanon = Attaque("Luminocanon", acier, 80, 1, "special")
giga_impact = Attaque("Giga-Impact", normal, 150, 0.9, "physique")

# Création des pokémons --> Sources : https://www.pokepedia.fr/Pikachu#Statistiques-remarques1
dracaufeu = Pokemon("Dracaufeu", [feu, vol], 360, 267, 255, 317, 269, 299)
ectoplasma = Pokemon("Ectoplasma", [spectre, poison], 324, 229, 219, 359, 249, 319)
tortank = Pokemon("Tortank", [eau], 362, 265, 299, 269, 309, 255)
pikachu = Pokemon("Pikachu", [electrique], 294, 259, 199, 249, 219, 339)

# Apprentissage des attaques
dracaufeu.apprendre_attaques([deflagration, vent_violent, seisme, tempete_verte])
ectoplasma.apprendre_attaques([bombe_beurk, vibrobscur, ball_ombre, fatal_foudre])
tortank.apprendre_attaques([laser_glace, hydrocanon, luminocanon, giga_impact])
pikachu.apprendre_attaques([fatal_foudre, queue_fer, souplesse, noeud_herbe])

# Création joueur
moi = Joueur("Chen", "j1")
lui = Joueur("Agatha", "j2")

##############################################################
# GAME

# Selection du poké
u = 0
for i in Pokemon.pokedex:
    print("{} - {}".format(u, i.name))
    u += 1
pokemon_j1 = int(input("Choisi un Poké par son chiffre : "))
moi.addEquipe(Pokemon.pokedex[pokemon_j1])
lui.addEquipe(Pokemon.pokedex[randint(0, 3)])

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
    attaque_j2 = ia.quantum_ia(lui.pokemon, moi.pokemon, qc_type, backend_sim)

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

    # Brulure / Poison
    if moi.pokemon.malus != "None" and moi.pokemon.status != 0:
        if moi.pokemon.malus == "poison":
            print("{} souffre du poison, il perd {} pv".format(moi.pokemon.name, round(moi.pokemon.pv/8)))
            moi.pokemon.degats += round(moi.pokemon.pv/8)
        if moi.pokemon.malus == "brulure":
            print("{} souffre de sa brûlure, il perd {} pv".format(moi.pokemon.name, round(moi.pokemon.pv / 16)))
            moi.pokemon.degats += round(moi.pokemon.pv / 16)
        if moi.pokemon.degats >= moi.pokemon.pv:
            moi.pokemon.status = 0
    if lui.pokemon.malus != "None" and lui.pokemon.status != 0:
        if lui.pokemon.malus == "poison":
            print("{} souffre du poison, il perd {} pv".format(lui.pokemon.name, round(lui.pokemon.pv / 8)))
            lui.pokemon.degats += round(lui.pokemon.pv / 8)
        if lui.pokemon.malus == "brulure":
            print("{} souffre de sa brûlure, il perd {} pv".format(lui.pokemon.name, round(lui.pokemon.pv / 16)))
            lui.pokemon.degats += round(lui.pokemon.pv / 16)
        if lui.pokemon.degats >= lui.pokemon.pv:
            lui.pokemon.status = 0

    if moi.pokemon.status == 0 or lui.pokemon.status == 0:
        play = 0
        if moi.pokemon.status == 1:
            print("{} a gagné !".format(moi.name))
        else:
            print("{} a gagné !".format(lui.name))

print("Combat fini")
