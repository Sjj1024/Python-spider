# 下载斗鱼主页的图片
import re
import gevent
import urllib.request
from gevent import monkey
monkey.patch_all()


# 定义一个下载图片的方法，实现协成下载
def down_jpg(name, url):
    req = urllib.request.urlopen(url)
    count = req.read()
    with open(name, "wb") as jpg:
        jpg.write(count)
    print(name + "下载完成－－－－")


file_souce = open("douyu.html", "r", encoding="utf-8")
file_count = file_souce.read()
# print(file_count)

# file_jpg = re.findall(r"https://[^ ][^\"]*jpg",file_count)
file_jpg = re.findall(r"https://[^( |,|{|})]*jpg",file_count)
# print(file_jpg)
# for x in file_jpg:
#     print(x)
# 创建一个gevent.spawn的卵列表，将卵对象添加进去
spanwn_list = list()
start_name = 0
for x in file_jpg:
    start_name += 1
    spawn = gevent.spawn(down_jpg, str(start_name), x)
    spanwn_list.append(spawn)
# 将卵列表添加到协成中
gevent.joinall(spanwn_list)