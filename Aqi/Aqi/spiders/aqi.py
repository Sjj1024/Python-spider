# -*- coding: utf-8 -*-
import scrapy

from Aqi.Aqi.items import AqiItem


class AqiSpider(scrapy.Spider):
    name = 'aqi'
    allowed_domains = ['aqistudy.cn']
    base_urls = 'https://www.aqistudy.cn/historydata/'
    start_urls = [base_urls]

    def parse(self, response):
        city_name_list = response.xpath('//ul/div[2]/li/a/text()').extract()[4:5]
        city_link_list = response.xpath('//ul/div[2]/li/a/@href').extract()[4:5]

        for city, link in zip(city_name_list, city_link_list):
            item = AqiItem()