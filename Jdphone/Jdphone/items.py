# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class JdphoneItem(scrapy.Item):
    # define the fields for your item here like:
    goodid = scrapy.Field() # 商品id
    brand = scrapy.Field()  # 手机品牌
    name = scrapy.Field()  # 手机名字
    image = scrapy.Field()  # 手机图片
    year_time = scrapy.Field()   # 上市时间年份
    month_time = scrapy.Field()  # 上市时间月份
    price = scrapy.Field()  # 价格
    goodrate = scrapy.Field()  # 好评率
    link = scrapy.Field()   # 商品链接
    CommentCount = scrapy.Field()  # 商品总评价
    # 拓展信息
    weight = scrapy.Field() # 机身重量
    length = scrapy.Field() # 机身长度
    width = scrapy.Field()  # 机身宽度
    inch = scrapy.Field()   # 主屏幕尺寸



