import json
import requests
from datetime import date

today = str(date.today())
all_url = "https://api.corona-zahlen.org/vaccinations/history"
resp = requests.get(url=all_url)
all_data = resp.json()
with open('C:/Corona Mining/data/%s/DE_vaccine_history.json'%today, 'w') as f:
    f.write(json.dumps(all_data, indent=4))

daily_url = "https://api.corona-zahlen.org/vaccinations"
resp = requests.get(url=daily_url)
daily_data = resp.json()
with open('C:/Corona Mining/data/%s/DE_vaccine.json'%today, 'w') as f:
    f.write(json.dumps(daily_data, indent=4))
