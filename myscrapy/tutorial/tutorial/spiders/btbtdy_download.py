# import scrapy
# import mysql.connector
# from tutorial.items import  BtbtdyItem

# class LoLdySpider(scrapy.Spider):
#     PAGE =   370
#     name = "btbtdy_download"
#     # start_urls = [
#     #     #'http://www.btbtdy.net/screen/0-----time-1.html',
#     #     'http://www.btbtdy.net/btdy/dy13401.html',
#     # ]
#     def loadIdArray(self):
#         try:    
#             cnx = mysql.connector.connect(user='root', 
#                                       password='123456',
#                                       host='127.0.0.1',
#                                       database='dianying')
#             cursor = cnx.cursor()
#             cursor.execute("select dyid from sp_movie_btbtdy")
#             array = cursor.fetchall()
#             return array
#         except Exception as err:
#             pass
#         else:
#             cnx.close()

#     def start_requests(self):  
#         array = self.loadIdArray()

#         for pn in range(self.PAGE): 
#                 yield scrapy.Request('http://www.btbtdy.net/down/%s-0-0.html.html'%(pn+1), self.parse) 
         

   

#     def parse(self, response): 
#         try: 
#             f0 = response.xpath('//div[@class="download"]/a[last()]/@href').extract() #dyid
#             f1 = response.xpath('//div[@class="vod_img lf"]/img/@alt').extract() #title
#             f2 = response.xpath('//div[@class="vod_img lf"]/img/@src').extract() #image
#             f3 = response.xpath('//span[@class="year"]/text()').extract()         #year 
#             f4 = response.xpath('//dl/dd/text() | //dl/dd/a/text()').extract()  #标签 tags dd 
#             f5 = response.xpath('//div[@class="c05"]/span/text() | //div[@class="c05"]/text() | //div[@class="c05"]/p/text()').extract()   #剧情介绍
#             #f6 = response.xpath('//ul[@class="p_list_02"]/li/a/@href | //ul[@class="downurl"]/li/a/@title | //div[@id="bt"]/ul/li/a/@href | //div[@id="bt"]/ul/li/a/@title').extract() 
            
#             yield BtbtdyItem( 
#                 dyid =  str(f0[0]).replace('/btdy/dy','').replace('.html','') ,
#                 title = f1[0] if len(f1)>0 else 'null',
#                 image =f2[0] if len(f2)>0 else 'null' ,
#                 year = f3[0].replace(' (','').replace(')',''),
#                 tags = str(f4),  
#                 content = str(f5),
#                 # download = str(f6)  
#             )
#         except Exception as err:
#             print(err) 