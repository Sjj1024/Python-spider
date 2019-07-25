import requests

# 测试图片反爬
url1 = "https://www.ttbcdn.com/d/file/p/2019-02-10/40df9ce5d4e5a47a2910cfa43b716aef.jpg"
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36"
}
ret = requests.get(url1, headers=header, verify=False)
res_jpg = ret.content

with open("smoke.jpg", "wb") as f:
    f.write(res_jpg)
