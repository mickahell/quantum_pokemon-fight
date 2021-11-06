import math
from qiskit import QuantumCircuit, execute
import os
import requests


def quantum_fight(psi, backend_sim):
    qc = QuantumCircuit(1, 1)

    qc.rx(math.pi * psi, 0)
    qc.measure(0, 0)

    job = execute(qc, backend_sim, shots=1, memory=True)
    result_job = job.result().get_memory()
    to_return = int(result_job[0], 2)

    return to_return


def calcul_dommage(attac, pokemon_att, pokemon_def, backend_sim):
    quantum_precision = quantum_fight(attac.precision, backend_sim)
    if quantum_precision == 1:
        STAB = 1
        RESISTANCE = 1
        CRIT = 1
        if attac.type in pokemon_att.types:
            STAB = 1.5

        for i in pokemon_def.types:
            if attac.type in i.weakness:
                RESISTANCE *= 2
            elif attac.type in i.resistance:
                RESISTANCE *= 0.5
            elif attac.type in i.imunite:
                RESISTANCE *= 0

        quantum_crit = quantum_fight(0.0417, backend_sim)
        if quantum_crit == 1:
            CRIT = 1.5
            print("critical hit !")

        if attac.status == "physical":
            dommages = ((((100 * 0.4 + 2) * pokemon_att.points_attack * attac.power) / (
                    pokemon_def.points_defense * 50)) + 2) * STAB * RESISTANCE * CRIT
        else:
            dommages = ((((100 * 0.4 + 2) * pokemon_att.points_att_sp * attac.power) / (
                    pokemon_def.points_def_sp * 50)) + 2) * STAB * RESISTANCE * CRIT

        if RESISTANCE > 1:
            print("It's super efficient !")
        if RESISTANCE < 1:
            if RESISTANCE == 0:
                print("{} is not affected by this attack !".format(pokemon_def.name))
            else:
                print("It is not very effective !")

        if attac.type.name == "Poison" and RESISTANCE > 0:
            if quantum_fight(0.3, backend_sim) == 1 and pokemon_def.malus == "None":
                pokemon_def.malus = "poison"
                print("{} is poisoned.".format(pokemon_def.name))
        if attac.type.name == "Fire" and RESISTANCE > 0:
            if quantum_fight(0.1, backend_sim) == 1 and pokemon_def.malus == "None":
                pokemon_def.malus = "burn"
                pokemon_def.points_attack *= 0.5
                print("{} is burnt.".format(pokemon_def.name))
        if attac.type.name == "Ice" and RESISTANCE > 0:
            if quantum_fight(0.1, backend_sim) == 1 and pokemon_def.malus == "None":
                pokemon_def.malus = "freeze"
                print("{} is frozen.".format(pokemon_def.name))
        if attac.type.name == "Electric" and RESISTANCE > 0:
            if quantum_fight(0.3, backend_sim) == 1 and pokemon_def.malus == "None":
                pokemon_def.malus = "paralysis"
                pokemon_def.speed *= 0.5
                print("{} is paralyzed.".format(pokemon_def.name))

    else:
        print("{} miss !".format(pokemon_att.name))
        dommages = 0

    return dommages


def action_attack(attaque, player_att, player_def, backend_sim):
    player_att.action = 0
    thaw = 1
    paralysis = 1

    if player_att.pokemon.malus == "freeze":
        thaw = quantum_fight(0.2, backend_sim)
        if thaw == 1:
            print("{} is thawed.".format(player_att.pokemon.name))
            player_att.pokemon.malus = "None"
        else:
            print("{} is still frozen.".format(player_att.pokemon.name))

    if player_att.pokemon.malus == "paralysis":
        paralysis = quantum_fight(0.75, backend_sim)
        if paralysis == 0:
            print("{} is paralyzed, he cannot attack.".format(player_att.pokemon.name))

    if thaw == 1 and paralysis == 1:
        print("{} is using {}".format(player_att.pokemon.name, attaque.name))
        player_def.pokemon.dommages = player_def.pokemon.dommages + calcul_dommage(attaque, player_att.pokemon,
                                                                               player_def.pokemon, backend_sim)
        if round(player_def.pokemon.pv - player_def.pokemon.dommages) < 0:
            print("{} - 0 / {} pv".format(player_def.pokemon.name, player_def.pokemon.pv))

        else:
            print("{} - {} / {} pv".format(player_def.pokemon.name, round(player_def.pokemon.pv - player_def.pokemon.dommages),
                                        player_def.pokemon.pv))

        if player_def.pokemon.dommages >= player_def.pokemon.pv:
            player_def.pokemon.status = 0
            player_def.action = 0


def control_input(options, input_ctl):
    if input_ctl is not None:
        if 0 <= input_ctl < options:
            return True
    print("Please give a number between 0 and {}.".format(options-1))
    return False


def stats(winner):
    TOKEN = os.environ.get("GITHUB_TOKEN")

    if TOKEN is not None:
        headers = {
            "Accept": "application/vnd.github.v3+json",
            "Authorization": f"token {TOKEN}",
        }

        data = {
            "event_type": "games-stats",
            "client_payload": {
                "game": "qpokemon",
                "winner": f"{winner}"
            }
        }

        r = requests.post(
            url="https://api.github.com/repos/mickahell/robots-data/dispatches",
            headers=headers,
            json=data
        )

    else:
        print("Your token is empty ! The stats aren't updated.")


def team_stats(winner, looser):
    TOKEN = os.environ.get("GITHUB_TOKEN")

    if TOKEN is not None:
        headers = {
            "Accept": "application/vnd.github.v3+json",
            "Authorization": f"token {TOKEN}",
        }

        data = {
            "event_type": "qpokemon-team-stats",
            "client_payload": {
                "winner": [i for i in winner],
                "looser": [i for i in looser]
            }
        }

        r = requests.post(
            url="https://api.github.com/repos/mickahell/robots-data/dispatches",
            headers=headers,
            json=data
        )

    else:
        print("Your token is empty ! The stats aren't updated.")
