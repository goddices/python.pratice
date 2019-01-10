import requests

def request_siweituxin():
    requests.get("http://cmspro.navinfo.com:80/NI/cms/bmw/weather/v1/forecastByLocation4bmw?language=zh_CN&lng=%s&lat=%s&has24hour=true&cata=json&userid=sh_bmw&key=%s")