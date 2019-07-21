import urllib.request
import gevent
from gevent import monkey
monkey.patch_all()


# 协成里面报错的话，程序是在协成里等待还是退出这个协成了？退出这协成，相当于这个协成就废了，继续下一个协成
def down_jpg(name, url):
    req = urllib.request.urlopen(url)
    count = req.read()
    with open(name, "wb") as jpg:
        jpg.write(count)
    print(name + "下载完成－－－－")


gevent.joinall([
    gevent.spawn(down_jpg, "01.png", "https://rpic.douyucdn.cn/asrpic/190412/5286883_1101.png"),
    gevent.spawn(down_jpg, "02.jpg", "https://i.meizitu.net/2019/03/23d01.jpg"),
    # gevent.spawn(down_jpg, "03.png", "https://rpic.douyucdn.cn/asrpic/190412/5286883_1101.png"),
])

