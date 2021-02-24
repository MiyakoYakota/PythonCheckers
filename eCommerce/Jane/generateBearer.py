import uuid
import requests

GUEST_TOKEN_ENDPOINT="https://login.jane.com/guest-login"


def generateHeaders(authorization=None, deviceId=None, sessionId=None):
    response = {
        "accept-encoding": "gzip",
        "cache-control": "public, max-age=0",
        "connection": "Keep-Alive",
        "content-type": "application/json; charset=UTF-8",
        "authorization": f"Bearer {authorization}",
        "host": "login.jane.com",
        "user-agent": "JaneAndroidInstalled/5.1.2 (Android; 7.1.2; samsung; samsung; SM-G977N)",
        "x-jane-app-name": "jane-android",
        "x-jane-app-version": "5.1.2",
        "x-jane-device-id": str(uuid.uuid4()),
        "x-jane-session-id": str(uuid.uuid4()),
        "x-jane-timezon-offset": "-300"
    }
    if deviceId:
        response['x-jane-device-id'] = deviceId
    if sessionId:
        response['x-jane-session-id'] = sessionId
    return response

def generateLoginBearer():
    response = requests.post(GUEST_TOKEN_ENDPOINT, headers=generateHeaders(), data="")
    try:
        bearer = response.json()['janeAuth']
        print(f'{bearer}')
    except:
        print('Unable to grab new bearer, change your IP address.')
        exit()

generateLoginBearer()
