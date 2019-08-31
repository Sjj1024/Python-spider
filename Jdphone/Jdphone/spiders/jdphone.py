# -*- coding: utf-8 -*-
import scrapy
from Jdphone.items import JdphoneItem

class JdphoneSpider(scrapy.Spider):
    name = 'jdphone'
    allowed_domains = ['jd.com', 'search.jd.com']
    # 单页开始url
    start_urls = ['https://search.jd.com/Search?keyword=%E6%89%8B%E6%9C%BA&enc=utf-8&page=1']

    def parse(self, response):
        # 解析反回回来的html数据，提取商品详情页链接
        result = response.xpath('//*[@id="J_goodsList"]/ul/li/div/div[4]/a/@href').getall()
        print(len(result))
        # 打印提取出来的商品详情页链接
        for i in result:
            if not i.startswith("https:"):
                i = "https:" + i
            print(i)
            yield scrapy.Request(i, callback=self.parse_detail)
        # 隐藏的30个商品链接提取
        hide_url = "https://search.jd.com/s_new.php?keyword=%E6%89%8B%E6%9C%BA&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&psort=3&cid2=653&cid3=655&page=8&s=175&scrolling=y&log_id=1567233603.68952&tpl=3_M&show_items=53401701313,44126874550,100001893367,100003603159,100001485602,34487179057,7621213,50074585240,53372677476,31301071649,52588010239,100003258297,100004739684,43769837873,8348845,50645404316,39073847898,100000322417,31581424073,4938578,42847047935,7701235,100002544820,32896352259,100004363706,100002624532,47847150993,100006567258,52766070431,100006785480"

        # 第n页页面链接生成，然后还是使用parse方法解析


    def parse_detail(self, response):
        # 解析详情页手机信息
        item = JdphoneItem()


    def parse_comment(self):
        # 解析评论信息
        pass