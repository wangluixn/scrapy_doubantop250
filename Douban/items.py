# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    info = scrapy.Field()
    score = scrapy.Field()
    desc = scrapy.Field()
    link = scrapy.Field()
    category = scrapy.Field()
    story = scrapy.Field()
    review = scrapy.Field()
    
