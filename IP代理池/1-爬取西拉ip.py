# 待定http://www.xiladaili.com/
import requests

url = "http://www.xiladaili.com/"
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36",
}

res = requests.get(url)
# print(res.content.decode("UTF-8"))
with open("xila.html", "a+", encoding="UTF-8") as f:
    f.write(res.content.decode("UTF-8"))