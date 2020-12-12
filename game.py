import function
import ia
from class_custom.attaques import Attaque
from class_custom.joueur import Joueur
from class_custom.pokemon import Pokemon
from class_custom.type import Type
from random import *
from qiskit import Aer, QuantumCircuit, QuantumRegister, ClassicalRegister, execute, IBMQ

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

resistance = [insecte, plante, feu, glace]
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

resistance = [eau, feu]
faiblesse = [plante, electrique]
imunite = ["None"]
eau.add_info(resistance, faiblesse, imunite)

resistance = [eau, electrique, plante, sol]
faiblesse = [feu, insecte, poison, vol, glace]
imunite = ["None"]
plante.add_info(resistance, faiblesse, imunite)

resistance = [electrique, vol]
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
qc_type = QuantumCircuit(feu.qubit, normal.qubit, eau.qubit, plante.qubit, electrique.qubit, vol.qubit, poison.qubit, insecte.qubit, spectre.qubit, sol.qubit, tenebre.qubit, glace.qubit)

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

# Création des pokémons --> Sources : https://www.pokepedia.fr/Pikachu#Statistiques-remarques1
dracaufeu = Pokemon("Dracaufeu", [feu, vol], 360, 267, 255, 317, 269, 299)
ectoplasma = Pokemon("Ectoplasma", [spectre, poison], 324, 229, 219, 359, 249, 319)
tortank = Pokemon("Tortank", [eau], 362, 265, 299, 269, 309, 255)
pikachu = Pokemon("Pikachu", [electrique], 294, 259, 199, 249, 219, 339)

# Apprentissage des attaques
dracaufeu.apprendre_attaques([deflagration, vent_violent, seisme, tempete_verte])
ectoplasma.apprendre_attaques([hydrocanon, vibrobscur, laser_glace, fatal_foudre])

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

    if moi.pokemon.status == 0 or lui.pokemon.status == 0:
        play = 0
        if moi.pokemon.status == 1:
            print("{} a gagné !".format(moi.name))
        else:
            print("{} a gagné !".format(lui.name))

print("Combat fini")
