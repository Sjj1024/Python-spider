# -*- coding: utf-8 -*-
import scrapy
from Baidu.items import GuokrItem, GuokrdetailItem


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
            item["link"] = i.xpath("./@href").extract_first()
            yield item
            yield scrapy.Request(url=item["link"], callback=self.detail_parse)

        # 翻页操作
        next_url = response.xpath('//a[text()="下一页"]/@href').extract_first()
        if next_url is not None:
            next_url = "https://www.guokr.com" + next_url
            print(22222222222222222222222)
            print(next_url)
            yield scrapy.Request(url=next_url, callback=self.parse)

    def detail_parse(self, response):
        item = GuokrdetailItem()
        div_list = response.xpath('')
