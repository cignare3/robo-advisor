# app/robo_advisor.py
import csv
import datetime
import json
import os
import requests

def to_usd(my_price):
    return "${0:,.2f}".format(my_price)

from dotenv import load_dotenv
load_dotenv()

while True:
    stock_symbol = input("Please enter stock symbol: ")
    if len(stock_symbol) > 5:
     print("Stock symbol input too long, expecting a ticker no more than 5 characters")
    elif stock_symbol.isalpha():
        break
    else:    
        print("Input should not contains numbers.  Expecting a properly formatted symbol like 'MSFT'.  Please try again.")

API_KEY = os.environ.get("ALPHADVANTAGE_API_KEY")
request_url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={stock_symbol}&apikey={API_KEY}"
response = requests.get(request_url)
response_message = response.text

if "Error" in response_message:
        print("Invalid Stock Symbol please try again")
        quit()


parsed_response = json.loads(response.text)

last_refreshed = parsed_response["Meta Data"]["3. Last Refreshed"]
tsd = parsed_response["Time Series (Daily)"]
dates = list(tsd.keys())
sorted(dates)   #assume latest day is first, may want to sort
latest_date = dates[0]
close_price = tsd[latest_date]["4. close"]

high_prices = []
low_prices = []
for date in dates:
    high_price = tsd[date]["2. high"]
    high_prices.append(float((high_price)))
    low_price = tsd[date]["3. low"]
    low_prices.append(float((low_price)))

recent_high = max(high_prices)
recent_low = min(low_prices)
   
csv_file_path = os.path.join(os.path.dirname(__file__), "..", "data", "prices.csv")

csv_headers = ["timestamp", "open", "high", "low", "close", "volume"]

with open(csv_file_path, "w") as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=csv_headers)
    writer.writeheader() # uses fieldnames set above
    for date in dates:
        daily_prices = tsd[date]


    #looping
        writer.writerow({
            "timestamp": date, 
            "open": daily_prices["1. open"],
            "high": daily_prices["2. high"],
            "low": daily_prices["3. low"],
            "close": daily_prices["4. close"],
            "volume": daily_prices["5. volume"]
        })


now = datetime.datetime.now()


print("-------------------------")
print(f"SELECTED SYMBOL: {stock_symbol}")
print("-------------------------")
print("REQUESTING STOCK MARKET DATA...")
print("REQUEST AT: " + now.strftime("%Y-%m-%d %I:%M:%S %p"))
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


