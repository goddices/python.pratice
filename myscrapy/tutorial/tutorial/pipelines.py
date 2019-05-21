# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

#import mysql.connector 
import csv
import datetime

# class TutorialPipeline(object): 

#     def open_spider(self, spider):
#         try:
#             self.cnx = mysql.connector.connect(  
#                 user='root', 
#                 password='123456',
#                 host='127.0.0.1',
#                 database='ha1') 

#         except mysql.connector.Error as err:
#             print(err)
#             self.close_db()

#     def close_spider(self, spider): 
#         self.close_db()

#     def process_item(self, item, spider): 
#         cursor = self.cnx.cursor()
#         add_employee = ("INSERT INTO news "
#                         "(text,link) "
#                         "VALUES (%s,%s)")
          
#         try: 
#             lentxt,lenlnk = len(item['text']),len(item['link'])
#             iternum = lenlnk if lentxt>=lenlnk else lentxt
#             for i in range(iternum):
#                 cursor.execute(add_employee,(item['text'][i],item['link'][i]))
#             # Make sure data is committed to the database
#             self.cnx.commit()
#         except mysql.connector.Error as err:
#             print(err)
#             cursor.close()  
#             self.close_db()
#         return item
    
#     def close_db(self):
#         if self.cnx.is_connected():
#             self.cnx.close()




class LoLdyPipeline(object): 

    def open_spider(self, spider):
        self.datacache = []
        # try:
        #     self.cnx = mysql.connector.connect(  
        #         user='root', 
        #         password='123456',
        #         host='127.0.0.1',
        #         database='dianying') 
        #     self.cursor = self.cnx.cursor()

        # except mysql.connector.Error as err:
        #     print(err)
        #     self.close_db()

    def close_spider(self, spider): 
        # try:
        #     for data in self.datacache:
        #         try:
        #             self.cursor.execute(
        #                 "INSERT INTO sp_film_info (title,tags,image,actors,content,download) VALUES (%s,%s,%s,%s,%s,%s)" ,data)
        #         except mysql.connector.Error as err:
        #             print(err) 
        #             continue
        #     # Make sure data is committed to the database
        #     self.cnx.commit()
        # except mysql.connector.Error as err:
        #     print(err) 
        #     self.close_db()
        # self.close_db()
        try:
            file = open('c:/users/qxu8502/desktop/output/Zuixinmeiju'+ datetime.datetime.now().strftime('%Y%m%d%H%M%S')+'.csv','w+',encoding='gb2312',errors='ignore')
            writer = csv.writer(file)
            for row in self.datacache:
                writer.writerow(row) 
            file.close()
        except Exception as err:
            print(err)

    def process_item(self, item, spider):   
        self.datacache.append(( 
            item['title'],
            item['tags'],
            item['image'],
            item['actors'],
            item['content'],
            item['download'],
            item['datetime']
        )) 
        return item
    
    # def close_db(self):  
        # if self.cnx.is_connected(): 
        #     self.cursor.close()
        #     self.cnx.close()


class BtbtdyPipeline(object): 

    def open_spider(self, spider):
        self.datacache = []
        # try:
        #     self.cnx = mysql.connector.connect(  
        #         user='root', 
        #         password='123456',
        #         host='127.0.0.1',
        #         database='dianying') 
        #     self.cursor = self.cnx.cursor()

        # except mysql.connector.Error as err:
        #     print(err)
        #     self.close_db()

    def close_spider(self, spider): 
        # try:
        #     for data in self.datacache:
        #         try:
        #             self.cursor.execute(
        #                 "INSERT INTO sp_film_info (title,tags,image,actors,content,download) VALUES (%s,%s,%s,%s,%s,%s)" ,data)
        #         except mysql.connector.Error as err:
        #             print(err) 
        #             continue
        #     # Make sure data is committed to the database
        #     self.cnx.commit()
        # except mysql.connector.Error as err:
        #     print(err) 
        #     self.close_db()
        # self.close_db()
        try:
            file = open('c:/users/qxu8502/desktop/output/btbtdy'+ datetime.datetime.now().strftime('%Y%m%d%H%M%S')+'.csv','w+',encoding='gb2312',errors='ignore')
            writer = csv.writer(file)
            for row in self.datacache:
                writer.writerow(row) 
            file.close()
        except Exception as err:
            print(err)

    def process_item(self, item, spider):   
        self.datacache.append(( 
            item['dyid'],
            item['title'],
            item['image'],
            item['year'],  
            item['tags'],
            item['content'] 
        )) 
        return item
    
class HuangLingPipeline(object): 
    def open_spider(self, spider):
        self.datacache = []

    def close_spider(self, spider): 
        try:
            file = open('C:/Users/zhufeng/Desktop/save'+ datetime.datetime.now().strftime('%Y%m%d%H%M%S')+'.csv','w+',encoding='gb2312',errors='ignore')
            writer = csv.writer(file)
            for row in self.datacache:
                writer.writerow(row) 
            file.close()
        except Exception as err:
            print(err)
         

    def process_item(self, item, spider):   
        self.datacache.append(  
            (item['cmname'],
            item['prname'],
            item['enname'],
            item['pzwh'],
            item['producer'])
        ) 
        return item