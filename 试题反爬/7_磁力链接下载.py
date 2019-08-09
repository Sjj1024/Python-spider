import requests

# 测试图片反爬,妹子图竟然是带上了referer反爬
url1 = "http://www.3btbtt.com/attach-download-fid-1-aid-125130.htm"
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36",
}
ret = requests.get(url1, headers=header)
res = ret.content

with open("3e.torrent", "wb") as f:
    f.write(res)
