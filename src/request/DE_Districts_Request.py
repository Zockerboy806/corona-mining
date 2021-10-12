import json
import requests
from datetime import date

today = str(date.today())
all_url = "https://api.corona-zahlen.org/districts/history/cases"
resp = requests.get(url=all_url)
all_data = resp.json()
with open('/data/%s/DE_districts_cases_history.json'%today, 'w') as f:
    f.write(json.dumps(all_data, indent=4))

all_url = "https://api.corona-zahlen.org/districts/history/incidence"
resp = requests.get(url=all_url)
all_data = resp.json()
with open('//data/%s/DE_districts_incidence_history.json'%today, 'w') as f:
    f.write(json.dumps(all_data, indent=4))

all_url = "https://api.corona-zahlen.org/districts/history/deaths"
resp = requests.get(url=all_url)
all_data = resp.json()
with open('/data/%s/DE_districts_deaths_history.json'%today, 'w') as f:
    f.write(json.dumps(all_data, indent=4))

all_url = "https://api.corona-zahlen.org/districts/history/recovered"
resp = requests.get(url=all_url)
all_data = resp.json()
with open('/data/%s/DE_districts_recovered_history.json'%today, 'w') as f:
    f.write(json.dumps(all_data, indent=4))

daily_url = "https://api.corona-zahlen.org/districts"
resp = requests.get(url=daily_url)
daily_data = resp.json()
with open('/data/%s/DE_districts.json'%today, 'w') as f:
    f.write(json.dumps(daily_data, indent=4))