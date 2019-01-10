import requests
import datetime
import hmac
import hashlib
import base64

APIURI_0 = "http://cmspro.navinfo.com/NI/cms/bmw/weather/v1/forecastByLocation4bmw"
DATATYPE = "json"
USERID = "sh_bmw"
SECRETKEY = "523a8fdda97e45e6"


def signKey(data):
    sign = hmac.new(SECRETKEY.encode("utf-8"),
                    data.encode("utf-8"), hashlib.sha1).digest()
    return base64.b64encode(sign).decode("utf-8").replace("+", "-").replace("/", "-")


def forecastByLocation(lng, lat):
    uri = getUri(lng, lat)
    print('四维图新请求地址:', uri)
    response = requests.get(uri, headers={'Accept-Language': 'zh_CN'})
    resp_text = response.text
    print('四维图新响应文本:', resp_text)
    response.close()
    return resp_text


def getUri(lng, lat):
    dts = getUTC_timeformat()
    param = ("lng=%s&lat=%s&dateTime=%s&cata=%s&userid=%s") % (
        lng, lat, dts, DATATYPE, USERID)
    key = signKey(param)
    return APIURI_0 + "?" + param + "&key="+key


def getUTC_timeformat():
    now = datetime.datetime.utcnow()
    return now.strftime('%Y-%m-%dT%H%%3A%M%%3A%SZ')


forecastByLocation(121.43333, 31.5)
