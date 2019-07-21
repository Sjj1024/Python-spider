# !/usr/bin python
# _*_ coding:utf-8 _*_

import requests, json

class Jinshan(object):
    def __init__(self):
        self.base_url = 'http://fy.iciba.com/ajax.php?a=fy'
        self.header = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36"
        }
        # self.query_data = input("请输入翻译词语:")

    def send_request(self, form_data):
        response = requests.post(self.base_url, headers=self.header, data=form_data)
        data = response.content.decode("utf-8")
        print(data)
        return data

    def write_data(self, data):
        data_dict = json.loads(data)
        # print(data_dict)
        try:
            result = data_dict['content']['out']
        except:
            result = data_dict['content']['word_mean']

        # print(self.query_data + '----翻译的结果----->', result)
        print('----翻译的结果----->', result)

    def run(self):
        # 目标url
        # 构造请求体
        form_data = {
            "f": "aotu",
            "t": "aotu",
            "w": "美女"
        }

        # 发送请求
        data = self.send_request(form_data)
        # 保存数据

        self.write_data(data)


if __name__ == '__main__':
    fanyi = Jinshan()
    fanyi.run()
