import json
import requests
from datetime import date

today = str(date.today())
all_url = "https://api.corona-zahlen.org/testing/history"
resp = requests.get(url=all_url)
all_data = resp.json()
with open('/data/%s/DE_testing_history.json'%today, 'w') as f:
    f.write(json.dumps(all_data, indent=4))