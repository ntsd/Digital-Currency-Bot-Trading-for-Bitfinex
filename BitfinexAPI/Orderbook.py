import requests



if __name__ == "__main__":
    url = "https://api.bitfinex.com/v2/book/tOMGBTC/P0"

    response = requests.request("GET", url)

    print(response.text)