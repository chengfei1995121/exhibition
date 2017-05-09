# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ZHItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title=scrapy.Field()
    stime=scrapy.Field()
    etime=scrapy.Field()
    city=scrapy.Field()
    province=scrapy.Field()
    address=scrapy.Field()
    zhuban=scrapy.Field()