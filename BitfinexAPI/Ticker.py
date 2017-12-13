import requests



if __name__ == "__main__":
    url = "https://api.bitfinex.com/v1/pubticker/omgbtc"

    response = requests.request("GET", url)

    print(response.text)