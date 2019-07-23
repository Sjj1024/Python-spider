# 获取达盖尔单单页文章链接
import requests
import re
import os

class Dagaier(object):
    def __init__(self):
        self.url = "https://1024.fil6.tk/thread0806.php?fid=16"
        self.header = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36",
        }

    # @retry(stop_max_attempt_number=3)
    def request_url(self):
        res = requests.get(self.url, headers=self.header)
        # print(res.content)
        res_html = res.content.decode("gbk")
        return res_html

    def parse_url(self, res_html):
        """<h3><a href="htm_data/1907/16/3582293.html" target="_blank" id=""><font color=green>[原创]女教师的新婚夜在婚床上放飞自我[25P]</font></a></h3>  """
        url_list = re.findall(r'<h3><a href="(.*?)".*?<font color=green>(.*?)</font>', res_html)
        # print(url_list)
        return url_list

    def parse_newurl(self, url_list):
        print(url_list)
        res_html_list = []
        for i in url_list:
            url, title = i
            new_url = "https://1024.fil6.tk/" + url
            # print(new_url)
            res = requests.get(new_url, headers=self.header)
            res_html = res.content.decode("gbk")
            res_html_list.append(res_html)
        return res_html_list

    def parse_jpg(self, html_list):
        for i in html_list:
            res_jpg = re.findall(r'', i)


    def run(self):
        # 生成url
        # 发送请求获取html
        res_html = self.request_url()
        # 解析文章链接 url
        url_list = self.parse_url(res_html)
        # 保存url
        # 请求文章utl
        html_list = self.parse_newurl(url_list)
        # 解析图片链接
        self.parse_jpg(html_list)

if __name__ == '__main__':
    Dagaier().run()
