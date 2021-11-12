from Utilities import *
import datetime

class Scalping:
    def __init__(self,cryptoDataFrame,cryptoTradeFrame):
        self.cryptoFrame = cryptoDataFrame
        self.tradeFrame = cryptoTradeFrame



    def decideToTrade(self,cryptoFrame,tradeFrame):

        ticker = cryptoFrame.loc[cryptoFrame.index[-1], "ticker"]
        price = cryptoFrame.loc[cryptoFrame.index[-1], "price"]

        if tradeFrame.empty:
            print("Trade Frame is empty")
            buyCryptoTEST(ticker,0.1,float(price),1)

            return [datetime.datetime.now(),ticker,price,0.1,1,"BUY"]

        else:
            buyCryptoTEST(ticker, 0.1, float(price), 1)

            return [datetime.datetime.now(), ticker, price, 0.1, 1, "BUY"]





