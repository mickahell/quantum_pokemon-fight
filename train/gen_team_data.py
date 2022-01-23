from train.robot_vs_robot import team, battle
from stats.gen_data import gen_team_data
from src.class_custom.attacks import Attack
from src.class_custom.player import Player
from src.class_custom.pokemon import Pokemon
from src.class_custom.type import Type
from qiskit import Aer, QuantumCircuit, QuantumRegister

import warnings


class Team:
    def __init__(self):
        warnings.filterwarnings("ignore", category=DeprecationWarning)

        # Init Qasm simulator backend
        qasm = Aer.get_backend("qasm_simulator")

        backend_sim = qasm  # Choose your backend : <quantum_computer> or <qasm>

        for u in range(2):
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
            fire.qubit = QuantumRegister(1, "fire")
            normal.qubit = QuantumRegister(1, "normal")
            water.qubit = QuantumRegister(1, "water")
            grass.qubit = QuantumRegister(1, "grass")
            electric.qubit = QuantumRegister(1, "electric")
            fly.qubit = QuantumRegister(1, "fly")
            poison.qubit = QuantumRegister(1, "poison")
            bug.qubit = QuantumRegister(1, "bug")
            ghost.qubit = QuantumRegister(1, "ghost")
            ground.qubit = QuantumRegister(1, "ground")
            dark.qubit = QuantumRegister(1, "dark")
            ice.qubit = QuantumRegister(1, "ice")
            steel.qubit = QuantumRegister(1, "steel")
            qc_type = QuantumCircuit(
                steel.qubit,
                fire.qubit,
                normal.qubit,
                water.qubit,
                grass.qubit,
                electric.qubit,
                fly.qubit,
                poison.qubit,
                bug.qubit,
                ghost.qubit,
                ground.qubit,
                dark.qubit,
                ice.qubit,
            )

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
            #hyper_beam = Attack("Hyper Beam", normal, 150, 0.9, "special")
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
            toxtricity = Pokemon(
                "Toxtricity", [electric, poison], 354, 295, 239, 327, 239, 249
            )

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
            me = Player("Oak", "j1", "human")
            him = Player("Agatha", "j2", "robot")

            ##############################################################
            # GAME

            print(
                """
###################################################
# Welcome in the Quantum Pokémon fight - CLI
# Will you succeed to win against the Quantum AI ?
#
# Good Luck !!!
###################################################
            """
            )

            team(me, him, nb_team=3)
            winner, looser = battle(me, him, qc_type, backend_sim)

            for i, y in zip(winner.register_team, looser.register_team):
                gen_team_data(pokemon=i, has_win="yes")
                gen_team_data(pokemon=y, has_win="no")

            print("Fight {} is finished !".format(u + 1))

        print("Gen team data program ended !")
