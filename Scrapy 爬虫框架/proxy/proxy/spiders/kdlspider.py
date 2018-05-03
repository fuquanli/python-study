# -*- coding: utf-8 -*-
import scrapy
from proxy.items import ProxyItem

class KdlspiderSpider(scrapy.Spider):
    name = 'kdlspider'
    allowed_domains = ['kuaidaili.com']
    start_urls = []

    for i in range(1, 6):
        start_urls.append('http://www.kuaidaili.com/free/inha/' + str(i) + '/')

    def parse(self, response):
        item = ProxyItem()

        #通过Xpath找到每条代理
        main = response.xpath('//table[@class="table table-bordered table-striped"]/tbody/tr')

        for li in main:
            ip = li.xpath('td/text()').extract()[0]
            port = li.xpath('td/text()').extract()[1]
            item['addr'] = ip+':'+port
            yield item
    
