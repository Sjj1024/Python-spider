import requests

# 测试图片反爬,妹子图竟然是带上了referer反爬
url1 = "https://i.meizitu.net/2019/08/01d01.jpg"
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36",
    "Referer": "https://www.mzitu.com/197306/1"
}
ret = requests.get(url1, headers=header)
res_jpg = ret.content

with open("06b01.jpg", "wb") as f:
    f.write(res_jpg)
