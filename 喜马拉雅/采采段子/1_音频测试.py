import requests

# 测试音频下载
url1 = "https://fdfs.xmcdn.com/group63/M01/D9/4F/wKgMaF03NnzglzEGATMiHPB_PT0881.m4a"
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36"
}
ret = requests.get(url1, headers=header)
res_m4a = ret.content

with open("PT0881.m4a", "wb") as f:
    f.write(res_m4a)
