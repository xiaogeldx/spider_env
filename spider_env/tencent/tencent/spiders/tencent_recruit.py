# -*- coding: utf-8 -*-
import scrapy
import json
from tencent.items import TencentItem
class TencentRecruitSpider(scrapy.Spider):
    name = 'tencent_recruit'
    start_urls = ['https://hr.tencent.com/position.php?keywords=python&lid=0&tid=0']
    def parse(self, response):
        trs = response.xpath('//table[@class="tablelist"]/tr[@class="even"]|//table[@class="tablelist"]/tr[@class="odd"]')
        if trs:     #如果没有表示到了最后一页
            for tr in trs:
                item = TencentItem()
                item['job_name'] = tr.xpath('./td[1]/a/text()').extract_first()
                item['job_type'] = tr.xpath('./td[2]/text()').extract_first()
                item['job_num'] = tr.xpath('./td[3]/text()').extract_first()
                item['job_addr'] = tr.xpath('./td[4]/text()').extract_first()
                item['job_time'] = tr.xpath('./td[5]/text()').extract_first()
                yield item  #发回管道并且不终止
            #提取下一页
            next_url = response.xpath('//a[@id="next"]/@href').extract_first()  # 如果有多个值，用extract
            yield scrapy.Request('https://hr.tencent.com/%s' % next_url)
        else:
            return

