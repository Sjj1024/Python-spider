import requests
"""
使用ip代理访问网站
格式：proxy = {"协议":"协议+ip+端口","协议2":"协议2+ip+端口"}
使用方法：response = requests.post(url, headers=header, proxies=proxy)

"""

# 设置访问的url地址
url = "https://www.csdn.net/"
# 设置用户代理
header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36"}
# 设置IP代理
proxy = {"https": "35.229.113.175:443"}
# 发送访问请求
response = requests.get(url, headers=header, proxies=proxy)

# 查看访问状态
print(response.status_code)