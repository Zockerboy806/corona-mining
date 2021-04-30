import json
import requests
from datetime import date

today = str(date.today())
all_url = "https://covid19-brazil-api.now.sh/api/report/v1/countries"
resp = requests.get(url=all_url)
all_data = resp.json()
with open('/data/%s/All_Countries.json'%today, 'w') as f:
    f.write(json.dumps(all_data, indent=4))