import requests
from lxml import etree
# from queue import Queue
# import threading
from multiprocessing import Process
from multiprocessing import JoinableQueue as Queue


class QiuShi(object):
    def __init__(self):
        self.url = "https://www.qiushibaike.com/text/page/{}"
        self.header = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                          "(KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36"}
        #  设置url队列
        self.url_queue = Queue()
        # 设置请求队列
        self.html_queue = Queue()
        # 设置相应队列
        self.content_queue = Queue()

    def cret_url(self):
        #  构建url管理器，生成url列表
        # url_list = [url.format(i) for i in range(14)]
        # return url_list
        for i in range(14):
            # 向url队列中添加url
            self.url_queue.put(self.url.format(i))
            print(i)

    def parse_url(self):
        while True:
            # 从url队列中取出url
            url = self.url_queue.get()
            #  定义一个解析网址的方法
            response = requests.get(url, headers=self.header)
            # print(response)
            # 将请求后返回的数据，放到html_queue中
            self.html_queue.put(response.content.decode())
            # 将url队列的计数减一
            self.url_queue.task_done()

    def get_content(self):
        while True:
            # 从html队列中获取数据
            html_str = self.html_queue.get()
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
                cont_str = str([i.strip() for i in div.xpath(".//div[@class='content']/span/text()")]).replace("', '",
                                                                                                               "")
                cont_dict["内容"] = cont_str
                cont_list.append(cont_dict)
            # 将请求到的数据放到内容队列中
            self.content_queue.put(cont_list)
            self.html_queue.task_done()

    def save_data(self):
        while True:
            # 从内容队列中获取，然后
            cont_list = self.content_queue.get()
            #  传入一个列表，然后遍历出来，
            for data in cont_list:
                print(data)
                pass
            self.content_queue.task_done()

    def run(self):
        # 创建一个列表，将线程保存到列表中，后期统一设置比较方便
        t_list = list()
        # 使用线程开始制作url列表
        t_url = Process(target=self.cret_url)
        t_list.append(t_url)
        print(t_list)
        # 使用线程开始请求url信息，设置将添加三个线程
        for x in range(3):
            t_parse = Process(target=self.parse_url)
            t_list.append(t_parse)
            print(t_list)
        # 使用线程开始获取内容
        t_get = Process(target=self.get_content)
        t_list.append(t_get)
        # 使用线程开始保存数据
        t_save = Process(target=self.save_data)
        t_list.append(t_save)
        print(t_list)
        # 遍历列表中的线程，依次设置成守护线程，并且开始执行线程
        for process in t_list:
            print("111111111111111111")
            process.daemon = True
            print("222222222222222222222")
            process.start()
            process.join()
            print("333333333333333333333")

        # 让主进程阻塞，等待队列计数为0
        for q in [self.url_queue, self.html_queue, self.content_queue]:
            q.join()


"""
每一个线程就相当于一个车间，每一个任务就相当于一个订单，队列就是保存订单的地方。
然后开启一个列表，让每个车间出来一个人到列表中（产生url，解析数据等车间），然后统一发号施令说开干，并设为守护线程。
最后让主线程阻塞，等待每个车间都完成任务再停止。
"""
if __name__ == '__main__':
    qiushi = QiuShi()
    qiushi.run()
