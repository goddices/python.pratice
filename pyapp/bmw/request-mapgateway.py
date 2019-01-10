import csv
import requests


def request100():
    headers = { 
        'Cache-Control':'no-cache',
        'ocp-apim-subscription-key':'4be77952d6fe4f25a5e398fd84c77965',
        'Content-Type':'application/json',
        'Authorization':'Bearer _ErEZEfriSeHaOVA21oVejs14wByg8n9tEIOK04bRWAnfY5bZCv_1E_lsXRm4t8v2jwcSlHDf3uRudZSr5rHj-5q2_BQpvCrKDnfX8dFnFsv6ad-kvunEWewKH7OHhOukoyXI32u9dUXr5FtlbPLGrTdXqHymlI3jB63Hfs5f4m9FKqHrKEoczs10s31LMpnb0hKKBdE0tkb2oc1mzTdTKvBrZS8YnX-ZphetCqX_12lhzfjmyCMVO8wipvfN8U3MHXFh3q9x3VTUbag_tfTQZPoD6fpIUM4Y4rMadeRCIgIowOP7hzptLPMgW4ylGnXICUkSecHLbpIlhZhJxDdjqsA4womzC7dq4xjwUtWAPn72ESdi3m8VZSaTTq1YYUuXxL1dFLVG8p2q7Ypd_TH1YpyUu6n58CgafHa87gKX1lNv6cJVETLkY6GrU9tksCy5bP71dm04yMDSOgU5JM9Lv3tLLn_u9gnnXGWMcHJrd0fkMZT3ToC_3Gza-WRQYglJmR2yCXfnCwkou10kn-lNtuiT3pZ08QWRrf_MKcAFZHnGCXKKt1NPmGsVXX1HAWyEJfNE_T_3h0Uqfojn0DeuWLIt4v9mxAaWu77vHo0xNVkQFKsZVQemv-yhL12faWpqsQNYWmy_4IYQMrMG8ANOyEGn7WU_CYARWcdo7nLfMn7Wcp3b8_catEeiI22NvkZwABgfpydXCVDI1I1Q0GjKa7AijwMmnZvAmMUYFbbVbaFrJJD73b3Zw40_dznKLGHN1SfNFsKvBph0Z1DrEQYnNuDc2rLaSTr93hB99HsL5TGDfrGqH1NfGrwwFXmmfYTDGUiDkVPKby7U36jkvTG80NtC5gWJTu2CBlbSdEtC1k'
    }
    response = requests.post(
        'https://mapgatewaydev.chinacloudsites.cn/api/gateway/context-motorist/v1/motorist/8c8e96bf-0558-4e49-b400-0672f5c40e0c/agents'  ,  
         headers = headers,
         data = '{"acceptLanguage":"zh-CN","appId":"de.bmw.connected.cn.dev","brand":"bmw","platform":"android","pushHandle":"451fa9c49d3a53b444edb184d5bcef3ef8d231fa","sessionState":"login"}'
    )
    
    return response
    
print('ready to work..')
try:
    for i in range(2):
        print(i,request100())

except Exception as err:
    print(err)
else:
    print('work complete..')