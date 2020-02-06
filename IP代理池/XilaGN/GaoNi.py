# 爬取西拉高匿代理，并判断是否可用
import re
import requests


class XiLa:
    def __init__(self):
        self.name = "西拉"
        self.url = "http://www.xiladaili.com/gaoni/"
        self.header = {
                        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36",
                    }

    def get_html(self):
        res = requests.get(self.url, headers=self.header)
        html_str = res.content.decode("utf-8")
        # print(html_str)
        return html_str

    def get_ips(self, html):
        ip_lists = re.findall(r"\d*\.\d*\.\d*\.\d*:\d*", html)
        print(ip_lists)
        return ip_lists

    def check_ip(self, ip):
        print("检查ip是否可用")
        check_url = "https://1024shen.com/"
        proxie = {"https": "https://" + ip}
        try:
            res = requests.get(check_url, headers=self.header, proxies=proxie, timeout=5)
            print(f"{proxie}可以使用++++++++++>")
        except:
            print(f"{proxie}不可以使用-------->")

    def run(self):
        print("开始获取可用ip")
        html_str = self.get_html()
        ips = self.get_ips(html_str)
        for i in ips:
            self.check_ip(i)


if __name__ == '__main__':
    print("开始执行爬虫程序")
    xi_obj = XiLa()
    xi_obj.run()