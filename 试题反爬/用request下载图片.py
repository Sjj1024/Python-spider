import requests

# 测试图片反爬
url1 = "https://www.ttbcdn.com/d/file/p/2019-07-21/55cd45c7d858df43b9d32ec926094636.jpg"
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36"
}
ret = requests.get(url1, headers=header)
res_jpg = ret.content

with open("2.jpg", "wb") as f:
    f.write(res_jpg)
