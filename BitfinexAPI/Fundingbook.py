import requests



if __name__ == "__main__":
    url = "https://api.bitfinex.com/v1/lendbook/BTC"

    response = requests.request("GET", url)

    print(response.text)