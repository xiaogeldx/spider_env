# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
from tencent.items import TencentItem

class TencentPipeline(object):

    def open_spider(self,spider):
        #在爬虫被打开的时候运行
        #打开文件句柄
        self.f = open('tencent_job.json','w')

    def process_item(self, item, spider):
        if isinstance(item,TencentItem):
            content = json.dumps(dict(item),ensure_ascii=False) + "\n"
            self.f.write(content)
        return item     #丢到下一个工序

    def close_spider(self,spider):
        #爬虫关闭时运行
        self.f.close()


class DatailPipeline(object):

    def open_spider(self,spider):
        self.file = open('detail.json','w')

    def process_item(self,item,spider):
        if isinstance(item,DetailItem):
            content = json.dumps(dict(item),ensure_ascii=False) + "\n"
            self.file.write(content)
        return item

    def close_spider(self,spider):
        self.file.close()
