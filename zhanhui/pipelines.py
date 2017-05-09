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
    	n=conn.execute("select * from zh where title=%s",item['title'])
    	if n:
    		print "yes"
    	else:
    		print n
        	sql = "insert into zh(title,stime,etime,city,province,address,zhuban) values(%s,%s,%s,%s,%s,%s,%s)"
        	params = (item['title'],item['stime'],item['etime'],item['province'],item['city'],item['address'],item['zhuban'])
        	conn.execute(sql,params)
    #异常处理
    def _handle_error(self, failue, item, spider):
    	log.err(failure)