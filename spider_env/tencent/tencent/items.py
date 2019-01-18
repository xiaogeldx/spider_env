# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
class TencentItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # pass
    job_name = scrapy.Field()   #声明一下，如果没有这几个字段会报错
    job_type = scrapy.Field()
    job_num = scrapy.Field()
    job_addr = scrapy.Field()
    job_time = scrapy.Field()
class DetailItem(scrapy.Item):
    detail_content = scrapy.Field()
