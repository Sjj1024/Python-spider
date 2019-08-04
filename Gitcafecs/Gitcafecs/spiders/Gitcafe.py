# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from Gitcafecs.items import GitcafecsItem


class GitcafeSpider(CrawlSpider):
    name = 'Gitcafe'
    allowed_domains = ['gitcafe.net']
    start_urls = ['http://gitcafe.net/']

    rules = (
        Rule(LinkExtractor(allow=r'page/'), callback='parse_item', follow=True),
        Rule(LinkExtractor(allow=r'archives/\d+.html'), callback='parse_datail', follow=False)
    )

    def parse_item(self, response):
        print(111111111111111111111111111)
        print(response.url)

    def parse_datail(self, response):
        item = GitcafecsItem()
        print(22222222222222222222222222)
        print(response.url)
        item["title"] = response.xpath('//h1/a/text()').extract_first()
        item["author"] = response.xpath('//section/div[2]/div/header/div/span[2]/a/text()').extract_first()
        yield item
