import urllib3
import json
def get_data():
    http = urllib3.PoolManager()
    url = "https://cloud.iexapis.com/stable/stock/tsla/previous?token=pk_7801f2603ff44dc882336198248c9419"
    resp = http.request("GET", url)
    values = json.loads(resp.data)
    print(values)
    return values
get_data()

import gspread

def save_data():
    data = get_data()
    gc = gspread.service_account(filename="./service_account.json")

    wks = gc.open("DPL").sheet1

    wks.append_row([data["date"],
                    data["close"]])
save_data()

