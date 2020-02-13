# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class VstupParserItem(scrapy.Item):
    name_of_university = scrapy.Field()
    number = scrapy.Field()
    name_of_pupil = scrapy.Field()
    priority = scrapy.Field()
    av_mark = scrapy.Field()
    state = scrapy.Field()
    a = scrapy.Field()
    b = scrapy.Field()
    c = scrapy.Field()
    d = scrapy.Field()
    url = scrapy.Field()