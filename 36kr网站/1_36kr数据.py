import requests
import re
import json


class KrSpider(object):
    def __init__(self):
        self.base_url = 'https://36kr.com/'
        self.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko"}

    # 1. 发请求
    def send_request(self):
        data = requests.get(self.base_url, headers=self.headers).content.decode('utf-8')
        return data

    # 2.解析数据 正则
    def parse_data(self, data):
        # pattern = re.compile('<h3 data-stat-click="(.*)">(.*)</h3>')

        pattern = re.compile('<script>window.initialState=(.*)</script>')
        # pattern = re.compile('<script>var props=(.*),locationnal=')
        result_list = pattern.findall(data)

        dict_data = json.loads(result_list[0])

        print(dict_data["homeData"]["data"]["latestArticle"]['data'])
        print(len(dict_data["homeData"]["data"]["latestArticle"]['data']))
        return dict_data["homeData"]["data"]["latestArticle"]['data']

    # 3.保存
    def write_file(self, data):
        # with open('0736kr.html', 'w') as f:
        #     f.write(data)
        json.dump(data, open('0736kr.json', 'w'))

    # 4.调度
    def run(self):
        # 1. 发请求
        data = self.send_request()
        # 2.解析
        parse_data = self.parse_data(data)

        # 3.存储
        self.write_file(parse_data)


if __name__ == '__main__':
    KrSpider().run()
