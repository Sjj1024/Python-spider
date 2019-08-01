import os
import re
from fontTools.ttLib import TTFont
import requests
from lxml import etree
from copy import deepcopy

"""
1.运行条件，安装包 pip3 install fontTools
2.在当前目录下创建font文件夹

"""


def FrontParse(HexNum, woffFileName):
    base_num = dict()  # 编号—数字
    base_obj = dict()  # 编号—对象
    # 注意，这里的编号与上面说的是一致的，只是前缀不一样，网页上看的是 &#x，爬下来的是\u，需要处理一下
    # 基准信息
    base_num["uniE1EE"] = "0"
    base_num["uniE226"] = "1"
    base_num["uniF53F"] = "2"
    base_num["uniF435"] = "3"
    base_num["uniF36E"] = "4"
    base_num["uniEFBE"] = "5"
    base_num["uniE63E"] = "6"
    base_num["uniF48A"] = "7"
    base_num["uniF813"] = "8"
    base_num["uniE442"] = "9"
    # 打开基准的woff文件
    BaseFontfile = TTFont('6e4929660c6569f64de7073025d802762076.woff')
    for key in base_num:
        base_obj[key] = BaseFontfile['glyf'][key]  # 获得woff内编号对应的字体对象
    fontFile = TTFont(woffFileName)
    obj = fontFile['glyf'][HexNum]
    for key in base_obj:  # 遍历找到相同的字体对象
        if obj == base_obj[key]:
            return base_num[key]


class MaoYan(object):
    """猫眼电影评分"""

    def __init__(self):
        self.start_url = "https://maoyan.com/films?offset={}"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36"
        }

    def send_request(self, url):
        response = requests.get(url, headers=self.headers)
        data = response.content.decode("utf-8")
        return data

    def parse_film_list(self, data):

        xp_data = etree.HTML(data)
        film_list = xp_data.xpath('//dl[@class="movie-list"]//dd')
        # print(film_list)
        # film_dict = dict()
        for film in film_list:
            film_dict = dict()
            film_dict["name"] = film.xpath('.//div[@class="channel-detail movie-item-title"]/a/text()')[0]
            film_dict["url"] = "https://maoyan.com" + film.xpath(
                './/div[@class="channel-detail movie-item-title"]/a/@href')[0]
            yield deepcopy(film_dict)

    def parse_score(self, film):
        """解析详情页字体反爬评分数据"""
        detail_content = self.send_request(film["url"])

        regex_woff = re.compile("(?<=url\(').*\.woff(?='\))")
        woff_url = "http:" + regex_woff.findall(detail_content)[0]

        regex_text = re.compile('(?<=<span class="stonefont">).*?(?=</span>)')
        span_list = regex_text.findall(detail_content)
        # 判断当前电影是否有评分
        if len(span_list[0]) == 17:
            # 编码转换为大写
            score_1 = "uni" + span_list[0][3:7].upper()
            score_2 = "uni" + span_list[0][12:16].upper()
            # 去掉请求协议
            localfn = 'font/' + os.path.basename(woff_url)
            with open(localfn, 'wb+') as f:
                f.write(requests.get(woff_url, headers=self.headers).content)

            score1 = FrontParse(score_1, localfn)
            score2 = FrontParse(score_2, localfn)

            score = score1 + "." + score2
            return score

    def run(self):
        for i in [0, 30]:
            data = self.send_request(self.start_url.format(i))
            for film in self.parse_film_list(data):
                score = self.parse_score(film)
                print("{}的评分:{}".format(film["name"], score))


if __name__ == '__main__':
    MaoYan().run()
