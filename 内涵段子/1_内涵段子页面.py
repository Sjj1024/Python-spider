# https://www.neihan-8.com/article/list_5_1.html
import requests
import re


class Duanzi(object):
    def __init__(self):
        self.url1 = "https://www.neihan-8.com/article/list_5_1.html"
        self.header = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36"
        }

    def send_request(self, url):
        response = requests.get(url, headers=self.header)
        html = response.content.decode("gbk")
        return html

    def parse_data(self, html):
        # 第一层解析
        re_obj = re.compile('<h4>.*?<a href=".*?">(.*?)</a>.*?</h4>.*?<div class="f18 mb20">(.*?)</div>', re.S)
        result1 = re_obj.findall(html)
        # 第二层解析，换行，标签等
        second_re_obj = re.compile(r"\s|\r|\n|<(.*?)>|\t|\u3000\u3000|&(.*?);")
        result2 = []
        for one in result1:
            title = second_re_obj.sub("", one[0])
            content = second_re_obj.sub("", one[1])
            result2.append((title, content))
        # print(result2)
        return result2

    def save_data(self, page, result):
        # 保存数据到文件中,result是一个元组，包含标题和内容
        with open("data.html", "a+", encoding="gbk") as f:
            f.write("----------------------------第{}页数据-------------------------------\n".format(page))
            for i in result:
                # i是一个元组title，content
                str1 = "标题：" + i[0] + "\n"
                str1 += "内容：" + i[1] + "\n\n"
                f.write(str1)

    def run(self):
        for page in range(1, 10):
            url = "https://www.neihan-8.com/article/list_5_{}.html".format(page)
            # 发送请求
            html = self.send_request(url)
            # 解析数据
            result = self.parse_data(html)
            # 保存数据
            self.save_data(page, result)
            print("第{}页数据已经保存完成------------>".format(page))


if __name__ == '__main__':
    Duanzi().run()
