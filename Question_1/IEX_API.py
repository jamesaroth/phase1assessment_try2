
import requests, json

def askticker():
    ticker = input("Please enter a valid stock ticker:")
    return ticker

ticker = askticker()

call = "https://api.iextrading.com/1.0/stock/{symbol}/chart"
params = ""

r = requests.get(call.format(symbol=ticker))
data = r.json()
filename = "{}_chart.json".format(ticker.upper())
with open(filename, "w") as f:
    json.dump(data, f)




