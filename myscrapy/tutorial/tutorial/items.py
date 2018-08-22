# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


# class HexunHomeItem(scrapy.Item):
#     # define the fields for your item here like:
#     # name = scrapy.Field()
#     text = scrapy.Field()
#     link = scrapy.Field()

# 电影天堂
class LoLdyItem(scrapy.Item):
    title = scrapy.Field()
    tags = scrapy.Field()
    image = scrapy.Field()
    actors = scrapy.Field()
    content = scrapy.Field()
    download = scrapy.Field()
    datetime = scrapy.Field()
