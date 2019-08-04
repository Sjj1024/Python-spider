# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class Guokr3Spider(CrawlSpider):
    name = 'guokr3'
    allowed_domains = ['guokr.com']
    start_urls = ['https://www.guokr.com/ask/highlight/?page=1']

    rules = (
        Rule(LinkExtractor(allow=r'page='), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        print(1111111111111111)
        print(response.url)
