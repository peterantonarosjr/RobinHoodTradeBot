import robin_stocks.robinhood as r
import robin_stocks.gemini as c
import datetime
import time

def login(numOfDays):
    seconds = 60
    secPerMinute = seconds * 60
    secPerHour = secPerMinute * 60
    secPerDay = secPerHour * 24
    loginDuration = numOfDays * secPerDay

    credentialFile = open('/home/peterjr/Pycharm-Workspace/RobinHoodTradeBot/RH.txt').read().splitlines()
    EMAIL = credentialFile[0]
    PASSWORD = credentialFile[1]
    KEY = credentialFile[2]

    try:
        r.login(EMAIL, PASSWORD, expiresIn=loginDuration, store_session=False)
        c.authentication.login(EMAIL, PASSWORD)
        c.authentication.heartbeat(jsonify=None)
        print("Successful Login/Authentication")
    except:
        print("Failed Login/Authentication")

# User logout
def logout():
    r.logout()


def main(loginDuration,mainUpdateDelta):
    #Times relevant to login and login duration
    login(loginDuration)
    loginTime = datetime.datetime.now()
    logoutTime = loginTime + datetime.timedelta(loginDuration)
    currentTime = datetime.datetime.now()

    while currentTime < logoutTime:
        #Do stuff here

        time.sleep(mainUpdateDelta)
        currentTime = datetime.datetime.now()
        pass

    logout()

if __name__ == "__main__":
    # Input # days login, # seconds update delta
    main(1,5)