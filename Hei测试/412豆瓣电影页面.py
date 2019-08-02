import requests
import json

"""
爬取豆瓣电影页面数据:
使用面向对象的方式爬取：

"""


class DouBan(object):
    # 定义初始化内容,url,header等
    def __init__(self):
        # 豆瓣电视剧
        url = "https://m.douban.com/tv/american"
        #
