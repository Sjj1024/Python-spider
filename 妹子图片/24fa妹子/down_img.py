import requests


url = "https://www.24fa.top/upload/2020-01/20012910476116.jpg"
header = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.79 Safari/537.36",
    "Referer": "https://www.24fa.top/MeiNv/2020-01/70912p2.html"
}
res = requests.get(url, headers=header)
print(res.status_code)
