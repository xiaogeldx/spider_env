# -*- coding: utf-8 -*-
import scrapy
import json


class TencentRecruitSpider(scrapy.Spider):
    name = 'tencent_recruit'
    start_urls = ['https://hr.tencent.com/position.php?keywords=python&lid=0&tid=0']      #初始地址

    def parse(self, response):
        #解析请求回来的响应
        #所有的行数据
        trs = response.xpath('//table[@class="tablelist"]/tr[@class="even"]|//table[@class="tablelist"]/tr[@class="odd"]')
        with open('job.json','a',encoding='utf-8') as f:
            for tr in trs:
                item = {
                    'job_name':tr.xpath('./td[1]/a/text()').extract_first(),
                    'job_type':tr.xpath('./td[2]/text()').extract_first(),
                    'job_num':tr.xpath('./td[3]/text()').extract_first(),
                    'job_addr':tr.xpath('./td[4]/text()').extract_first(),
                    'job_time':tr.xpath('./td[5]/text()').extract_first()
                }
                f.write(json.dumps(item,ensure_ascii=False))
                f.write('\n')
        next_url = response.xpath('//a[@id="next"]/@href').extract_first() #如果有多个值，用extract
        #返回一个request的请求
        if '50' in next_url:
            return
        return scrapy.Request('https://hr.tencent.com/%s' % next_url)
        #
        #
