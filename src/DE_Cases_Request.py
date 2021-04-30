import json
import requests
from datetime import date

today = str(date.today())
all_url = "https://api.corona-zahlen.org/germany/history/cases"
resp = requests.get(url=all_url)
all_data = resp.json()
with open('/data/%s/DE_cases_history.json'%today, 'w') as f:
    f.write(json.dumps(all_data, indent=4))

all_url = "https://api.corona-zahlen.org/germany/history/incidence"
resp = requests.get(url=all_url)
all_data = resp.json()
with open('/data/%s/DE_incidence_history.json'%today, 'w') as f:
    f.write(json.dumps(all_data, indent=4))

all_url = "https://api.corona-zahlen.org/germany/history/deaths"
resp = requests.get(url=all_url)
all_data = resp.json()
with open('/data/%s/DE_deaths_history.json'%today, 'w') as f:
    f.write(json.dumps(all_data, indent=4))

all_url = "https://api.corona-zahlen.org/germany/history/recovered"
resp = requests.get(url=all_url)
all_data = resp.json()
with open('/data/%s/DE_recovered_history.json'%today, 'w') as f:
    f.write(json.dumps(all_data, indent=4))

daily_url = "https://api.corona-zahlen.org/germany"
resp = requests.get(url=daily_url)
daily_data = resp.json()
with open('/Corona Mining/data/%s/DE_cases.json'%today, 'w') as f:
    f.write(json.dumps(daily_data, indent=4))