from gevent import monkey

monkey.patch_all()
from gevent.pool import Pool
import requests
import time
from lxml import etree
from queue import Queue


class QiuShi(object):
    def __init__(self):
        self.url = "https://www.qiushibaike.com/text/page/{}"
        self.header = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                          "(KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36"}
        self.queue = Queue()
        self.pool = Pool(5)
        self.is_running = True
        self.total_request_num = 0
        self.total_response_num = 0

    def cret_url(self, url):
        #  构建url管理器，生成url列表
        url_list = [url.format(i) for i in range(14)]
        # 使用线程池导入url链接
        for i in url_list:
            self.queue.put(i)
            self.total_request_num += 1
            # print(i)

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

    # 进行一次url地址的请求和保存
    def execute_request_content_save(self):
        urli = self.queue.get()
        res = self.parse_url(urli)
        cont_list = self.get_content(res)
        # 4、筛选数据，保存数据
        self.save_data(cont_list)
        self.total_response_num += 1

    def _callback(self, temp):
        if self.is_running:
            self.pool.apply_async(self.execute_request_content_save, callback=self._callback)

    def run(self):
        # 1.获取url地址，
        url = self.url
        # 2.构建rul管理器，列表
        self.cret_url(url)
        # 3、发送url请求，获取数据
        for i in range(5):
            self.pool.apply_async(self.execute_request_content_save, callback=self._callback)
        while True:
            time.sleep(0.0001)
            if self.total_response_num >= self.total_request_num:
                self.is_running = False
                break


if __name__ == '__main__':
    t1 = time.time()
    qiushi = QiuShi()
    qiushi.run()
    print("total cost:", time.time() - t1)
