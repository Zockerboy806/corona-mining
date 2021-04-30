import requests
import json
from datetime import date

today = str(date.today())
legend_url = "https://api.corona-zahlen.org/map/districts/legend"
resp = requests.get(url=legend_url)
all_data = resp.json()
with open('/data/%s/DE_legend_districts_history.json'%today, 'w') as f:
    f.write(json.dumps(all_data, indent=4))

map_url = "https://api.corona-zahlen.org/map/districts"
heatmap = requests.get(map_url)
with open('/data/%s/DE_districts_heatmap.png'%today, 'wb') as f:
    f.write(heatmap.content)

legend_url = "https://api.corona-zahlen.org/map/states/legend"
resp = requests.get(url=legend_url)
all_data = resp.json()
with open('/data/%s/DE_legend_states_history.json'%today, 'w') as f:
    f.write(json.dumps(all_data, indent=4))

map_url = "https://api.corona-zahlen.org/map/states"
heatmap = requests.get(map_url)
with open('/data/%s/DE_states_heatmap.png' %today, 'wb') as f:
    f.write(heatmap.content)

