# import scrapy
# from tutorial.items import HexunHomeItem

# class HexunHomeSpider(scrapy.Spider):
#     name = "hexun"
#     start_urls = [
#         'http://www.hexun.com',
#     ]

#     def parse(self, response):
#         yield HexunHomeItem(
#             text = response.xpath('//div[@class="newsList"]/ul/li/a/text()').extract() ,
#             link = response.xpath('//div[@class="newsList"]/ul/li/a/@href').extract() 
#         )
        # yield {
        #     'text': c1.xpath()
        #     'author': quote.css('small.author::text').extract_first(),
        #     'tags': quote.css('div.tags a.tag::text').extract(),
        # }

        # next_page = response.css('li.next a::attr(href)').extract_first()
        # if next_page is not None:
        #     next_page = response.urljoin(next_page)
        #     yield scrapy.Request(next_page, callback=self.parse)
