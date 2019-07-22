import requests

url = "https://www.12306.cn/mormhweb/"
response = requests.get(url, verify=False)
