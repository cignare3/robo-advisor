# app/robo_advisor.py
import csv
import datetime
import json
import os
import requests

def to_usd(my_price):
    return "${0:,.2f}".format(my_price)

#from dotenv import load_dotenv

#load_dotenv()

#request_url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={stock_symbol}&apikey={API_KEY}"
request_url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=MSFT&apikey=P40N2DKCG8YHQQB4"
response = requests.get(request_url)
#print(type(response))
#print(response.status_code)
#print(response.text)

parsed_response = json.loads(response.text)
#print(parsed_response)


last_refreshed = parsed_response["Meta Data"]["3. Last Refreshed"]
tsd = parsed_response["Time Series (Daily)"]
dates = list(tsd.keys()) #assume latest day is first, may want to sort
latest_date = dates[0]
close_price = tsd[latest_date]["4. close"]

#maximum of all high prices
high_prices = []
low_prices = []
for date in dates:
    high_price = tsd[date]["2. high"]
    high_prices.append(float((high_price)))
    low_price = tsd[date]["3. low"]
    low_prices.append(float((low_price)))

recent_high = max(high_prices)
recent_low = min(low_prices)


#breakpoint()

#stock_symbol = input("Please enter stock symbol: ")
#if stock_symbol.isalpha():  
   
csv_file_path = os.path.join(os.path.dirname(__file__), "..", "data", "prices.csv")

csv_headers = ["timestamp", "open", "high", "low", "close", "volume"]

with open(csv_file_path, "w") as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=csv_headers)
    writer.writeheader() # uses fieldnames set above

    #looping
    writer.writerow({
        "timestamp": "TODO", 
        "open": "TODO",
        "high": "TODO",
        "low": "TODO",
        "close": "TODO"
        })

    
#else:
  #  Print("Oh, expecting a properly-formed stock symbol like 'MSFT'. Please try again.")

print("-------------------------")
print("SELECTED SYMBOL: XYZ")
print("-------------------------")
print("REQUESTING STOCK MARKET DATA...")
print(f"REQUEST AT: XXXX")
print("-------------------------")
print(f"LATEST DAY: {last_refreshed}")
print(f"LATEST CLOSE: {to_usd(float(close_price))}")
print(f"RECENT HIGH: {to_usd(float(recent_high))}")
print(f"RECENT LOW: {to_usd(float(recent_low))}")
print("-------------------------")
print("RECOMMENDATION: BUY!")
print("RECOMMENDATION REASON: TODO")
print("-------------------------")
print(f"WRITING DATA TO CSV... {csv_file_path}")
print("-------------------------")
print("HAPPY INVESTING!")
print("-------------------------")


