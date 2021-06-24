import function
import ia
from class_custom.attacks import Attack
from class_custom.player import Player
from class_custom.pokemon import Pokemon
from class_custom.type import Type
from random import *
from qiskit import Aer, QuantumCircuit, QuantumRegister

# Init Qasm simulator backend
qasm = Aer.get_backend('qasm_simulator')

backend_sim = qasm  # Choose your backend : <quantum_computer> or <qasm>

# Types creation --> Sources : https://boutique-pokemon.com/blogs/blog-pokemon/table-types-pokemon
fire = Type("Fire")
normal = Type("Normal")
water = Type("Water")
grass = Type("Grass")
electric = Type("Electric")
fly = Type("Fly")
poison = Type("Poison")
bug = Type("Bug")
ghost = Type("Ghost")
ground = Type("Ground")
dark = Type("Dark")
ice = Type("Ice")
steel = Type("Steel")

resistance = [bug, grass, fire, ice, steel]
weakness = [water, ground]
imunite = ["None"]
fire.add_info(resistance, weakness, imunite)

resistance = ["None"]
weakness = ["None"]
imunite = [ghost]
normal.add_info(resistance, weakness, imunite)

resistance = [grass, ground]
weakness = [fire, fly]
imunite = ["None"]
bug.add_info(resistance, weakness, imunite)

resistance = [water, fire, steel]
weakness = [grass, electric]
imunite = ["None"]
water.add_info(resistance, weakness, imunite)

resistance = [water, electric, grass, ground]
weakness = [fire, bug, poison, fly, ice]
imunite = ["None"]
grass.add_info(resistance, weakness, imunite)

resistance = [electric, fly, steel]
weakness = [ground]
imunite = ["None"]
electric.add_info(resistance, weakness, imunite)

resistance = [bug, grass]
weakness = [electric, ice]
imunite = [ground]
fly.add_info(resistance, weakness, imunite)

resistance = [ghost, dark]
weakness = [bug]
imunite = ["None"]
dark.add_info(resistance, weakness, imunite)

resistance = [bug, poison]
weakness = [ghost, dark]
imunite = [normal]
ghost.add_info(resistance, weakness, imunite)

resistance = [bug, grass, poison]
weakness = [ground]
imunite = ["None"]
poison.add_info(resistance, weakness, imunite)

resistance = [poison]
weakness = [water, grass, ice]
imunite = [electric]
ground.add_info(resistance, weakness, imunite)

resistance = [ice]
weakness = [fire, steel]
imunite = ["None"]
ice.add_info(resistance, weakness, imunite)

resistance = [steel, ice, bug, normal, grass, fly]
weakness = [fire, ground]
imunite = [poison]
steel.add_info(resistance, weakness, imunite)

# type qubits creation
fire.qubit = QuantumRegister(1, 'fire')
normal.qubit = QuantumRegister(1, 'normal')
water.qubit = QuantumRegister(1, 'water')
grass.qubit = QuantumRegister(1, 'grass')
electric.qubit = QuantumRegister(1, 'electric')
fly.qubit = QuantumRegister(1, 'fly')
poison.qubit = QuantumRegister(1, 'poison')
bug.qubit = QuantumRegister(1, 'bug')
ghost.qubit = QuantumRegister(1, 'ghost')
ground.qubit = QuantumRegister(1, 'ground')
dark.qubit = QuantumRegister(1, 'dark')
ice.qubit = QuantumRegister(1, 'ice')
steel.qubit = QuantumRegister(1, 'steel')
qc_type = QuantumCircuit(steel.qubit, fire.qubit, normal.qubit, water.qubit, grass.qubit, electric.qubit, fly.qubit, poison.qubit, bug.qubit, ghost.qubit, ground.qubit, dark.qubit, ice.qubit)

# Attacks creation
fire_blast = Attack("Fire Blast", fire, 110, 0.85, "special")
hurricane = Attack("Hurricane", fly, 110, 0.70, "special")
earthquake = Attack("Earthquake", ground, 100, 1, "physical")
leaf_storm = Attack("Leaf Storm", grass, 90, 1, "special")
shadow_ball = Attack("Shadow Ball", ghost, 80, 1, "special")
sludge_bomb = Attack("Sludge Bomb", poison, 90, 1, "special")
thunder = Attack("Thunder", electric, 110, 0.70, "special")
dark_pulse = Attack("Dark Pulse", dark, 80, 1, "special")
ice_beam = Attack("Ice Beam", ice, 90, 1, "special")
hydroblast = Attack("Hydroblast", water, 110, 0.8, "special")
iron_tail = Attack("Iron Tail", steel, 100, 0.75, "physical")
slam = Attack("Slam", normal, 80, 0.75, "physical")
grass_knot = Attack("Grass Knot", grass, 80, 1, "special")
flash_cannon = Attack("Flash Cannon", steel, 80, 1, "special")
giga_impact = Attack("Giga-Impact", normal, 150, 0.9, "physical")
bite = Attack("Bite", dark, 60, 1, "physical")
tri_attack = Attack("Triplattaque", normal, 80, 1, "special")
hyper_beam = Attack("Hyper Beam", normal, 150, 0.9, "special")
throat_chop = Attack("Throat Chop", dark, 80, 1, "physical")
fire_punch = Attack("Fire Punch", fire, 75, 1, "physical")

# Pokémon creation --> Sources : https://www.pokepedia.fr/Pikachu#Statistiques-remarques1
charizard = Pokemon("Charizard", [fire, fly], 360, 267, 255, 317, 269, 299)
gengar = Pokemon("Gengar", [ghost, poison], 324, 229, 219, 359, 249, 319)
blastoise = Pokemon("Blastoise", [water], 362, 265, 299, 269, 309, 255)
pikachu = Pokemon("Pikachu", [electric], 294, 259, 199, 249, 219, 339)
glaceon = Pokemon("Glaceon", [ice], 334, 219, 319, 359, 289, 229)
porygonz = Pokemon("Porygon-Z", [normal], 374, 259, 239, 369, 249, 279)
abomasnow = Pokemon("Abomasnow", [grass, ice], 384, 283, 249, 283, 269, 219)
toxtricity = Pokemon("Toxtricity", [electric, poison], 354, 295, 239, 327, 239, 249)

# Attacks learning
charizard.learn_attacks([fire_blast, hurricane, earthquake, leaf_storm])
gengar.learn_attacks([sludge_bomb, dark_pulse, shadow_ball, thunder])
blastoise.learn_attacks([ice_beam, hydroblast, flash_cannon, giga_impact])
pikachu.learn_attacks([thunder, iron_tail, slam, grass_knot])
glaceon.learn_attacks([ice_beam, slam, iron_tail, bite])
porygonz.learn_attacks([thunder, ice_beam, tri_attack, dark_pulse])
abomasnow.learn_attacks([ice_beam, leaf_storm, earthquake, giga_impact])
toxtricity.learn_attacks([sludge_bomb, thunder, throat_chop, fire_punch])

# Player creation
me = Player("Oak", "j1")
him = Player("Agatha", "j2")

##############################################################
# GAME

# Choose of poké
for i in range(3):
    u = 0
    for y in Pokemon.pokedex:
        print("{} - {}".format(u, y.name))
        u += 1
    pokemon_j1 = int(input("Choose your Poké by its number : "))
    me.team.append(Pokemon.pokedex[pokemon_j1])
    Pokemon.pokedex.remove(Pokemon.pokedex[pokemon_j1])
    pokemon_j2 = randint(0, len(Pokemon.pokedex) - 1)
    him.team.append(Pokemon.pokedex[pokemon_j2])
    Pokemon.pokedex.remove(Pokemon.pokedex[pokemon_j2])

u = 0
for i in me.team:
    print("{} - {}".format(u, i.name))
    u += 1

first = int(input("Choose your 1st Poké by its number : "))
print("-----------------------------------------------------------")
me.addFirst(me.team[first])
him.addFirst(him.team[randint(0, 2)])

play = 1
# Round
while play:
    print("##############################################################")
    print("J1 - {}".format(me.pokemon.name))
    print("J2 - {}".format(him.pokemon.name))

    him.action = 1
    me.action = 1

    action_j2 = ia.quantum_action(him.pokemon, me.pokemon, qc_type, backend_sim)
    if action_j2 == 0 or len(him.team) == 1:
        attack_j2 = ia.quantum_attaq(him.pokemon, me.pokemon, qc_type, backend_sim)
    else:
        copy_team = []
        for i in him.team:
            if i != him.pokemon:
                copy_team.append(i)
        next_poke = ia.quantum_switch(copy_team, me.pokemon, qc_type, backend_sim)
        him.addFirst(copy_team[next_poke])
        him.action = 0

    action_j1 = int(input("[0] - Attacks |||||| [1] - Pokémon : "))
    print("-----------------------------------------------------------")
    if action_j1 == 0:
        # Attack choose
        u = 0
        for i in me.pokemon.attacks:
            print("[{}] {}  |   ".format(u, i.name))
            u += 1
        attack_j1 = int(input("Choose an attack by its number : "))
        print("-----------------------------------------------------------")
    else:
        # Switch choose
        u = 0
        for i in me.team:
            print("{} - {}".format(u, i.name))
            u += 1
        next_poke = int(input("Choose the Poké to use by its number : "))
        print("-----------------------------------------------------------")
        me.addFirst(me.team[next_poke])
        me.action = 0

    if action_j1 == 1:
        print("{} call {}".format(me.name, me.pokemon.name))
    if action_j2 == 1:
        print("{} call {}".format(him.name, him.pokemon.name))

    # Who first ?
    while (him.action == 1 or me.action == 1) and (him.pokemon.status == 1 and me.pokemon.status == 1):
        # The fastest !
        if him.action == 1 and me.action == 1:
            if me.pokemon.speed > him.pokemon.speed:
                function.action_attack(me.pokemon.attacks[attack_j1], me, him, backend_sim)
            elif me.pokemon.speed < him.pokemon.speed:
                function.action_attack(him.pokemon.attacks[attack_j2], him, me, backend_sim)
            # Speedtie
            else:
                speetie = function.quantum_fight(0.5)
                if speetie == 0:
                    function.action_attack(me.pokemon.attacks[attack_j1], me, him, backend_sim)
                else:
                    function.action_attack(him.pokemon.attacks[attack_j2], him, me, backend_sim)
        # The lowest !
        else:
            if me.action == 1 and me.pokemon.status == 1:
                function.action_attack(me.pokemon.attacks[attack_j1], me, him, backend_sim)

            elif him.action == 1 and him.pokemon.status == 1:
                function.action_attack(him.pokemon.attacks[attack_j2], him, me, backend_sim)

    # Burn / Poison
    if me.pokemon.malus != "None" and me.pokemon.status != 0:
        if me.pokemon.malus == "poison":
            print("{} suffers from poison, he loose {} pv".format(me.pokemon.name, round(me.pokemon.pv/8)))
            me.pokemon.dommages += round(me.pokemon.pv/8)
        if me.pokemon.malus == "burn":
            print("{} suffers from his burn, he loose {} pv".format(me.pokemon.name, round(me.pokemon.pv / 16)))
            me.pokemon.dommages += round(me.pokemon.pv / 16)
        if me.pokemon.dommages >= me.pokemon.pv:
            me.pokemon.status = 0
    if him.pokemon.malus != "None" and him.pokemon.status != 0:
        if him.pokemon.malus == "poison":
            print("{} suffers from poison, he loose {} pv".format(him.pokemon.name, round(him.pokemon.pv / 8)))
            him.pokemon.dommages += round(him.pokemon.pv / 8)
        if him.pokemon.malus == "burn":
            print("{} suffers from his burn, he loose {} pv".format(him.pokemon.name, round(him.pokemon.pv / 16)))
            him.pokemon.dommages += round(him.pokemon.pv / 16)
        if him.pokemon.dommages >= him.pokemon.pv:
            him.pokemon.status = 0

    # End of round, check if KO
    if me.pokemon.status == 0 or him.pokemon.status == 0:
        if me.pokemon.status == 0:
            print("{} is KO !".format(me.pokemon.name))
            me.team.remove(me.pokemon)
            # Switch me
            if len(me.team) > 0:
                u = 0
                for i in me.team:
                    print("{} - {}".format(u, i.name))
                    u += 1
                next_poke = int(input("Choose a Poké by its number : "))
                print("-----------------------------------------------------------")
                me.addFirst(me.team[next_poke])
                print("{} call {}".format(me.name, me.pokemon.name))
            else:
                print("{} won !".format(him.name))
                print("GAME OVER !")
                play = 0
        if him.pokemon.status == 0:
            print("{} is KO !".format(him.pokemon.name))
            him.team.remove(him.pokemon)
            # Switch adversaire
            if len(him.team) > 0:
                if len(him.team) > 1:
                    next_poke = ia.quantum_switch(him.team, me.pokemon, qc_type, backend_sim)
                else:
                    next_poke = 0
                him.addFirst(him.team[next_poke])
                print("{} call {}".format(him.name, him.pokemon.name))
            else:
                print("{} loose !".format(him.name))
                print("YOU WON !")
                play = 0

print("The fight is over !")
actualize = int(input("Push enter to auto F5 the page"))
