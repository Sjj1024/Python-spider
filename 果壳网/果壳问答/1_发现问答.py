import requests
import re


class Guoke(object):
    def __init__(self):
        self.url1 = "https://www.guokr.com/ask/hottest/"
        self.header = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36"
        }

    def send_request(self):
        response = requests.get(self.url1, headers=self.header)
        html = response.content.decode("utf-8")
        # with open("wenda.html", "a+", encoding="utf-8") as f:
        #     f.write(html)
        return html

    def parse_data(self, html):
        re_obj = re.compile('<h2><a target="_blank" href="(.*)">(.*)</a></h2>')
        result = re_obj.findall(html)
        return result

    def save_data(self, result):
        with open("data.txt", "a+", encoding="utf-8") as f:
            for i in result:
                str1 = str(i) + "\n"
                f.write(str1)

    def run(self):
        # 发送请求
        html = self.send_request()
        # 解析数据
        result = self.parse_data(html)
        # 保存数据
        self.save_data(result)

if __name__ == '__main__':
    Guoke().run()
