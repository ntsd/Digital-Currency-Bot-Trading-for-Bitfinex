import BitfinexAPI.Symbols
import BitfinexAPI.Candles
import Helpers.CSVSaver

import time


def get_candles():
    symbols = BitfinexAPI.Symbols.getSymbolsV2()
    symbols_to_usd = [s for s in symbols if "USD" in s[0]]
    symbols_to_btc = [s for s in symbols if "BTC" == s[0][4:]]

    candles = BitfinexAPI.Candles.get_candles("tOMGUSD", "30m", "1000")
    Helpers.CSVSaver.listToCSV(candles, "Data/candles_to_btc/{}_{}_{}.csv".format("tOMGUSD", "30m", time.strftime("%m-%d-%y")))

    timeFrameList = ["1m", "5m", "15m", "30m", "1h", "3h", "6h", "12h"]
    # for symbol in symbols_to_usd:
    #     for timeFrame in timeFrameList:
    #         # timeFrame = "1m"
    #         candles = BitfinexAPI.Candles.get_candles(symbol[0], timeFrame, "1000")
    #         Helpers.CSVSaver.listToCSV(candles, "Data/candles_to_btc/{}_{}_{}.csv".format(symbol[0], timeFrame, time.strftime("%m-%d-%y")))


def get_symbol():
    symbols = BitfinexAPI.Symbols.getSymbolsV2()
    symbols_to_usd = [s for s in symbols if "USD" in s[0]]
    symbols_to_btc = [s for s in symbols if "BTC" == s[0][4:]]
    # Helpers.CSVSaver.listToCSV(symbols_to_usd, "symbols_to_usd.csv")
    # Helpers.CSVSaver.listToCSV(symbols_to_btc, "symbols_to_btc.csv")

if __name__ == "__main__":
    get_candles()