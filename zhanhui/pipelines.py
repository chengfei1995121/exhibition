# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
from scrapy import signals
import json
import codecs
from twisted.enterprise import adbapi
from datetime import datetime
from hashlib import md5
import MySQLdb
import MySQLdb.cursors
import chardet

class MySQLzhanhuiPipeline(object):
    def __init__(self, dbpool):
        self.dbpool = dbpool
    
    @classmethod
    def from_settings(cls, settings):
        dbargs = dict(
            host=settings['MYSQL_HOST'],
            db=settings['MYSQL_DBNAME'],
            user=settings['MYSQL_USER'],
            passwd=settings['MYSQL_PASSWD'],
            charset='utf8',
            cursorclass = MySQLdb.cursors.DictCursor,
            use_unicode= True,
        )
        dbpool = adbapi.ConnectionPool('MySQLdb', **dbargs)
        return cls(dbpool)

    #pipeline默认调用
    def process_item(self, item, spider):
        d = self.dbpool.runInteraction(self._do_upinsert, item)
        d.addErrback(self._handle_error, item, spider)
        d.addBoth(lambda _: item)
        return d

    #将每行更新或写入数据库中
    def _do_upinsert(self, conn, item):
            """s=item['title']
            sql="select * from infotable where 事件名称=%s" % (s)
            print sql.encode("GB18030");
            n=conn.execute(sql)
            print n
            print "hahaha"
            if n:
                 print "yes"
            else:"""
            sql = "insert into infotable(事件名称,开始日期,结束日期,举办城市,是否国际性组织,是否国家政府,是否省政府,是否地方政府,是否国内民间协会,是否国际民间协会,是否国内行业协会,是否国际行业协会,主要影响成人,是否是展会,是否影响商务人群,最大影响全球,事件历史悠久程度,事件一年内频次) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            params = (item['title'],item['stime'],item['etime'],item['city'],item['guoji'],item['guojia'],item['sheng'],item['shi'],item['gnmx'],item['gjmx'],item['gnhx'],item['gjhx'],item['chengren'],item['zh1'],item['shangwu'],item['yxgj'],item['lishi'],item['pl'])
            conn.execute(sql,params)
    #异常处理
    def _handle_error(self, failue, item, spider):
        log.err(failure)