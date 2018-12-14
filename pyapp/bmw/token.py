import requests
import json

gcdmRootUrl = "customer.bmwgroup.cn:443"
gcdmAuthToken = "Basic blF2NkNxdHhKdVhXUDc0eGYzQ0p3VUVQOjF6REh4NnVuNGNEanliTEVOTjNreWZ1bVgya0VZaWdXUGNRcGR2RFJwSUJrN3JPSg=="
gcdmUser = "8618616392237"
gcdmPassword = "BM667863"
btcapiRootUrl = "myc-profile.bmw.com.cn"
gcdmTokenApi = "https://" + gcdmRootUrl + "/gcdm/oauth/token"
btcapiTokenApi = "http://" + btcapiRootUrl + \
    "/api/Account/ExternalLogin?client_id=self&provider=GCDM&redirect_uri=http%3A//" + \
    btcapiRootUrl + "/&response_type=token"


def getTokenFromGcdm():
    headers = {
        'Authorization': gcdmAuthToken,
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    payload = {"grant_type": "password",
               "username": gcdmUser, "password": gcdmPassword}
    response = requests.post(gcdmTokenApi, data=payload, headers=headers)
    token = None
    if response.status_code == 200:
        token = json.loads(response.text)
    response.close()
    return token


def getTokenFromBtcapi(token):
    btcapiTokenApi2 = "https://" + btcapiRootUrl + \
        "/api/Account/ExternalLogin?provider=GCDM&response_type=token&client_id=self&redirect_uri=https%3A//"+btcapiRootUrl+"/"
    gcdmloginUrl = None
    btcapiCookie = None
    response = requests.get(btcapiTokenApi2)
    if response.status_code == 302:
        gcdmloginUrl = response.headers['Location']
        btcapiCookie = response.headers['Set-Cookie']
    response.close()
    response = requests.get(gcdmloginUrl, headers={
                 'Authorization': token['token_type']+' '+token['access_token']})
    if response.status_code==200:
        #gcdmLoginParams = ($gcdmloginUrl -split "\?")[1] -split "&";
        gcdmLoginParams  = gcdmloginUrl.split('?')[1].split('&')

token = getTokenFromGcdm()
