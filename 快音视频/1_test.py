import requests

# 测试视频下载
url1 = "http://183.215.105.254:6310/txmov2.a.yximgs.com/upic/2018/08/18/21/BMjAxODA4MTgyMTAyMDlfNDU0NDIzMzY5Xzc2NTkwMDc3MjlfMV8z_hd3_Bb5df930f97d936a0d8de66afa1bd710a.mp4"
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36"
}
ret = requests.get(url1, headers=header)
res_m4a = ret.content

with open("d710a.mp4", "wb") as f:
    f.write(res_m4a)
