import scrapy
from tutorial.items import  LoLdyItem

class LoLdySpider(scrapy.Spider):
    name = "loldy"
    # start_urls = [
    #     'file://c/users/qxu8502/desktop/loldownload.html',
    # ]


    def start_requests(self): 
        source_table = [ 
                        # ('Dongzuodianying',99), 
                        # ('Kehuandianying',31), 
                        # ('Kongbudianying',83),
                        # ('Xijudianying',121),
                        # ('Aiqingdianying',54),
                        # ('Juqingdianying',276),
                        # ('Zhanzhengdianying',13),
                        # ('Anime',118),
                        ('Zuixinmeiju',102) 
                        ]
        for row in source_table:
            for i in range(row[1]): 
                yield scrapy.Request('https://www.loldytt.com/%s/chart/%d.html'%(row[0],i+1), self.parse_list) 
               

    def parse_list(self, response):
        links = response.xpath('//div[@class="box3_mid"]/ul/li/div/a/@href').extract()
        for link in links:
            yield scrapy.Request(link, self.parse) 

    def parse(self, response): 
        try:
            f1 = response.xpath('//div[@class="haibao"]/a/@title').extract()
            f2 = response.xpath('//div[@class="lanmu"]/ul/text()').extract()
            f3 = response.xpath('//div[@class="haibao"]/a/img/@src').extract()
            f4 = response.xpath('//div[@class="zhuyan"]/ul/li/text()').extract()
            f5 = response.xpath('//div[@class="neirong"]/p/text()').extract()
            f6 = response.xpath('//ul[@class="downurl"]/li/a/@href').extract() 
            f7 = response.xpath('//ul[@class="lm"]/h1/p/text()').extract() 
            yield LoLdyItem( 
                title = f1[0] if len(f1)>0 else 'null',
                tags = str(f2[0]).strip('\r\n') if len(f2)>1 else 'null'  ,
                image =f3[0] if len(f3)>0 else 'null' ,
                actors =f4[0] if len(f4)>0 else 'null' ,
                content =f5[0] if len(f5)>0 else 'null',
                download = str(f6) ,
                datetime  = f7[0] if len(f7)>0 else 'null'
            )
        except Exception as err:
            print(err) 