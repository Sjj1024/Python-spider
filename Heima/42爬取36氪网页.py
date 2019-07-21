import requests
import json
import re

url = "https://36kr.com/"
res = requests.get(url)
# print(res.status_code)
# 保存网页内容
content = res.content.decode()

# 分析网页内容
news = re.findall(r"<script>window.initialState=(.*?)</script>", content)[0]
# print(news)
# 将json数据转换成python 类型
pycontent = json.loads(news)
print(pycontent)