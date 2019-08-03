# -*- coding: utf-8 -*-
import scrapy
from Baidu.items import GuokrItem

class GuokrSpider(scrapy.Spider):
    name = 'guokr'
    allowed_domains = ['guokr.com']
    start_urls = ['https://www.guokr.com/ask/highlight/']

    def parse(self, response):
        print(1111111111111)
        res_list = response.xpath("/html/body/div[3]/div[1]/ul[2]//div[2]/h2/a")
        for i in res_list:
            item = GuokrItem()
            # print(i.xpath("./text()").extract_first())
            item["name"] = i.xpath("./text()").extract_first()
            yield item
