# 待定http://www.xiladaili.com/
import requests
from lxml import etree

url = "http://www.xiladaili.com/"
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36",
}

res = requests.get(url, headers=header)

html = etree.HTML(res.content.decode("utf-8"))

ip_list = html.xpath("//tr/td[1]/text()")

for i in ip_list:
    print(i)
