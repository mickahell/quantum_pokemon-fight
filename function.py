import math
from qiskit import QuantumCircuit, execute


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
            if attaq.type in i.faiblesse:
                RESISTANCE *= 2
            elif attaq.type in i.resistance:
                RESISTANCE *= 0.5
            elif attaq.type in i.imunite:
                RESISTANCE *= 0

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

        if RESISTANCE > 1:
            print("C'est super efficace !")
        elif RESISTANCE < 1:
            print("Ce n'est pas très efficace !")
        elif RESISTANCE == 0:
            print("{} n'est pas affecté par cette attaque !".format(pokemon_def.name))

        if attaq.type.name == "Poison" and RESISTANCE > 0:
            if quantum_fight(0.3, backend_sim) == 1 and pokemon_def.malus == "None":
                pokemon_def.malus = "poison"
                print("{} est empoisonné.".format(pokemon_def.name))
        if attaq.type.name == "Feu" and RESISTANCE > 0:
            if quantum_fight(0.1, backend_sim) == 1 and pokemon_def.malus == "None":
                pokemon_def.malus = "brulure"
                pokemon_def.points_attaque *= 0.5
                print("{} est brulé.".format(pokemon_def.name))
        if attaq.type.name == "Glace" and RESISTANCE > 0:
            if quantum_fight(0.1, backend_sim) == 1 and pokemon_def.malus == "None":
                pokemon_def.malus = "gel"
                print("{} est gelé.".format(pokemon_def.name))
        if attaq.type.name == "Electrique" and RESISTANCE > 0:
            if quantum_fight(0.3, backend_sim) == 1 and pokemon_def.malus == "None":
                pokemon_def.malus = "paralysie"
                pokemon_def.vitesse *= 0.5
                print("{} est paralysé.".format(pokemon_def.name))

    else:
        print("{} a loupé son attaque !".format(pokemon_att.name))
        degats = 0

    return degats


def action_attaque(attaque, joueur_att, joueur_def, backend_sim):
    joueur_att.action = 0
    degel = 1
    paralysie = 1

    if joueur_att.pokemon.malus == "gel":
        degel = quantum_fight(0.2, backend_sim)
        if degel == 1:
            print("{} est dégelé.".format(joueur_att.pokemon.name))
            joueur_att.pokemon.malus = "None"
        else:
            print("{} est toujours gelé.".format(joueur_att.pokemon.name))

    if joueur_att.pokemon.malus == "paralysie":
        paralysie = quantum_fight(0.75, backend_sim)
        if paralysie == 0:
            print("{} est paralysé, il ne peut pas attaquer.".format(joueur_att.pokemon.name))

    if degel == 1 and paralysie == 1:
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
