import gspread

gc = gspread.service_account()

# Open a sheet from a spreadsheet in one go
wks = gc.open("CAB_P6_Data_pipeline_Tsla").sheet1

# Update a range of cells using the top left corner address
wks.update('A1', [[1, 2], [3, 4]])

# Or update a single cell
#wks.update('B42', "it's down there somewhere, let me take another look.")

# Format the header
wks.format('A1:B1', {'textFormat': {'bold': True}})



def get_data():
    print("Hello World")
get_data()

