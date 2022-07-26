#!usr/bin/env python

# Importing needed modules.
from urllib.request import urlopen
from config import api_key, uri
from list import ticker_list
from bq_update import *
import pandas as pd
import subprocess
import json
import time

# Starting the program run timer.
start_time = time.time()

# URLs needed to build the API endpoint connection.
base_url = 'https://cloud.iexapis.com/stable/stock/'
quote_url = '/quote/?token='
company_url = '/company?token='

def company_info():
    header_list = ['Ticker', 'Company', 'Price', 'PercentChange']

    # Iterating through all of the tickers to get the data.
    master_list = []
    count = 0
    while count < len(ticker_list):
        ticker = ticker_list[count]

        # Opening and reading the API endpoints.
        with urlopen("{}{}{}{}".format(base_url, ticker, quote_url, api_key)) as response:
            source = response.read()
            data = json.loads(source)

        # API endpoints used.
        symbol = data["symbol"]
        company = data["companyName"]
        price = data["latestPrice"]
        change = data["change"]
    
        # Appending the end point data to the master list.
        info = [symbol, company, price, change]
        master_list.append(info)
        count += 1
        
        # Removing commas in company names, outputting a CSV file.
        dataframe = pd.DataFrame(master_list)
        dataframe = dataframe.replace(",", "", regex=True)
        dataframe.to_csv('output.csv', header=header_list, index=False)

if __name__ == "__main__":
    company_info()

# Printing out how long it took the file to run.
print("Code ran for:", time.time() - start_time, "seconds.")

# Running a shell command to upload to Cloud Storage.
subprocess.run(["gsutil cp *.csv " + uri], shell=True)

# Running the function from bq_update file.
bigqueryupload()