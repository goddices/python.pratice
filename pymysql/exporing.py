import mysql.connector
import csv
try:    
    cnx = mysql.connector.connect(  user='root', 
                                password='123456',
                                host='127.0.0.1',
                                database='dianying')
    cursor = cnx.cursor()   #C:\Users\qxu8502\mypython\python.pratice\myscrapy\tutorial\output\Zuixinmeiju20180822163455.csv
    file = open('c:/users/qxu8502/desktop/output/Zuixinmeiju20180828142531.csv', 
        'r',encoding='gb2312',newline='\r\n')
    reader = csv.reader(file) 

    for row in reader:
        if row[0] == '名侦探柯南': 
            continue
        cursor.execute("INSERT INTO sp_movie_lol (title,category,image,actors,content,download) VALUES (%s,%s,%s,%s,%s,%s)" ,
            (row[0],row[1],row[2],row[3],row[4],row[5]) 
        ) 

    file.close() 
    cnx.commit() 
    cursor.close() 
except Exception as err:
    print(err)
else:       
    cnx.close()