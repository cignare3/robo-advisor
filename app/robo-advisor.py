# app/robo_advisor.py
import csv
import datetime
import json
import os
import requests

#from dotenv import load_dotenv

#load_dotenv()

#request_url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={stock_symbol}&apikey={API_KEY}"
request_url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=MSFT&apikey=P40N2DKCG8YHQQB4"
response = requests.get(request_url)
#print(type(response))
#print(response.status_code)
#print(response.text)

parsed_response = json.loads(response.text)


last_refreshed = parsed_response["Meta Data"]["3. Last Refreshed"]

#breakpoint()

#stock_symbol = input("Please enter stock symbol: ")
#if stock_symbol.isalpha():  
   


    
#else:
  #  Print("Oh, expecting a properly-formed stock symbol like 'MSFT'. Please try again.")

print("-------------------------")
print("SELECTED SYMBOL: XYZ")
print("-------------------------")
print("REQUESTING STOCK MARKET DATA...")
print(f"REQUEST AT: {last_refreshed}")
print("-------------------------")
print("LATEST DAY: 2018-02-20")
print("LATEST CLOSE: $100,000.00")
print("RECENT HIGH: $101,000.00")
print("RECENT LOW: $99,000.00")
print("-------------------------")
print("RECOMMENDATION: BUY!")
print("RECOMMENDATION REASON: TODO")
print("-------------------------")
print("HAPPY INVESTING!")
print("-------------------------")