import pandas as pd
import numpy as np
import json
import DataGrabber as dg
import time
import matplotlib.pyplot as plt


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

jsont = json.loads(jsonText)
print(jsont.keys())
data = pd.DataFrame(jsont['elements'])
print(data.keys())

newData = data[['id', 'first_name', 'second_name', 'form', 'team', 'total_points', 'expected_goals', 'expected_assists',
                'now_cost']]

newData['p/v'] = newData['total_points']/newData['now_cost'] * 10
newData.loc[:, 'now_cost'] = newData['now_cost']/10

maxID = newData['id'].max()
print("maxID = ", maxID)

# When required uncomment code to update gameweek data
#for n in range(0, maxID):
#    dg.urltofile(fgwStatsUrl+str(n),
#                 "C:/Users/tomk1/PycharmProjects/fantasyFootball2/gameweeks/fantasyGWStats"+str(n)+".json")
#    time.sleep(1/40)
#    print(n)

# Plot player gameweek history data
n = 140
with open("C:/Users/tomk1/PycharmProjects/fantasyFootball2/gameweeks/fantasyGWStats" + str(n) + ".json",
          "r", encoding="utf-8") as fg:
    jsonGWText = fg.read()

jsonGW = json.loads(jsonGWText)
print(jsonGW.keys())
gwData = pd.DataFrame(jsonGW['history'])
print(gwData.keys())

newGWData = gwData[['element', 'fixture', 'goals_scored', 'assists', 'minutes', 'total_points']]


print(newData.sort_values(by="p/v", ascending=False).head(20))
print(newGWData)

# Plot GW points for a player
plotGWData = newGWData[['total_points']]
plt.plot(plotGWData)
plt.show()


newData.sort_values(by="p/v", ascending=False).to_html('temp.html')
