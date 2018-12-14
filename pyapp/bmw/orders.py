import requests
import csv
import json

f = open("C:\\Users\\qxu8502\\Desktop\\json.json", "r")
orders = json.load(f).get('ParentOrders')
f.close()

results = [['ParentOrderNo', 'UsId', 'OrderTime',
            'TotalPayAmount', 'TotalAmount', 'BusinessType']]
csvf = open('C:\\Users\\qxu8502\\Desktop\\result.csv',
            'w', encoding='gb2312', newline='')
writer = csv.writer(csvf)

for order in orders:
    pon = order['ParentOrderNo']
    resp = requests.get('https://omcfufmfece17q2.chinacloudsites.cn/order/BizOrder?parentOrderNo=' +
                        pon, headers={'ocp-apim-subscription-key': '2014_MyBMW837'})

    orderItems = json.loads(resp.text)
    resp.close()
    if orderItems[0]['BusinessType'] == '012':
        results.append([pon,  order['UsId'], order['OrderTime'],
                        order['TotalPayAmount'], order['TotalAmount'], 'CDStore'])


for result in results:
    writer.writerow(result)
csvf.close()
