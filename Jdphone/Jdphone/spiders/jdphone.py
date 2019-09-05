# -*- coding: utf-8 -*-
import json
import re

import scrapy
from copy import deepcopy

from Jdphone.items import JdphoneItem


class JdphoneSpider(scrapy.Spider):
    name = 'jdphone'
    allowed_domains = ['jd.com', 'search.jd.com', 'item.jd.com', 'c0.3.cn', "club.jd.com"]

    def start_requests(self):
        start_urls = []
        header = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36",
            "Referer": ""
        }
        for i in range(1, 100, 2):
            # 第n页链接生成
            url_n = f"https://search.jd.com/Search?keyword=%E6%89%8B%E6%9C%BA&enc=utf-8&page={i}"
            header['Referer'] = url_n
            start_urls.append(scrapy.Request(url_n, headers=header))
            # 隐藏的30个商品链接提取
            hide_url = f"https://search.jd.com/s_new.php?keyword=%E6%89%8B%E6%9C%BA&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&psort=3&cid2=653&cid3=655&page={i}&s=175&scrolling=y&log_id=1567233603.68952&tpl=3_M&show_items=53401701313,44126874550,100001893367,100003603159,100001485602,34487179057,7621213,50074585240,53372677476,31301071649,52588010239,100003258297,100004739684,43769837873,8348845,50645404316,39073847898,100000322417,31581424073,4938578,42847047935,7701235,100002544820,32896352259,100004363706,100002624532,47847150993,100006567258,52766070431,100006785480"
            # 将新生成的第n页url返回给开始的url列表
            header['Referer'] = url_n
            start_urls.append(scrapy.Request(url_n, headers=header))
            # 打印一下现在到第几页了
            print(f"正在下载第{(i+1)/2}页数据-------------------------------------")
        return start_urls

    # 解析商品详情页链接和生成第n也链接
    def parse(self, response):
        # 解析反回回来的html数据，提取商品详情页链接
        result = response.xpath('//*[@id="J_goodsList"]/ul/li/div/div[1]/a/@href').getall()
        print("++++++++++++++++++++++++++++++++++++++++" + str(len(result)))
        # 提取出来一个列表页中商品详情页链接
        for i in result:
            # 创建item对象保存数据信息
            item = JdphoneItem()
            # 判断链接是不是以https开头的，不是的话，就加上
            if not i.startswith("https:"):
                i = "https:" + i
            # 将商品链接保存到item中
            goodid = re.search(r"/(\d*).html", i)
            # 将商品id和手机详情字典对应
            item['goodid'] = goodid.group(1)
            item['link'] = i
            yield scrapy.Request(i, callback=self.parse_detail, meta={"item": deepcopy(item)})

    def parse_detail(self, response):
        # 解析详情页手机信息，主要是价格进行单独接口了
        # 获取之前传入的item
        item = response.meta["item"]
        # 提取出手机图片链接
        img_res = response.xpath('//*[@id="spec-img"]/@data-origin').get()
        if img_res and img_res.startswith("//"):
            img_res = "https:" + img_res
        item["image"] = img_res
        # 取出手机品牌
        brand = response.xpath('//*[@id="parameter-brand"]/li/a/text()').get()
        item["brand"] = brand
        # 提取出手机名称
        name_str = response.xpath('//dt[text()="产品名称"]/following-sibling::dd/text()').get()
        if not name_str:
            name_str = response.xpath('//dt[text()="型号"]/following-sibling::dd[2]/text()').get()
        item["name"] = name_str
        # 提取上市时间
        year_time = response.xpath('//dt[text()="上市年份"]/following-sibling::dd/text()').get()
        month_time = response.xpath('//dt[text()="上市月份"]/following-sibling::dd/text()').get()
        item["year_time"] = year_time
        item["month_time"] = month_time
        # 提取手机重量、长款，屏幕尺寸信息
        length = response.xpath('//dt[text()="机身长度（mm）"]/following-sibling::dd[1]/text()').get()
        item["length"] = length
        width = response.xpath('//dt[text()="机身宽度（mm）"]/following-sibling::dd[1]/text()').get()
        item["width"] = width
        weight = response.xpath('//dt[text()="机身重量（g）"]/following-sibling::dd[1]/text()').get()
        item["weight"] = weight
        inch = response.xpath('//dt[text()="主屏幕尺寸（英寸）"]/following-sibling::dd[1]/text()').get()
        item["inch"] = inch
        # 构造商品价格查询接口
        price_url = f"https://c0.3.cn/stock?skuId={item['goodid']}&area=2_2825_51931_0&cat=9987,653,655"
        yield scrapy.Request(price_url, callback=self.parse_price, meta={"item": deepcopy(item)})

    def parse_price(self, response):
        # 获取之前传入的item
        item = response.meta["item"]
        # 返回json数据
        json_str = response.body.decode("gbk")
        dict_str = json.loads(json_str)
        # 从数据中提取到价格
        goodprice = dict_str['stock']['jdPrice']['p']
        if goodprice:
            item["price"] = goodprice
        # 构造商品评价接口
        comment_url = f"https://club.jd.com/comment/productCommentSummaries.action?referenceIds={item['goodid']}"
        yield scrapy.Request(comment_url, callback=self.parse_comment, meta={"item": deepcopy(item)})

    def parse_comment(self, response):
        # 解析评论信息
        # 获取之前传入的item
        item = response.meta["item"]
        # 返回评价的json数据
        json_str = response.body.decode("gbk")
        dict_str = json.loads(json_str)
        # 从数据中提取好评率
        goodrate = dict_str['CommentsCount'][0]['GoodRateShow']
        CommentCount = dict_str['CommentsCount'][0]['CommentCount']
        if goodrate and CommentCount:
            item["CommentCount"] = CommentCount
            item["goodrate"] = str(goodrate) + "%"
        yield item
