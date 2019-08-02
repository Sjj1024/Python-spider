import requests
import json


# 使用post请求，更安全的获取数据，编写一个百度翻译的代码,
# 因为返回的数据是json类型，所以需要json模块来变成python字典数据

# 定义一个翻译的类
class Fanyi(object):
    def __init__(self, cont):
        self.header = {
            "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1"}
        self.cont = cont
        # 设置翻译的接口，下面的就是
        self.touurl = "https://fanyi.baidu.com/basetrans"

    # 设置url请求，
    def url_post(self):
        post_date = {"query": self.cont,
                     "from": "zh",
                     "to": "en"}
        print(post_date)
        return post_date

    # 发送请求
    def requst_post(self, url, data):
        # 发送请求，获取响应
        response = requests.post(url, data=data, headers=self.header)
        # response是一个对象，是要返回的是一个字符串，所以要countent，而且要将byte解码成str类型
        print(response.status_code)
        return response.content.decode()

    # 获取响应
    def res_content(self, json_str):
        # 将接收到的数据，转变成python可识别的字典数据
        temp_dict = json.loads(json_str)
        print(temp_dict)
        # 因为获得到的是复杂的字典数据，需要一层一层获取
        contents = temp_dict["trans"][0]["dst"]

        print("{} : {}".format(self.cont, contents))

    # 全程调度程序
    def run(self):
        # 获取请求信息post
        post_count = self.url_post()
        # 发送请求数据,只需要传送url和数据就可以，用户代理自己有，得到的是一个json字符串
        response = self.requst_post(self.touurl, data=post_count)
        # 获取响应，并将json转换成Python可以识别的字典，然后提取出想要的数据
        self.res_content(response)


if __name__ == '__main__':
    fanyi = Fanyi("你好")
    fanyi.run()