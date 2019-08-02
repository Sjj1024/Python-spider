import requests


url = "https://www.12306.cn/index/"
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36"}
# 设置当证书错误的时候，忽略提示
# 设置超时参数，当超过多少时间后没有响应，就忽略，执行下面的操作 timeout=3
response = requests.get(url, headers=header, verify=False)
print(response.status_code)

# 使用retry模块装饰器，可以装饰要请求的函数，帮助解决一些问题