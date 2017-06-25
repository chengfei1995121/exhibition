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
                yield Request(i,self.parse_next,dont_filter=True)

    def parse_next(self,response):
                    item=ZHItem()
                    s=''
                    """drecipt=response.xpath("//div[@class='zhgkcon']/div[@id='Span1']")
                    for i in drecipt.xpath("div/text()").extract():
                        s=s+i;
                    item['descript']=s"""
                    title=response.xpath("//div[@class='zhmaincontent']/h1/text()").extract()
                    t=title[0]
                    t=t.replace(' ','').replace('\n','')
                    item['title']=t
                    for sel in response.xpath("//div[@class='zhxxcontent']"):
                        hanye=sel.xpath("p/a/text()").extract()[0]
                        #item['address']=hanye.strip().replace(' ','')
                        time=sel.xpath("p/text()").extract()
                        item['etime']=time[0].replace(' ','')[-10:].replace("-","")
                        item['stime']=time[0].replace(' ','')[7:17].replace("-","")
                        city=time[5].strip().replace(' ','')
                        m=len(city)
                        m=m-1
                        item['city']=city[8:m].replace('|','')
                        #item['city']=city[5:8].replace('|','')
                        s=time[6]
                        if s.find(u"主办") !=-1:
                            s=s.strip()
                            n=len(s)
                            n=n-5
                            ss=s[-n:]
                            ss=ss.replace(' ','')
                            if ss.find(u"国际") !=-1:
                                item['guoji']='1'
                                item['guojia']='0'
                                item['sheng']='0'
                                item['shi']='0'
                            else:
                                if ss.find(u"政府"):
                                    if ss.find(u"国家") !=-1:
                                        item['guojia']='1'
                                        item['guoji']='0'
                                        item['sheng']='0'
                                        item['shi']='0'
                                    elif ss.find(u"省") !=-1:
                                        item['guojia']='0'
                                        item['guoji']='0'
                                        item['sheng']='1'
                                        item['shi']='0'
                                        
                                    elif ss.find(u"市") !=-1:
                                        item['guojia']='0'
                                        item['guoji']='0'
                                        item['sheng']='0'
                                        item['shi']='1'
                                        
                                else:
                                    item['guojia']='0'
                                    item['guoji']='0'
                                    item['sheng']='0'
                                    item['shi']='0'
                            if ss.find(u"协会")!=-1:
                                if ss.find(u"行业"):
                                    if ss.find(u"国际")!=-1:
                                        item['gjhx']='1'
                                        item['gnhx']='0'
                                        item['gjmx']='0'
                                        item['gnmx']='0'
                                    else:
                                        item['gjhx']='0'
                                        item['gnhx']='1'
                                        item['gjmx']='0'
                                        item['gnmx']='0'
                                else:
                                    if ss.find(u"国际")!=-1:
                                        item['gjhx']='0'
                                        item['gnhx']='0'
                                        item['gjmx']='1'
                                        item['gnmx']='0'
                                    else:
                                        item['gjhx']='0'
                                        item['gnhx']='0'
                                        item['gjmx']='0'
                                        item['gnmx']='0'
                            else:
                                item['gjhx']='0'
                                item['gnhx']='0'
                                item['gjmx']='0'
                                item['gnmx']='0'
                        else:
                            item['gjhx']='0'
                            item['gnhx']='0'
                            item['gjmx']='0'
                            item['gnmx']='0'
                            item['guojia']='0'
                            item['guoji']='0'
                            item['sheng']='0'
                            item['shi']='0'
                        item['zh1']='1'
                        item['chengren']='1'
                        item['shangwu']='1'
                        if item['title'].find(u"国际"):
                            item['yxgj']='1'
                        else:
                            item['yxgj']='0'
                    yield item