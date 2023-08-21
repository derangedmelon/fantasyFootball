import pandas as pd
import numpy as np
import json
import DataGrabber as dg
import time


pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

# When required uncomment code to update the statistics
# fStatsUrl = 'https://fantasy.premierleague.com/api/bootstrap-static/'
fgwStatsUrl = 'https://fantasy.premierleague.com/api/element-summary/'
# dg.urltofile(fStatsUrl, "fantasyStats.json")


# Open the statistics file
with open("fantasyStats.json", "r", encoding="utf-8") as f:
    jsonText = f.read()

json = json.loads(jsonText)
print(json.keys())
data = pd.DataFrame(json['elements'])
print(data.keys())

newData = data[['id', 'first_name', 'second_name', 'form', 'team', 'total_points', 'expected_goals', 'expected_assists',
                'now_cost']]

newData['p/v'] = newData['total_points']/newData['now_cost'] * 10
newData.loc[:, 'now_cost'] = newData['now_cost']/10

maxID = newData['id'].max()
print("maxID = ", maxID)

for n in range(0, maxID):
    dg.urltofile(fgwStatsUrl+str(n),
                 "C:/Users/tomk1/PycharmProjects/fantasyFootball2/gameweeks/fantasyGWStats"+str(n)+".json")
    time.sleep(1/40)
    print(n)

# Lookup ID, get and store match history, then plot a graph of the interesting data

print(newData.sort_values(by="p/v", ascending=False).head(20))
newData.sort_values(by="p/v", ascending=False).to_html('temp.html')
