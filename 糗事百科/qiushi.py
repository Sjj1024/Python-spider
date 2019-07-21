import requests
from lxml import etree


class QiuShi(object):
    def __init__(self):
        self.url = "https://www.qiushibaike.com/text/page/{}"
        self.header = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                          "(KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36"}

    def cret_url(self, url):
        #  构建url管理器，生成url列表
        url_list = [url.format(i) for i in range(14)]
        return url_list

    def parse_url(self, url):
        #  定义一个解析网址的方法
        response = requests.get(url, headers=self.header)
        return response.content.decode()

    def get_content(self, html_str):
        #  提取数据
        html = etree.HTML(html_str)
        # 使用xpath分析获取id为content-lest下的所有div标签，因为内容都存在这些标签里
        div_list = html.xpath("//div[@id='content-left']/div")
        # 定义一个列表，存储用户名和内容
        cont_list = []
        # 然后遍历这个列表，从中提取出用户名和内容
        for div in div_list:
            cont_dict = {}
            cont_dict["作者"] = div.xpath(".//h2/text()")[0].strip()
            cont_str = str([i.strip() for i in div.xpath(".//div[@class='content']/span/text()")]).replace("', '", "")
            cont_dict["内容"] = cont_str
            cont_list.append(cont_dict)
        return cont_list

    def save_data(self, cont_list):
        #  传入一个列表，然后遍历出来，
        for data in cont_list:
            print(data)

    def run(self):
        pass
        # 1.获取url地址，
        url = self.url
        # 2.构建rul管理器，列表
        url_list = self.cret_url(url)
        # 3、发送url请求，获取数据
        for urli in url_list:
            res = self.parse_url(urli)
            cont_list = self.get_content(res)
            # 4、筛选数据，保存数据
            self.save_data(cont_list)


if __name__ == '__main__':
    qiushi = QiuShi()
    qiushi.run()
