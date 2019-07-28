# 使用xpath提取响应的文章链接和图片链接
import requests
import re

class Yuanqi(object):
    def __init__(self):
        self.url = "http://www.iyuanqi.com/flist/26103/new/1.html"
        self.header = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36",
        }

    def send_all_title(self):
        response =  requests.get(self.url, headers=self.header)
        res_html = response.content.decode("utf-8")
        return res_html

    def parse_title_url(self, res_html):
        re_obj = re.compile('<a href="(.*?)" target="_blank" class="block-img has-danmu">')
        url_list = re_obj.findall(res_html)
        return url_list

    def send_img_url(self, url):
        res_img_html = requests.get(url, headers=self.header)
        img_re_obj = re.compile('<p style="text-align: center;"><img src="(.*?)"')
        img_url_list = img_re_obj.findall(res_img_html.content.decode("utf-8"))
        return img_url_list

    def save_img(self, imgurl):
        image_name = imgurl[-12:]
        print("正在下载妹子{}".format(image_name))
        img_res_cont = requests.get(imgurl, headers=self.header)
        image_path = "some_img/" + image_name
        with open(image_path, "wb") as f:
            f.write(img_res_cont.content)
        print(image_name+"已下载完成哦---------->")

    def run(self):
        # 发送基本请求，获取文章列表
        res_html = self.send_all_title()

        # 先解析获取文章链接
        url_list = self.parse_title_url(res_html)

        # 遍历文章链接发送文章请求
        for url in url_list:
            end_url = "http://www.iyuanqi.com" + url
            img_url_list = self.send_img_url(end_url)
            for imgurl in img_url_list:
                # 请求图片的链接并保存
                self.save_img(imgurl)


if __name__ == '__main__':
    Yuanqi().run()