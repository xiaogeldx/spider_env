# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from tencent.items import TencentItem,DetailItem


class HrTencentSpider(CrawlSpider):    #CrawlSpider通过parse方法实现自动追踪链接的功能，不要在后面再自定义parse方法
    name = 'hr.tencent'
    allowed_domains = ['hr.tencent.com']
    start_urls = ['https://hr.tencent.com/position.php']
    rules = (   #包含一个或多个rule对象，写成列表或元组
        Rule(LinkExtractor(allow=r'start=\d+'), callback='parse_item', follow=True),    #follow=True意思是继续在这个页面解析新的内容
        #符合规则的url请求的回调函数为parse_items,并继续跟进，response传递下去继续匹配url
        Rule(LinkExtractor(allow=r'position_detail\.php\?id=\d+'), callback='parse_detail_item', follow=False),
    )   #callback='parse_detail_item'响应返回给parse_item

    def parse_item(self, response):
        """
        解析职位信息，解析之后继续解析
        :param response:
        :return:
        """
        for tr in response.xpath('//tr[@class="even"]|//tr[@class="odd"]'):
            item = TencentItem()
            item['job_name'] = tr.xpath('./td[1]/a/text()').extract_first()
            item['job_type'] = tr.xpath('./td[2]/text()').extract_first()
            item['job_num'] = tr.xpath('./td[3]/text()').extract_first()
            item['job_addr'] = tr.xpath('./td[4]/text()').extract_first()
            item['job_time'] = tr.xpath('./td[5]/text()').extract_first()
            yield item

    def parse_detail_item(self, response):
        """
        解析具体职位详情，解析之后不再解析
        :param response:
        :return:
        """
        item = DetailItem()
        item['detail_content'] = "".join(response.xpath('//ul[@class="squareli"]/li/text()').extract())
        yield item
        # i = {}
        # #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        # #i['name'] = response.xpath('//div[@id="name"]').extract()
        # #i['description'] = response.xpath('//div[@id="description"]').extract()
        # return i

