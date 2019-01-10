import requests

print('ready to work..')

headers = {
    "Host": "localhost:2053",
    "X-Forwarded-For": "114.66.81.100:61996",
    "DISGUISED-HOST": "localhost:2053",
    "Connection": "Keep-Alive",
    "Max-Forwards": "10",
    "CLIENT-IP": "114.66.81.100:61996",
    "WAS-DEFAULT-HOSTNAME": "bmwentportalint.chinacloudsites.cn",
    "User-Agent": "Jersey/2.25.1.payara-p3,(Apache HttpClient 4.5)",
    "Accept": "application/xml",
    "X-Original-URL": "/api/gateway/omc-products-management/760a0367-b6dd-45d5-99ae-a29ded41def1/products",
    "X-Forwarded-Proto": "http",
    "Accept-Encoding": "gzip, deflate",
    "X-ARR-SSL": "2048|256|C=BE, O=GlobalSign nv-sa, CN=GlobalSign Organization Validation CA - SHA256 - G2|C=DE, S=Bavaria, L=Munich, O=Bayerische Motoren Werke AG, CN=connected-int.bmw.com.cn",
    "IS-SERVICE-TUNNELED": "0",
    "Content-Type": "application/xml",
    "X-SITE-DEPLOYMENT-ID": "bmwentportalint",
    "X-ARR-LOG-ID": "0a0eca96-d899-4317-8518-1dc1f3e661ff",
    "X-WAWS-Unencoded-URL": "/api/gateway/omc-products-management/760a0367-b6dd-45d5-99ae-a29ded41def1/products",
    #"Transfer-Encoding": "chunked",
    "Content-Length": "0"
}


payload = "<?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"yes\"?><order><X-Omc-Api-Key>701c2884-711a-4eff-a214-422156245417</X-Omc-Api-Key><listOfProducts><product><offerCode>SMARTACCESPRO</offerCode><startDate>2018-12-21T03:26:03.926Z</startDate><endDate>2019-12-21T23:59:59.926Z</endDate><longVin>WBACR6108KLB11160</longVin><productId>SMART_ACCESS_Pro</productId><quantity>1</quantity></product><product><offerCode>SMARTACCESPRO</offerCode><startDate>2018-12-21T02:19:53.442Z</startDate><endDate>2018-12-21T03:24:58.934Z</endDate><longVin>WBACR6108KLB11160</longVin><productId>SMART_ACCESS_Pro</productId><quantity>1</quantity></product><product><offerCode>SMARTACCESPRO</offerCode><startDate>2018-12-20T08:48:10.132Z</startDate><endDate>2018-12-21T02:17:05.769Z</endDate><longVin>WBACR6108KLB11160</longVin><productId>SMART_ACCESS_Pro</productId><quantity>1</quantity></product><product><offerCode>SMARTACCESPRO</offerCode><startDate>2018-12-20T06:56:49.950Z</startDate><endDate>2018-12-20T08:47:12.375Z</endDate><longVin>WBACR6108KLB11160</longVin><productId>SMART_ACCESS_Pro</productId><quantity>1</quantity></product><product><offerCode>SMARTACCESPRO</offerCode><startDate>2018-12-20T02:46:06.460Z</startDate><endDate>2018-12-20T06:56:12.789Z</endDate><longVin>WBACR6108KLB11160</longVin><productId>SMART_ACCESS_Pro</productId><quantity>1</quantity></product><product><offerCode>SMARTACCESPRO</offerCode><startDate>2018-10-24T03:11:03.810Z</startDate><endDate>2018-12-20T02:44:58.009Z</endDate><longVin>WBACR6108KLB11160</longVin><productId>SMART_ACCESS_Pro</productId><quantity>1</quantity></product><product><offerCode>SMARTACCESSACTIVATION</offerCode><startDate>2018-04-27T17:38:00.000Z</startDate><endDate>2019-04-27T23:59:59.000Z</endDate><longVin>WBACR6108KLB11160</longVin><productId>SMART_ACCESS_Activation</productId><quantity>1</quantity></product></listOfProducts></order>"
try:
    response = requests.put(
        # 'https://connected-int.bmw.com.cn/api/gateway/omc-products-management/760a0367-b6dd-45d5-99ae-a29ded41def1/products',
        'http://localhost:2053/api/gateway/omc-products-management/760a0367-b6dd-45d5-99ae-a29ded41def1/products',
        data=payload, headers=headers)
    print('status code: ', response.status_code)
    print('text: ', response.text)
    response.close()
except requests.exceptions.ConnectionError as e:
    print('error: ', str(e))
else:
    print('no error..')
finally:
    print('work complete..')
