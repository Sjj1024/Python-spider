import os
import threading
import requests
from bs4 import BeautifulSoup
import queue


class FaMei:
    def __init__(self, url):
        self.url = url
        self.soup = None
        self.header = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.79 Safari/537.36"
        }
        self.title = None
        self.path = None
        self.suc_num = 0
        self.q = queue.Queue()

    def get_soup(self, url):
        res = requests.get(url, headers=self.header)
        res_html = res.content.decode("utf-8")
        self.soup = BeautifulSoup(res_html, "lxml")
        return self.soup

    def get_title(self):
        self.title = self.soup.find_all("h1")[0].get_text()
        print(f"此篇写真标题是{self.title}----------->")
        self.path = os.path.join(os.getcwd(), self.title)
        if not os.path.exists(self.path):
            os.mkdir(self.path)
        print(self.path)

    def get_i(self):
        # 获取本页图片临时列表,并换成真正的图片链接
        # print([i.get("src") for i in self.soup.select("p img")])
        temp_i = [i.get("src").replace("../..", "https://www.24fa.top") for i in self.soup.select("p img")]
        print(f"此页成功获取到{len(temp_i)}张图片------->")
        self.q.put(temp_i)
        return temp_i

    def get_n(self):
        # 获取下一页按钮链接
        next_list = self.soup.select('a[title="下一页"]')
        if next_list:
            # print(self.soup.select('a[title="下一页"]')[0].get("href"))
            next_url = self.soup.select('a[title="下一页"]')[0].get("href")
            return next_url
        else:
            return None

    def get_imgs(self):
        print("获取图片列表")
        img_lists = []
        page = 0
        while True:
            page += 1
            print(f"正在获取第{page}页图片---------->")
            self.soup = self.get_soup(self.url)
            img_temp = self.get_i()
            img_lists += img_temp
            next_temp = self.get_n()
            if next_temp:
                # 如果有下一页链接，就将self.url换成下一页链接继续请求
                self.url = next_temp.replace("../..", "https://www.24fa.top")
            else:
                print("所有页面图片链接已经获取完毕--------->")
                rel_img_lists = [i.replace("../..", "https://www.24fa.top") for i in img_lists]
                return rel_img_lists

    def down_img(self, nameint, img_url):
        # 开始下载图片
        name = str(nameint + 1) + ".jpg"
        print(f"开始下载图片{name}-------->")
        res = requests.get(img_url, headers=self.header)
        if res.status_code == 404:
            print(f"图片{img_url}下载出错------->")
            return None
        img_name = os.path.join(self.path, name)
        with open(img_name, "wb") as f:
            f.write(res.content)
        self.suc_num += 1
        print(f"图片{name}下载完成--------->")

    def run(self):
        self.soup = self.get_soup(self.url)
        self.get_title()
        img_lists = self.get_imgs()
        # print(img_lists)
        # print(len(img_lists))
        thread_list = []
        for name, img_url in enumerate(img_lists):
            # self.down_img(name, img_url)
            thread_list.append(threading.Thread(target=self.down_img, args=(name, img_url)))
        for t in thread_list:
            t.start()
        print(f"成功下载了{self.suc_num}张图片+++++++++++>")


if __name__ == '__main__':
    url = "https://www.24fa.top/MeiNv/2020-02/71000.html"
    fa = FaMei(url)
    fa.run()