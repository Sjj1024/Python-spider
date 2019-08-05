# -*- coding: utf-8 -*-
import scrapy


class DouyuSpider(scrapy.Spider):
    name = 'douyu'
    allowed_domains = ['douyu.com']
    start_urls = ['http://douyu.com/']

    def parse(self, response):
        pass
