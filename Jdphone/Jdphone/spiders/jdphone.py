# -*- coding: utf-8 -*-
import scrapy


class JdphoneSpider(scrapy.Spider):
    name = 'jdphone'
    allowed_domains = ['jd.com', 'search.jd.com']
    start_urls = ['https://search.jd.com/Search?keyword=%E6%89%8B%E6%9C%BA&enc=utf-8&page=1']

    def parse(self, response):
        result = response.xpath('//*[@id="J_goodsList"]/ul/li/div/div[4]/a/@href').getall()
        for i in result:
            print(i)