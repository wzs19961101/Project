# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class GamelolItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    hero_name = scrapy.Field()
    win_rate = scrapy.Field()
