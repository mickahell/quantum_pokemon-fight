import math
from qiskit import Aer, QuantumCircuit, execute, IBMQ


def quantum_fight(psi, backend_sim):
    qc = QuantumCircuit(1, 1)

    qc.rx(math.pi * psi, 0)
    qc.measure(0, 0)

    job = execute(qc, backend_sim, shots=1, memory=True)
    result_job = job.result().get_memory()
    to_return = int(result_job[0], 2)

    return to_return


def calcul_dommage(attaq, pokemon_att, pokemon_def, backend_sim):
    quantum_precision = quantum_fight(attaq.precision, backend_sim)
    if quantum_precision == 1:
        STAB = 1
        RESISTANCE = 1
        CRIT = 1
        if attaq.type in pokemon_att.types:
            STAB = 1.5

        for i in pokemon_def.types:
            if attaq.type.name in i.faiblesse:
                RESISTANCE *= 2
                print("C'est super efficace !")
            elif attaq.type.name in i.resistance:
                RESISTANCE *= 0.5
                print("Ce n'est pas très efficace !")
            elif attaq.type.name in i.imunite:
                RESISTANCE *= 0
                print("{} n'est pas affecté par cette attaque !".format(pokemon_def.name))

        quantum_crit = quantum_fight(0.0417, backend_sim)
        if quantum_crit == 1:
            CRIT = 1.5
            print("coup critique !")

        if attaq.status == "physique":
            degats = ((((100 * 0.4 + 2) * pokemon_att.points_attaque * attaq.puissance) / (
                    pokemon_def.points_defence * 50)) + 2) * STAB * RESISTANCE * CRIT
        else:
            degats = ((((100 * 0.4 + 2) * pokemon_att.points_att_sp * attaq.puissance) / (
                    pokemon_def.points_def_sp * 50)) + 2) * STAB * RESISTANCE * CRIT
    else:
        print("{} a loupé son attaque !".format(pokemon_att.name))
        degats = 0

    return degats


def action_attaque(attaque, joueur_att, joueur_def, backend_sim):
    joueur_att.action = 0
    print("{} utilise {}".format(joueur_att.pokemon.name, attaque.name))
    joueur_def.pokemon.degats = joueur_def.pokemon.degats + calcul_dommage(attaque, joueur_att.pokemon,
                                                                           joueur_def.pokemon, backend_sim)
    if round(joueur_def.pokemon.pv - joueur_def.pokemon.degats) < 0:
        print("{} - 0 / {} pv".format(joueur_def.pokemon.name, joueur_def.pokemon.pv))

    else:
        print("{} - {} / {} pv".format(joueur_def.pokemon.name, round(joueur_def.pokemon.pv - joueur_def.pokemon.degats),
                                    joueur_def.pokemon.pv))

    if joueur_def.pokemon.degats >= joueur_def.pokemon.pv:
        joueur_def.pokemon.status = 0
        print("{} est KO".format(joueur_def.pokemon.name))
        joueur_def.action = 0