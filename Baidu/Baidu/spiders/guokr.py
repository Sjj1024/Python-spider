# -*- coding: utf-8 -*-
import scrapy


class GuokrSpider(scrapy.Spider):
    name = 'guokr'
    allowed_domains = ['guokr.com']
    start_urls = ['http://guokr.com/']

    def parse(self, response):
        pass
