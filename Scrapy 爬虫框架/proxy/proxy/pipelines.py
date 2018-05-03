# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class ProxyPipeline(object):
    def process_item(self, item, spider):
        if spider.name == 'dxdlspider':
            content = item['addr'].split('\r\n')
            for line in content:
                print(line+'\n')
                open('/Users/Lifuquan.ET/Desktop/result/dx_proxy.txt', 'a').write(line+'\n')
        elif spider.name == 'kdlspider':
            print(item['addr']+'\n')
            with open('d:/fuquan/result/kd_proxy.txt', 'a+') as f:
                f.write(item['addr']+'\n')
            #open('d:/fuquan/result/kd_proxy.txt', 'a').write(item['addr']+'\n')
        return item
