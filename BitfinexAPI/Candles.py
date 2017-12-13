import requests
import json

# Response Details
# MTS	int	millisecond time stamp
# OPEN	float	First execution during the time frame
# CLOSE	float	Last execution during the time frame
# HIGH	float	Highest execution during the time frame
# LOW	float	Lowest execution during the timeframe
# VOLUME	float	Quantity of symbol traded within the timeframe


def get_candles(symbol, time_frame, limit):
    url = "https://api.bitfinex.com/v2/candles/trade:{}:{}/hist?limit={}&sort=-1".format(time_frame, symbol, limit)
    response = requests.request("GET", url)
    candles_list = json.loads(response.text)
    return candles_list[::-1]

if __name__ == "__main__":
    timeFrame = "1m"
    symbol = "tOMGBTC"
    limit = "100"
    url = "https://api.bitfinex.com/v2/candles/trade:{}:{}/hist?limit={}".format(timeFrame, symbol, limit)

    response = requests.request("GET", url)

    print(response.text)
