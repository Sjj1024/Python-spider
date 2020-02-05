# 获取91免翻地址
import re
import requests

url = "https://a.w27.rocks/1.php"
header = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.79 Safari/537.36",
    # "referer": "https://g.wonderfulday21.live/"
}
res = requests.get(url, headers=header)
# print(res.status_code)
# print(res.url)
video_91zhi = res.url + "/index.php"
print(video_91zhi)

header["accept-language"] = "zh-CN,zh;q=0.9"
rel_91video = requests.get(video_91zhi, headers=header)
# print(rel_91video.status_code)
# print(rel_91video.content.decode("utf-8"))
html_91video = rel_91video.content.decode("utf-8")
# 提取91自拍站网址
photo_91pai = re.search(r'href="(.*?)" >自拍论坛', html_91video)
# print(photo_91pai.group(1))
url_91pai = photo_91pai.group(1) + "/index.php"
print(url_91pai)
