# 图片下载
import urllib.request
import gevent
from gevent import monkey
monkey.patch_all()


def down_jpg(name, url):
    req = urllib.request.urlopen(url)
    count = req.read()
    file = open(name, "wb")
    file.write(count)
    file.close()
    print(name+"下载完成")

# g1 = gevent.spawn(down_jpg, "01.png", "https://rpic.douyucdn.cn/asrpic/190412/5286883_1101.png")
# g1.join()


gevent.joinall([
    gevent.spawn(down_jpg, "01.png", "https://rpic.douyucdn.cn/asrpic/190412/5286883_1101.png"),
    gevent.spawn(down_jpg, "02.jpg", "https://i.meizitu.net/2019/03/23d02.jpg")
])