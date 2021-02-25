import requests
import queue

PUBLISH_URL="https://events.jane.com/events/v3/publish"
PAYMENT_ENDPOINT="https://paymentsv2.jane.com/customer"

#def generateActionPayload(deviceId):


def generateHeaders(authorization, deviceId=None, sessionId=None):
    return {
        "accept-encoding": "gzip",
        "authorization": f"Bearer {authorization}",
        "cache-control": "public, max-age=0",
        "content-type": "application/json; charset=UTF-8",
        "host": "login.jane.com",
        "user-agent": "JaneAndroidInstalled/5.1.2 (Android; 7.1.2; samsung; samsung; SM-G977N)",
        "x-jane-app-name": "jane-android",
        "x-jane-app-version": "5.1.2",
        "x-jane-device-id": deviceId,
        "x-jane-session-id": sessionId,
        "x-jane-timezon-offset": "-300"
    }

def getBalance(janeAuth, deviceId, sessionId, proxyUrl):
    returnString = ""
    paymentResponse = requests.get(PAYMENT_ENDPOINT, proxies=proxyUrl, headers=generateHeaders(janeAuth, deviceId, sessionId)).json()
    returnString += f"Balance: ${paymentResponse['janeCreditBalance']} | "
    if paymentResponse['creditCards']:
        for paymentMethod in paymentResponse['creditCards']:
            returnString += paymentMethod['cardType'] + "*"
            returnString += paymentMethod['maskedNumber'] + f" ({paymentMethod['expirationMonth']}/{paymentMethod['expirationYear']}) | "
    if paymentResponse['payPalAccounts']:
        for payPal in paymentResponse['payPalAccounts']:
            returnString += f"Paypal {payPal['email']}"
    return returnString[:-2]
