import requests
from retrying import retry

url = "http://www.xiladaili.com/"

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36"
}

proxy = {
    "HTTPS": "http://12.34.56.79:9527"
}

# 函数里面只要有一处报错，就会进行下一次尝试，最多尝试3次
@retry(stop_max_attempt_number=3)
def request():
    print(11111111111)
    res = requests.get(url, headers=header, proxies=proxy, timeout=3)  # 响应超过3秒会报错
    assert res.status_code == 200  # 状态码不是200也会报错
    print(res.status_code)


request()

