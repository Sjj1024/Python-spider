import json

import requests


class JinShan(object):
    def __init__(self):
        self.url = "http://fy.iciba.com/ajax.php?a=fy"
        self.header = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36"
        }

    # 定义发送函数
    def request_url(self, data):
        res = requests.post(self.url, headers=self.header, data=data)
        res_json = res.content.decode("utf-8")
        res_dict = json.loads(res_json)
        return res_dict

    # 定义解析数据的方法
    def parse_dict(self, end_dict):
        try:
            ends_data = end_dict["content"]["out"]
        except:
            ends_data = end_dict["content"]["word_mean"]
        print(ends_data)

    def run(self):
        # 获取url及参数
        text = input("请输入：")
        data_parms = {
            "f": " auto",
            "t": " auto",
            "w": text
        }
        # 发送请求
        res_dict = self.request_url(data_parms)

        # 解析数据
        self.parse_dict(res_dict)


if __name__ == '__main__':
    while True:
        JinShan().run()
