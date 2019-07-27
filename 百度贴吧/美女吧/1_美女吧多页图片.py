import requests
from lxml import etree
import os


class TiebaSpider(object):
    def __init__(self):
        self.base_url = 'http://tieba.baidu.com/f'
        self.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko"}

    # 1. 发请求
    def send_request(self, url, tieba_parmas={}):
        response = requests.get(url, headers=self.headers, params=tieba_parmas)
        data = response.content
        return data

    # 2.保存数据
    def write_file(self, data, image_name):
        print(image_name)
        image_path = 'images/' + image_name
        with open(image_path, 'wb') as f:
            f.write(data)

    def parse_data(self, data, rule):
        # 1.转类型
        html_data = etree.HTML(data)

        # 2. xpath
        result_list = html_data.xpath(rule)

        return result_list

    # 3.调度方法
    def run(self):
        # 1.发送列表的页的请求
        tieba_params = {
            "kw": "美女",
            "pn": 0
        }
        # 2.发请求
        list_data = self.send_request(self.base_url, tieba_params)

        # 1.1 解析所有的详情页的链接 url
        # xpath插件 会优化代码
        # detail_rule = '//a[@class="j_th_tit"]/@href'  # 代码没数据 , xpath插件有

        detail_rule = '//div[@class="t_con cleafix"]/div/div/div/a/@href'
        detail_url_list = self.parse_data(list_data, detail_rule)
        # 2.发送详情页的请求
        for detail in detail_url_list:
            detail_url = 'http://tieba.baidu.com' + detail
            detail_data = self.send_request(detail_url)

            # 2.1 解析所有的图片的 url
            image_rule = '//img[@class="BDE_Image"]/@src'
            image_url_list = self.parse_data(detail_data, image_rule)

            # 3.发送图片的请求
            for img_url in image_url_list:
                img_data = self.send_request(img_url)

                # 图片的名字
                image_name = img_url[-15:]
                # 保存图片
                self.write_file(img_data, image_name)


if __name__ == '__main__':
    tool = TiebaSpider()
    tool.run()
