# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class JdphoneItem(scrapy.Item):
    # define the fields for your item here like:
    brand = scrapy.Field()  # 手机品牌
    name = scrapy.Field()  # 手机名字
    image = scrapy.Field()  #手机图片
    uptime = scrapy.Field()   #上市时间
    price = scrapy.Field()  # 价格
    comrate = scrapy.Field()    #好评率



