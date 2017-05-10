#coding=utf-8
import scrapy
from zhanhui.items import ZHItem
from scrapy.http import Request

class zhanhui(scrapy.Spider):
    name = "zhanhui"
    allowed_domains = ["eshow365.com"]
    start_urls = [
    "http://www.eshow365.com/"
    ]
    def parse(self, response):
        for sel in response.xpath("//div[@class='lefttitle ']"):
            title=sel.xpath('a/text()').extract()
            href=sel.xpath('a/@href').extract()
            for i in href:
                yield Request(i,self.parse_next)

    def parse_next(self,response):
                    item=ZHItem()
                    n=response.xpath("//span[@id='txtClicks']/text()").extract()
                    if n[0]:
                        print "haha"
                        print n[0].strip()
                    title=response.xpath("//div[@class='zhmaincontent']/h1/text()").extract()
                    t=title[0]
                    t=t.replace(' ','').replace('\n','')
                    item['title']=t
                    for sel in response.xpath("//div[@class='zhxxcontent']"):
                        hanye=sel.xpath("p/a/text()").extract()[0]
                        item['address']=hanye.strip().replace(' ','')
                        time=sel.xpath("p/text()").extract()
                        item['etime']=time[0].replace(' ','')[-10:].replace("-","")
                        item['stime']=time[0].replace(' ','')[7:17].replace("-","")
                        city=time[5].strip().replace(' ','')
                        m=len(city)
                        m=m-1
                        item['province']=city[8:m].replace('|','')
                        item['city']=city[5:8].replace('|','')
                        s=time[6]
                        if s.find(u"主办") !=-1:
                            s=s.strip()
                            n=len(s)
                            n=n-5
                            item['zhuban']=s[-n:]
                        else:
                            item['zhuban']=' '
                        yield item