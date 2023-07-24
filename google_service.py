from Data_pipeline_Tsla import get_data
import gspread

def save_data():
    data = get_data()
    gc = gspread.service_account(filename="./service_account.json")

    wks = gc.open("CAB_P6_Data_pipeline_Tsla").sheet1

    wks.append_row([data["date"],
                    data["close"]])
save_data()