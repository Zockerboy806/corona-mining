import json
import requests
from datetime import date

today = str(date.today())
daily_url = "https://data.cdc.gov/api/views/9mfq-cb36/rows.json?accessType=DOWNLOAD"
resp = requests.get(url=daily_url)
daily_data = resp.json()
with open('/Corona Mining/data/%s/US_data.json'%today, 'w') as f:
    f.write(json.dumps(daily_data, indent=4))