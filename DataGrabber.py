import requests
import pandas as pd


def urlToFile(url, file):
    r = requests.get(url)

    with open(file, "w", encoding="utf-8") as f:
        f.write(r.text)

base_url = 'https://fantasy.premierleague.com/api/'
fStatsUrl = 'https://fantasy.premierleague.com/api/bootstrap-static/'

urlToFile(fStatsUrl, "fantasyStats.json")

fGameWeek = base_url + 'element-summary/4/'

urlToFile(fGameWeek, 'fGW.json')
