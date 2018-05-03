# -*- coding: utf-8 -*-
import scrapy
from proxy.items import ProxyItem

class DxdlspiderSpider(scrapy.Spider):
    name = 'dxdlspider'
    allowed_domains = ['xicidaili.com']
    start_urls = ['http://api.xicidaili.com/free2016.txt']

    def parse(self, response):
        item = ProxyItem()
        #因为调用的是网站的api，get返回的就是一个文本
        item['addr'] = response.text
        return item
