import requests
import pandas as pd


# Grabs data from a website and writes it to a file
def urltofile(url, file):
    r = requests.get(url)

    with open(file, "w", encoding="utf-8") as f:
        f.write(r.text)


base_url = 'https://fantasy.premierleague.com/api/'
fStatsUrl = 'https://fantasy.premierleague.com/api/bootstrap-static/'


# Example of use
# urltofile(fStatsUrl, "fantasyStats.json")
