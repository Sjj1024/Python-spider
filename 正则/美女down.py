# 下载美女网图片
import urllib.request
import re
import gevent
from gevent import monkey

monkey.patch_all()


# 定义一个图片下载函数，来实现多线程
def down_jpg(name, url):
    print("正在下载" + name + "......")
    req = urllib.request.urlopen(url)
    count = req.read()
    with open(name, "wb") as jpg:
        jpg.write(count)
    print(name + "下载完成－－－－")


# 打开美女网源码
file_souce = open("meinv.html", "r", encoding="utf-8")
file_count = file_souce.read()
# print(file_count)

# 使用正则表达式，匹配出美女图片网址的列表，
file_jpg = re.findall(r"https://[^ ]*jpg", file_count)
print(file_jpg)

# 将图片网址加入到协成下载器中
# 制作一个协成产卵的列表，将每个卵对象添加进入，定义一个文件名自变量，随着循环，改变名字
list_spawn = list()
start_name = 0
for url in file_jpg:
    start_name += 1
    spawn_file = gevent.spawn(down_jpg, str(start_name) + ".jpg", url)
    list_spawn.append(spawn_file)
# print(list_spawn)
# g1 = gevent.spawn(down_jpg, "01.png", "https://rpic.douyucdn.cn/asrpic/190412/5286883_1101.png")
# g1.join()

gevent.joinall(list_spawn)
