# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import mysql.connector

class TutorialPipeline(object): 

    def open_spider(self, spider):
        try:
            self.cnx = mysql.connector.connect(  
                user='root', 
                password='123456',
                host='127.0.0.1',
                database='ha1') 

        except mysql.connector.Error as err:
            print(err)
            self.close_db()

    def close_spider(self, spider): 
        self.close_db()

    def process_item(self, item, spider): 
        cursor = self.cnx.cursor()
        add_employee = ("INSERT INTO news "
                        "(text,link) "
                        "VALUES (%s,%s)")
          
        try:
            data =  (str(item['text']), str(item['link']))
            cursor.execute(add_employee,data  )
            # Make sure data is committed to the database
            self.cnx.commit()
        except mysql.connector.Error as err:
            print(err)
            cursor.close()  
            self.close_db()
        return item
    
    def close_db(self):
        if self.cnx.is_connected():
            self.cnx.close()