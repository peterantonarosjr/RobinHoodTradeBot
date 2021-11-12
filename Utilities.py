import pandas as pd
import robin_stocks.robinhood as r
import robin_stocks.gemini as c
import pandas

#Authenticate Robinhood user (login) for "duration" days
def userLogin(duration):
    credentialFile = open('/home/peterjr/Pycharm-Workspace/RobinHoodTradeBot/RH.txt').read().splitlines()
    EMAIL = credentialFile[0]
    PASSWORD = credentialFile[1]
    try:
        r.login(EMAIL, PASSWORD, expiresIn=duration*86400, store_session=False)
        c.authentication.login(EMAIL, PASSWORD)
        c.authentication.heartbeat(jsonify=None)
        print("Successful Login/Authentication")
    except:
        print("Failed Login/Authentication")

#User logout
def userLogout():
    r.logout()

#Returns available cash for authenticated user
def getLiquidity():
    userAssets = r.load_account_profile()
    liquidity = float(userAssets["portfolio_cash"])
    return liquidity

#Returns the value of all held cryptocurrencies for authenticated user
def getCryptoEquity():
    userAssets = r.load_phoenix_account()
    equity = userAssets["crypto"].get("equity").get("amount")
    return equity

#Get prices for all interested crypto currencies of the authenticated user
def getCryptoPrice(crypto):
    return c.get_price(crypto,side='buy')

#Buy for a particular crypto currency with max overage willing to pay for authenticated user
def buyCrypto(ticker,amount,currentPrice,maxOver):
    cashAvailable = getLiquidity()
    buyLimitPrice = round(currentPrice + maxOver, 2)
    if amount*buyLimitPrice<=cashAvailable:
        r.order_buy_crypto_limit(symbol=ticker,quantity=amount,limitPrice=buyLimitPrice)
    else:
        print("Not enough cash available in account to purchase")

def buyCryptoTEST(ticker,amount,currentPrice,maxOver):
    cashAvailable = getLiquidity()
    buyLimitPrice = round(currentPrice + maxOver, 2)
    print("Bought " + str(amount) + " " + ticker + "@ " + str(buyLimitPrice))


def sellCryptoTEST(ticker,amount,currentPrice,maxUnder):
    sellLimitPrice = round(currentPrice - maxUnder, 2)
    print("Sold " + str(amount) + " " + ticker + "@ " + str(sellLimitPrice))

#Sell for a particular crypto currency with max underage willing to pay for authenticated user
def sellCrypto(ticker,amount,currentPrice,maxUnder):
    sellLimitPrice = round(currentPrice - maxUnder, 2)
    r.order_sell_crypto_limit(symbol=ticker,quantity=amount,limitPrice=sellLimitPrice)

#Returns a list of specified crypto price
def getCryptoHistorical(ticker,interval,length):
    return r.get_crypto_historicals(symbol=ticker, interval=interval, span=length, bounds="24_7")

def initCryptoDataFrame():
    cols = ['date','ticker','price']
    cryptoDataFrame = pd.DataFrame(columns=cols)
    return cryptoDataFrame

def updateCryptoDataFrame(cryptoFrame,date,ticker):
    tickerPrice = getCryptoPrice(ticker)
    cryptoFrame.loc[len(cryptoFrame)] = [date,ticker, tickerPrice]
    return cryptoFrame

def initTradeDataFrame():
    cols = ['date','ticker','price','amount','max_overage','trade_status']
    tradeFrame = pd.DataFrame(columns=cols)
    return tradeFrame

def updateTradeDataFrame(tradeFrame,tradeInfo):
    tradeFrame.loc[len(tradeFrame)] = tradeInfo
    return tradeFrame


#For the crypto historical dataframe this snippet is useful

'''
import schedule
import time

def task():
    print("Do task now")

schedule.every().day.at("15:07").do(task)

while True:
    schedule.run_pending()
    time.sleep(1)
    
'''