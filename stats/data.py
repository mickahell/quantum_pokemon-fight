import os
import requests


def stats(winner):
    TOKEN = os.environ.get("GITHUB_TOKEN")

    if TOKEN is not None:
        headers = {
            "Accept": "application/vnd.github.v3+json",
            "Authorization": f"token {TOKEN}",
        }

        data = {
            "event_type": "games-stats",
            "client_payload": {"game": "qpokemon", "winner": f"{winner}"},
        }

        requests.post(
            url="https://api.github.com/repos/mickahell/robots-data/dispatches",
            headers=headers,
            json=data,
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
                "looser": [i for i in looser],
            },
        }

        requests.post(
            url="https://api.github.com/repos/mickahell/robots-data/dispatches",
            headers=headers,
            json=data,
        )

    else:
        print("Your token is empty ! The stats aren't updated.")
