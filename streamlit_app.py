import gspread
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import json
import os

# Define the get_data() function to fetch the values from your Google Spreadsheet.

def get_data():

# Authenticate with Google Sheets API
gc = gspread.service_account(filename='C:\Users\sfmol\Dropbox\CAB\VSCode_GitHub\API_data_pipeline\streamlit_app.py')

# Open the spreadsheet
spreadsheet = gc.open('CAB_P6_Data_pipeline_Tsla')

# Select the worksheet
worksheet = spreadsheet.sheet1

# Get all values from the worksheet as a list of lists
data = worksheet.get_all_values()

# Create a pandas DataFrame from the data
df = pd.DataFrame(data[1:], columns=data[0])

return df
