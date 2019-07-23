# 待定http://www.xiladaili.com/
import requests
from lxml import etree
from retrying import retry

# 目标url和请求头
url = "http://www.xiladaili.com/"
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36",
}

# 发送请求获取内容
res = requests.get(url, headers=header)
html = etree.HTML(res.content.decode("utf-8"))

# 使用xpath获取解析数据
ip_list = html.xpath("//tr/td[1]/text()")


# 定义一个函数筛选出可用的ip,最多尝试三次
save_use_ip = []
@retry(stop_max_attempt_number=3)
def tiao_ip(ip_dict):
    url2 = "https://www.baidu.com/"
    res = requests.get(url2, headers=header, proxies=ip_dict, timeout=3)  # 响应超过3秒会报错
    if res.status_code == 200:
        save_use_ip.append(ip_dict)
        print("{}ip可以使用".format(ip_dict))
    else:
        print("{}ip不可用---------------".format(ip_dict))
    assert res.status_code == 200


# 遍历出所有ip，过滤成字典
ip_dict_list = []
for ip in ip_list:
    ip_dict = {}
    if "\n" not in ip:
        ip_dict["https"] = ip
        ip_dict_list.append(ip_dict)


for ip_dict in ip_dict_list:
    try:
        print("正在尝试ip:{}".format(ip_dict))
        tiao_ip(ip_dict)
    except:
        continue

print(save_use_ip)