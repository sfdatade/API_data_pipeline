import urllib3
import json
def get_data():
    http = urllib3.PoolManager()
    url = "https://cloud.iexapis.com/stable/stock/tsla/previous?token=<YOUR_TOKEN_HERE>"
    resp = http.request("GET", url)
    values = json.loads(resp.data)
    print(values)
    return values
get_data()