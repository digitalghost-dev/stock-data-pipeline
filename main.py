#!usr/bin/env python

# Importing needed modules.
from load import csv_file, bigquery_upload
from urllib.request import urlopen
from list import ticker_list
from config import api_key
import pandas as pd
import json

# URLs needed to build the API endpoint connection.
base_url = 'https://cloud.iexapis.com/stable/stock/'
quote_url = '/quote/?token='
company_url = '/company?token='

def company_info():
    header_list = ['ticker', 'company', 'price', 'change', 'peRatio']
    sep = " -"
    sep2 = " ("

    # Iterating through all of the tickers to get the data.
    master_list = []
    count = 0
    while count < len(ticker_list):
        ticker = ticker_list[count]

        # Opening and reading the API endpoints.
        with urlopen(f"{base_url}{ticker}{quote_url}{api_key}") as response:
            source = response.read()
            data = json.loads(source)

        # API endpoints used.
        symbol = data["symbol"]
        company = data["companyName"]
        company_stripped = company.split(sep, 1)[0]
        company_stripped = company_stripped.split(sep2, 1)[0]
        price = data["latestPrice"]
        change = data["change"]
        peRatio = data["peRatio"]
    
        # Appending the end point data to the master list.
        info = [symbol, company_stripped, price, change, peRatio]
        master_list.append(info)
        count += 1

        # Removing commas in company names, outputting a CSV file.
        dataframe = pd.DataFrame(master_list)
        dataframe = dataframe.replace(",", "", regex=True)
        dataframe.to_csv('output.csv', header=header_list, index=False)

if __name__ == "__main__":
    company_info()
    # Running the functions from load.py file.
    csv_file()
    bigquery_upload()