# -*- coding: utf-8 -*-
import scrapy
from copy import deepcopy

from Jdtushu.items import JdtushuItem


class JdSpider(scrapy.Spider):
    name = 'jd'
    allowed_domains = ['jd.com']
    start_urls = ['https://book.jd.com/booksort.html']

    def parse(self, response):
        # 解析大分类的名字
        dt_list = response.xpath('//*[@id="booksort"]/div[2]/dl/dt')
        # 遍历获取大分类和小分类内容
        for dt in dt_list:
            item = JdtushuItem()
            item['big_name'] = dt.xpath('./a/text()').extract_first()
            # 解析小分类名字和链接
            em_list = dt.xpath('./following-sibling::*[1]/em')
            for em in em_list:
                item['small_name'] = em.xpath('.//a/text()').extract_first()
                # print(item)
                small_link = 'https:' + em.xpath('.//a/@href').extract_first()
                # print(item)
                # print(small_link)
                yield scrapy.Request(url=small_link, callback=self.parse_book, meta={"book": deepcopy(item)})

    def parse_book(self, response):
        # 接收上一层传递过来的数据
        item = response.meta["book"]
        # 取出所有图书的链接
        book_link = response.xpath('//*[@id="plist"]/ul/li')
        for book in book_link:
            item['book_response_url'] = response.url
            # 因为图片有时候使用的是惰性加载，这个惰性加载怎么发现的？
            item['book_img_url'] = book.xpath('./div/div[1]/a/img/@src').extract_first()

            # if book_img_url == None:
            #     book_img_url = book.xpath('./div/div[1]/a/img/@src').extract_first()
            # item['book_img_url'] = 'https:' + book_img_url
            item['book_name'] = book.xpath('./div/div[3]/a/em/text()').extract_first().strip()
            # item['book_author'] = book.xpath('./div/div[4]/span[1]/span/a/text()').extract_first()
            item['book_store'] = book.xpath('./div/div[4]/span[2]/a/text()').extract_first()
            item['book_time'] = book.xpath('./div/div[4]/span[3]/text()').extract_first().strip()
            print(item)
