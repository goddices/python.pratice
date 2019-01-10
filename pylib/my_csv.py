import csv
data =  [['aa','bb','cc',['123','456']],['ddd','eee','gggcc',['(*":1$**#!','45dfd6']]] 
file = open('123.csv','w',encoding='gb2312',newline='')
writer = csv.writer(file)
for row in data:
        writer.writerow(row) 
file.close() 