import pandas as pd
import numpy as np
import json


with open("fantasyStats.json", "r", encoding="utf-8") as f:
    jsonText = f.read()

json = json.loads(jsonText)
print(json.keys())
data = pd.DataFrame(json['elements'])

print(list(data))
print(data.head())
newData = data[['first_name', 'second_name', 'form', 'team', 'total_points']]


print(newData.sort_values(by="form", ascending=False).head(10))
