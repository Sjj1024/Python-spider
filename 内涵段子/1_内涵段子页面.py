# https://www.neihan-8.com/article/list_5_1.html
import requests
import re


class Duanzi(object):
    def __init__(self):
        self.url1 = "https://www.neihan-8.com/article/list_5_1.html"
        self.header = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36"
        }

    def send_request(self):
        response = requests.get(self.url1, headers=self.header)
        html = response.content.decode("gbk")
        # with open("wenda.html", "a+", encoding="utf-8") as f:
        #     f.write(html)
        # print(html)
        return html

    def parse_data(self, html):
        re_obj = re.compile('<h4>.*?<a href=".*?">(.*?)</a>.*?</h4>', re.S)
        result = re_obj.findall(html)
        print(result)
        return result

    # def save_data(self, result):
    #     with open("data.txt", "a+", encoding="gbk") as f:
    #         for i in result:
    #             str1 = str(i) + "\n"
    #             f.write(str1)

    def run(self):
        # 发送请求
        html = self.send_request()
        # 解析数据
        result = self.parse_data(html)
        # 保存数据
        # self.save_data(result)

if __name__ == '__main__':
    Duanzi().run()
