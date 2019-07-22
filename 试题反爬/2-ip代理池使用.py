import requests

url = "https://www.csdn.net/"

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36"
}

proxy = {
    "HTTPS": "36.90.50.28:8181"
}

res = requests.get(url, headers=header, proxies=proxy)

print(res.status_code)
