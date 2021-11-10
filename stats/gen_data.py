from os import path
import pandas as pd


def team_stats(csv, pokemon, has_win):
    file_csv = csv

    pokemon_csv = []
    win_csv = []
    loose_csv = []

    csv_file = pd.read_csv(file_csv, header=None)

    for data in range(len(csv_file[0])):
        pokemon_csv.append(csv_file[0][data])
        win_csv.append(csv_file[1][data])
        loose_csv.append(csv_file[2][data])

    for i in range(len(pokemon_csv)):
        if pokemon == pokemon_csv[i]:
            if has_win == "yes":
                win_csv[i] += 1
            else:
                loose_csv[i] += 1

    csv_file = {"pokemon": pokemon_csv, "win": win_csv, "loose": loose_csv}
    df = pd.DataFrame(csv_file)
    df.to_csv(file_csv, index=False, header=None)


def gen_team_data(pokemon: str, has_win: str):
    current_dir = path.dirname(path.abspath(__file__))
    with open(
        "{}/team_stats.csv".format(current_dir), "r"
    ) as csv:
        team_stats(csv=str(csv), pokemon=pokemon, has_win=has_win)
