import mysql.connector
try:    
    cnx = mysql.connector.connect(  user='root', 
                                password='123456',
                                host='127.0.0.1',
                                database='ha1')
    cursor = cnx.cursor()
    add_employee = ("INSERT INTO table1 "
                    "(bbb, ccc, ddd) "
                    "VALUES (%s ,%s, %s)")
    data_employee = ('1','2','3')
    cursor.execute(add_employee, data_employee)
    # Make sure data is committed to the database
    cnx.commit()

    cursor.close() 
except mysql.connector.Error as err:
    print(err)
else:       
    cnx.close()