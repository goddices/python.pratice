import scrapy
from tutorial.items import  HuangLingItem
import csv

class HuangLingSpider(scrapy.Spider):
    name = "huangling"
    # start_urls = [
    #     'https://www.loldytt.com/Dongzuodianying/QSR/',
    # ]


    def start_requests(self): 
        try:
            datacache = []
            file = open('C:/Users/qxu8502/workspace/myspace/python/python-xuexi/myscrapy/tutorial/files/test.csv','r',encoding='utf8',errors='ignore')
            rdr = csv.reader(file) 
            for row in rdr:
                datacache.append([row[0],row[1],row[2],row[3]])
                
            for row in datacache:
                try:
                    name = row[1]
                    name = name[:name.index('/')]
                    yield scrapy.Request('http://drugs.dxy.cn/search/drug.htm?keyword=%s'%(name), self.parse_list) 
                except Exception as err:
                    print(err)
                    continue
        except Exception as err:
            print(err)

    def parse_list(self, response):
        try:
            cmname = response.xpath('//div[@class="m49 detail detail1"]/dl/dd').extract()[0].split('<br>')[0].replace('<dd>','').strip().replace('通用名称：','')
            enname = response.xpath('//div[@class="m49 detail detail1"]/dl/dd').extract()[0].split('<br>')[1].strip().replace('英文名称：','')
            prname = response.xpath('//div[@class="m49 detail detail1"]/dl/dd').extract()[0].split('<br>')[2].strip().replace('商品名称：','')
            # index1 = response.xpath('//div[@class="m49 detail detail1"]/dl/dt/span/text()').extract().index('批准文号:')
            # index1 = response.xpath('//div[@class="m49 detail detail1"]/dl/dt/span/text()').extract().index('批准文号:')
            # pzwh = response.xpath('//div[@class="m49 detail detail1"]/dl/dd').extract()[index1+1].replace('<dd>','').replace('</dd>','').replace('&amp;','&').strip()
            pzwh = response.xpath('//div[@class="m49 detail detail1"]/dl/dt/span[@id="39"]/../following-sibling::dd[1]/text() | //div[@class="m49 detail detail1"]/dl/dt/span[@id="39"]/../following-sibling::dd[1]/p/text()').extract()[0].strip()
            # index2 = response.xpath('//div[@class="m49 detail detail1"]/dl/dt/span/text()').extract().index('生产企业:')
            # producer = response.xpath('//div[@class="m49 detail detail1"]/dl/dd').extract()[index2+1].replace('<dd>','').replace('</dd>','').replace('&amp;','&').strip()
            producer =  response.xpath('//div[@class="m49 detail detail1"]/dl/dt/span[@id="1"]/../following-sibling::dd[1]/text() | //div[@class="m49 detail detail1"]/dl/dt/span[@id="39"]/../following-sibling::dd[1]/p/text()').extract()[0].strip()
            yield HuangLingItem ( 
                cmname = cmname,
                enname = enname ,
                prname = prname ,
                pzwh = pzwh,
                producer = producer 
            )
        except Exception as err:
            alist = response.xpath('//div[@class="m49 result"]/ul/li//div/h3/a/@href').extract()
            yield scrapy.Request('http:'+alist[0], self.parse_list) 
            # for link in alist:
            #     yield scrapy.Request('http:'+link, self.parse_list) 

    # def parse(self, response): 
    #     try:
    #         f1 = response.xpath('//div[@class="haibao"]/a/@title').extract()
    #         f2 = response.xpath('//div[@class="lanmu"]/ul/text()').extract() 
    #         f3 = response.xpath('//div[@class="haibao"]/a/img/@src').extract()
    #         f4 = response.xpath('//div[@class="zhuyan"]/ul/li/text()').extract()
    #         f5 = response.xpath('//div[@class="neirong"]/p/text()').extract()
    #         f6 = response.xpath('//ul[@class="downurl"]/li/a/@href | //ul[@class="downurl"]/li/a/@title | //div[@id="bt"]/ul/li/a/@href | //div[@id="bt"]/ul/li/a/@title').extract() 
    #         f7 = response.xpath('//div[@class="lm"]/h1/p/text()').extract() 
    #         yield HuangLingItem ( 
    #             title = f1[0] if len(f1)>0 else 'null',
    #             tags = str(f2[0]).strip('\r\n') if len(f2)>1 else 'null'  ,
    #             image =f3[0] if len(f3)>0 else 'null' ,
    #             actors =f4[0] if len(f4)>0 else 'null' ,
    #             content = str(f5),
    #             download = str(f6) ,
    #             datetime  = f7[0] if len(f7)>0 else 'null'
    #         )
    #     except Exception as err:
    #         print(err) 