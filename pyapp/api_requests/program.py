import csv
import requests


def request_casa(vin):
    headers = {
        'Authorization': 'Basic cXFjc2NuMTphNjFhZGVycw==', 
        'Cache-Control': 'no-cache'
    }
    response = requests.get(
        ('https://casa-cn-i-api.bmw.com/casa/store/portfolio?vin=%s&bu=BMW_CN') % (vin),   headers=headers)
        # test enviornment

    xfile = open(('C:/Users/qxu8502/Desktop/xml/1/%s.xml') % (vin), 'w')
    try:
        # tmp1 = xmltxt
        tmp1 = str(response.content)
        resptxt = tmp1[2:len(tmp1)-1]
        xfile.write(resptxt)

    except Exception as err:
        print(err)
    else:
        xfile.close()


# file = open('C:/Users/qxu8502/Desktop/2018.8月订单.csv',
            # 'r', encoding='gb2312', newline='')

a = ['LBVKY710XJSP01320',
     'WBY7Z2100J7B29638',
     'LBVHY1101HMD98761',
     'WBAJV6103JBC93938']

# rn = 0
# reader = csv.reader(file)
for row in a:
    # if rn!=0 :
    # vin = row[2]  # VIN
    vin = row
    request_casa(vin)
    # rn = rn + 1
# file.close()
