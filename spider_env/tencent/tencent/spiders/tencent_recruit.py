# -*- coding: utf-8 -*-
import scrapy


class TencentRecruitSpider(scrapy.Spider):
    name = 'tencent_recruit'
    allowed_domains = ['https://hr.tencent.com/']
    start_urls = ['https://hr.tencent.com//']

    def parse(self, response):
        pass
