import requests


# 采用面向对象的方式爬取百度贴吧的网页

# 定义一个贴吧爬虫的类
class TiebaSpider(object):
    # 1、实现init方法，定义要爬取的贴吧名称，用户代理头信息，还有通用url
    def __init__(self, tieba_name):
        self.tieba_name = tieba_name
        self.header = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                          "(KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36"}
        self.tou_url = "https://tieba.baidu.com/f?kw=" + tieba_name + "&ie=utf-8&pn={}"

    # 2、实现url管理器方法，让url生成保存到一个列表中
    def url_list(self):
        urllist = list()
        for x in range(10):
            urllist.append(self.tou_url.format(x * 50))
        return urllist

    # 3、向目标网址发送请求数据,得先传进来一个url
    def requst_get(self, url):
        print(url)  # 打印看一下这个url是啥
        # 发送请求，并获得相应
        response = requests.get(url, headers=self.header)
        return response.content.decode()

    # 4、获取请求到的数据，保存到本地
    def response_save(self, response, page):
        # 获取相应内容，获取页码信息
        page_num = "{}吧-第{}页.html".format(self.tieba_name, page)
        response = response
        with open(page_num, "w", encoding="utf-8") as file:
            file.write(response)
        print("%s保存成功......" % page)

    # 5、定义一全程调度的run方法
    def run(self):
        # 实现url管理器调度器
        url_list = self.url_list()
        # 循环调度ur
        for page, url in enumerate(url_list):
            # 调用发送请求方法，
            response = self.requst_get(url)
            # 调用保存内容的方法
            page_num = page + 1
            self.response_save(response, page_num)


# 实现main方法
if __name__ == '__main__':
    tieba = TiebaSpider("李毅")
    tieba.run()
