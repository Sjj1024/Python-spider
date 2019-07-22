import requests


# 测试图片反爬
ret = requests.get("https://www.ttbcdn.com/d/file/p/2019-07-21/55cd45c7d858df43b9d32ec926094636.jpg")

with open("2.jpg", "wb") as filr:
    filr.write(ret.content)
