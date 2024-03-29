# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapyNewItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    title_url = scrapy.Field()
    headlineinfo = scrapy.Field()
    message_title = scrapy.Field()
    message_url = scrapy.Field()
