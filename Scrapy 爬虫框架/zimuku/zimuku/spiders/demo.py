# -*- coding: utf-8 -*-
import scrapy

class DemoSpider(scrapy.Spider):
    name = 'demo'#爬虫的名字
    allowed_domains = ['zimuku.net']#规定爬虫爬取网页的域名
    start_urls = ['http://zimuku.net/']#开始爬取的链接


    def parse(self, response):
        name = response.xpath('//b/text()').extract()[1]
        items = {}
        items['第一个'] = name
        return items
                
