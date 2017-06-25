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
    guoji=scrapy.Field()
    guojia=scrapy.Field()
    sheng=scrapy.Field()
    shi=scrapy.Field()
    gnmx=scrapy.Field()
    gjmx=scrapy.Field()
    gnhx=scrapy.Field()
    gjhx=scrapy.Field()
    zh1=scrapy.Field()
    chengren=scrapy.Field()
    shangwu=scrapy.Field()
    yxgj=scrapy.Field()
