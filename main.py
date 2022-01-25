import requests
import pandas as pd
import numpy as np

url = 'https://fantasy.premierleague.com/api/bootstrap-static/'

r = requests.get(url)

data = pd.read_json(r.json())
