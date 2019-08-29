# -*- coding: utf-8 -*-
import scrapy


class JdphoneSpider(scrapy.Spider):
    name = 'jdphone'
    allowed_domains = ['jd.com']
    start_urls = ['http://jd.com/']

    def parse(self, response):
        pass
