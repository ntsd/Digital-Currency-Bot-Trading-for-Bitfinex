import requests
import json

def getSymbolsV2():
    url = "https://api.bitfinex.com/v1/symbols"
    response = requests.request("GET", url)
    list_symbols = json.loads(response.text)
    list_symbols2 = []
    for symbol in list_symbols:
        list_symbols2.append(["t"+symbol.upper()])
    return list_symbols2

if __name__ == "__main__":
    url = "https://api.bitfinex.com/v1/symbols"

    response = requests.request("GET", url)

    list_symbols = json.loads(response.text)
    for symbol in list_symbols:
        print(symbol)
