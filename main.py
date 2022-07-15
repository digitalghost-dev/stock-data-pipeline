from urllib.request import urlopen
from config import api_key, uri
import pandas as pd
import subprocess
import requests
import json
import time

# Pretend to be a browser.
headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36", "X-Requested-With": "XMLHttpRequest"}

start_time = time.time()

url_wiki = "https://en.wikipedia.org/wiki/List_of_S%26P_500_companies"

req = requests.get(url_wiki, headers = headers)
table = pd.read_html(req.text, attrs = {'id':'constituents'})

first_col = table[0]['Symbol']

companies = []
for ticker in first_col:
    companies.append(ticker.lower())

sorted_list = sorted(companies)

url = 'https://cloud.iexapis.com/stable/stock/'
url_2 = '/quote/?token='
key = api_key

def company_info():
    header_list = ['Ticker', 'Company', 'Price', 'PercentChange']

    list_of_companies = []
    count = 0
    while count < len(sorted_list):
        ticker = sorted_list[count]

        with urlopen(url + ticker + url_2 + key) as response:
            source = response.read()
            data = json.loads(source)

        symbol = data["symbol"]
        company = data["companyName"]
        price = data["latestPrice"]
        change = data["change"]
    
        info = [symbol, company, price, change]
        list_of_companies.append(info)
        count += 1
        
        dataframe = pd.DataFrame(list_of_companies)
        dataframe = dataframe.replace(",", "", regex=True)
        dataframe.to_csv('output.csv', header=header_list, index=False)

if __name__ == "__main__":
    company_info()

print("Code ran for:", time.time() - start_time, "seconds.")

subprocess.run(["gsutil cp *.csv " + url], shell=True)