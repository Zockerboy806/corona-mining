import json
import requests
from datetime import date

today = str(date.today())
all_url = "https://api.corona-zahlen.org/states/history/cases"
resp = requests.get(url=all_url)
all_data = resp.json()
with open('/data/%s/DE_states_cases_history.json'%today, 'w') as f:
    f.write(json.dumps(all_data, indent=4))

all_url = "https://api.corona-zahlen.org/states/history/incidence"
resp = requests.get(url=all_url)
all_data = resp.json()
with open('/data/%s/DE_states_incidence_history.json'%today, 'w') as f:
    f.write(json.dumps(all_data, indent=4))

all_url = "https://api.corona-zahlen.org/states/history/deaths"
resp = requests.get(url=all_url)
all_data = resp.json()
with open('/data/%s/DE_states_deaths_history.json'%today, 'w') as f:
    f.write(json.dumps(all_data, indent=4))

all_url = "https://api.corona-zahlen.org/states/history/recovered"
resp = requests.get(url=all_url)
all_data = resp.json()
with open('/data/%s/DE_states_recovered_history.json'%today, 'w') as f:
    f.write(json.dumps(all_data, indent=4))

daily_url = "https://api.corona-zahlen.org/states"
resp = requests.get(url=daily_url)
daily_data = resp.json()
with open('/data/%s/DE_states.json'%today, 'w') as f:
    f.write(json.dumps(daily_data, indent=4))