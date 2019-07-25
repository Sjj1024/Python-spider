import requests

# 测试图片反爬
url1 = "https://wvw.rosmm33.com/pic/upload/2019/07/25/rosikz-No1138-3-1220524767.jpg"
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36"
}
ret = requests.get(url1, headers=header, verify=False)
res_jpg = ret.content

with open("rose.jpg", "wb") as f:
    f.write(res_jpg)
