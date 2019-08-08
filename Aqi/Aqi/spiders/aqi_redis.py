# -*- coding: utf-8 -*-
import scrapy

from Aqi.items import AqiItem
from scrapy_redis.spiders import RedisSpider

class AqiSpider(RedisSpider):
    name = 'aqi_redis'
    allowed_domains = ['aqistudy.cn']
    base_urls = 'https://www.aqistudy.cn/historydata/'
    # start_urls = [base_urls]
    # 生成redis_key
    redis_key = "aqi"

    # 解析第一层数据，城市名字
    def parse(self, response):
        city_name_list = response.xpath('//ul/div[2]/li/a/text()').extract()[4:5]
        city_link_list = response.xpath('//ul/div[2]/li/a/@href').extract()[4:5]

        for city_name, city_link in zip(city_name_list, city_link_list):
            item = AqiItem()
            item['city_name'] = city_name
            item['city_link'] = city_link
            city_url = self.base_urls + city_link
            yield scrapy.Request(city_url, callback=self.parse_month, meta={"aqi":item})
            print(item)

    # 解析第二层数据，月份链接
    def parse_month(self, response):
        item = response.meta["aqi"]
        month_link_list = response.xpath("//table/tbody/tr/td/a/@href").extract()
        for month_link in month_link_list:
            month_url = self.base_urls + month_link
            yield scrapy.Request(month_url, callback=self.parse_day, meta={"aqi":item})
            print(item)

    # 解析第三层数据，真正数据
    def parse_day(self, response):
        item = response.meta["aqi"]
        tr_lsit = response.xpath("//tr")
        # 需要先删除表头信息
        tr_lsit.pop(0)
        # 遍历tr，取出tr中对应的每一个数据
        for tr in tr_lsit:
            # 日期
            item["data"] = tr.xpath("td[1]/text()").extract_first()
            # AQI
            item["aqi"] = tr.xpath("td[2]/text()").extract_first()
            # 质量等级
            item["level"] = tr.xpath("td[3]/text()").extract_first()
            # pm2.5
            item["pm25"] = tr.xpath("td[4]/text()").extract_first()
            # pm10
            item["pm10"] = tr.xpath("td[5]/text()").extract_first()
            # SO2
            item["so2"] = tr.xpath("td[6]/text()").extract_first()
            # CO
            item["co"] = tr.xpath("td[7]/text()").extract_first()
            # NO2
            item["no2"] = tr.xpath("td[8]/text()").extract_first()
            # O3
            item["o3"] = tr.xpath("td[9]/text()").extract_first()
            print(item)