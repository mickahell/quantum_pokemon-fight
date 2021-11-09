import src.ia
import src.function
from src.class_custom.pokemon import Pokemon
from random import *


def team(me, him, nb_team):
    # Choose of poké
    for i in range(nb_team):
        pokemon_j1 = randint(0, len(Pokemon.pokedex) - 1)
        me.team.append(Pokemon.pokedex[pokemon_j1])
        Pokemon.pokedex.remove(Pokemon.pokedex[pokemon_j1])
        pokemon_j2 = randint(0, len(Pokemon.pokedex) - 1)
        him.team.append(Pokemon.pokedex[pokemon_j2])
        Pokemon.pokedex.remove(Pokemon.pokedex[pokemon_j2])

    for i, y in zip(me.team, him.team):
        me.register_team.append(i.name)
        him.register_team.append(y.name)

    print("-----------------------------------------------------------")
    me.addFirst(me.team[randint(0, 2)])
    him.addFirst(him.team[randint(0, 2)])


def battle(me, him):
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

        action_j1 = ia.quantum_action(me.pokemon, him.pokemon, qc_type, backend_sim)
        if action_j1 == 0 or len(me.team) == 1:
            attack_j1 = ia.quantum_attaq(me.pokemon, him.pokemon, qc_type, backend_sim)
        else:
            copy_team = []
            for i in me.team:
                if i != me.pokemon:
                    copy_team.append(i)
            next_poke = ia.quantum_switch(copy_team, him.pokemon, qc_type, backend_sim)
            me.addFirst(copy_team[next_poke])
            me.action = 0
        print("-----------------------------------------------------------")

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
                    if len(me.team) > 1:
                        next_poke = ia.quantum_switch(me.team, him.pokemon, qc_type, backend_sim)
                    else:
                        next_poke = 0
                    me.addFirst(me.team[next_poke])
                    print("{} call {}".format(me.name, me.pokemon.name))
                else:
                    print("{} won !".format(him.name))
                    print("GAME OVER !")
                    return him, me
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
                    return me, him
