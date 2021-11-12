from TradeIndicators.Scalping import Scalping
from Utilities import *
import datetime
import time

def main(loginDuration,mainUpdateDelta):
    #Times relevant to login and login duration
    userLogin(loginDuration)
    loginTime = datetime.datetime.now()
    logoutTime = loginTime + datetime.timedelta(loginDuration)
    currentTime = datetime.datetime.now()

    #Crypto of Interest
    cryptoR = "ETH"
    cryptoC = "ETHUSD"

    cryptoDataFrame = initCryptoDataFrame()
    tradeDataFrame = initTradeDataFrame()
    scalper = Scalping(cryptoDataFrame,tradeDataFrame)


    while currentTime < logoutTime:
        #cryptoDataFrame = updateCryptoDataFrame(cryptoDataFrame)
        #Trading Logic Here
        #
        #
        cryptoDataFrame = updateCryptoDataFrame(cryptoDataFrame, datetime.datetime.now(), cryptoC)

        trade = scalper.decideToTrade(cryptoDataFrame,tradeDataFrame)
        if trade[5]== "BUY":
            tradeDataFrame = updateTradeDataFrame(tradeDataFrame,trade)

        pd.set_option('display.max_rows', 500)
        pd.set_option('display.max_columns', 500)
        pd.set_option('display.width', 150)
        print(tradeDataFrame)
        time.sleep(mainUpdateDelta)
        currentTime = datetime.datetime.now()

    userLogout()

if __name__ == "__main__":
    # Input # days login, # seconds update delta
    main(1,5)