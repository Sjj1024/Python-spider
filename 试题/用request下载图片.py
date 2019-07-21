import requests


ret = requests.get("https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1557064014233&di=9e2b1c6bf123c20b8b98def40800d87b&imgtype=0&src=http%3A%2F%2Fd.hiphotos.baidu.com%2Fimage%2Fpic%2Fitem%2F024f78f0f736afc3d229357ebd19ebc4b7451287.jpg")

with open("1.jpg","wb") as filr:
    filr.write(ret.content)