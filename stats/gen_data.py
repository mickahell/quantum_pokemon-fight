from os import path
import pandas as pd


def team_stats(csv, pokemon, has_win):
    file_csv = csv

    csv_file = pd.read_csv(file_csv)

    pokemon_csv = csv_file["pokemon"].tolist()
    win_csv = csv_file["win"].tolist()
    loose_csv = csv_file["loo"].tolist()

    for i in range(len(pokemon_csv)):
        if pokemon == pokemon_csv[i]:
            if has_win == "yes":
                win_csv[i] += 1
            else:
                loose_csv[i] += 1

    csv_file = {"pokemon": pokemon_csv, "win": win_csv, "loo": loose_csv}
    df = pd.DataFrame(csv_file)
    df.to_csv(file_csv, index=False, header=["pokemon", "win", "loo"])


def gen_team_data(pokemon: str, has_win: str):
    current_dir = path.dirname(path.abspath(__file__))
    csv = "{}/data/team_stats.csv".format(current_dir)

    team_stats(csv=str(csv), pokemon=pokemon, has_win=has_win)


def unity_stats(csv, opponent, has_win):
    file_csv = csv

    csv_file = pd.read_csv(file_csv)

    pokemon_csv = csv_file["opponent"].tolist()
    win_csv = csv_file["win"].tolist()
    loose_csv = csv_file["loo"].tolist()

    test = 0
    for i in range(len(pokemon_csv)):
        if opponent == pokemon_csv[i]:
            if has_win == "yes":
                win_csv[i] += 1
            else:
                loose_csv[i] += 1
            test = 1

    if test == 0:
        if has_win == "yes":
            pokemon_csv.append(opponent)
            win_csv.append(1)
            loose_csv.append(0)
        else:
            pokemon_csv.append(opponent)
            win_csv.append(0)
            loose_csv.append(1)

    csv_file = {"opponent": pokemon_csv, "win": win_csv, "loo": loose_csv}
    df = pd.DataFrame(csv_file)
    df.to_csv(file_csv, index=False, header=["opponent", "win", "loo"])


def gen_unity_data(winner: str, looser: str):
    current_dir = path.dirname(path.abspath(__file__))
    csv_winner = "{}/data/{}.csv".format(current_dir, winner)
    if not path.exists(csv_winner):
        with open(csv_winner, "w") as f:
            f.write("opponent,win,loo")
    print("Generate data for : ", winner)
    unity_stats(csv=str(csv_winner), opponent=looser, has_win="yes")

    csv_looser = "{}/data/{}.csv".format(current_dir, looser)
    if not path.exists(csv_looser):
        with open(csv_looser, "w") as f:
            f.write("opponent,win,loo")
    print("Generate data for : ", looser)
    unity_stats(csv=str(csv_looser), opponent=winner, has_win="no")
