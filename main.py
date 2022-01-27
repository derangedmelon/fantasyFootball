import requests
import pandas as pd
import numpy as np
import json

url = 'https://fantasy.premierleague.com/api/bootstrap-static/'

r = requests.get(url)
json = r.json()
print(json.keys())
data = pd.DataFrame(json['elements'])

print(data.head())
