import json
import re
import requests
import jsonpath

url = 'http://www.lagou.com/lbs/getAllCitySearchLabels.json'
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36"
}
# response = requests.get(url, headers=header)
# py_dict = response.json()
# # 只能接收字典，或列表对象
# name_list = jsonpath.jsonpath(py_dict, "$..name")
# # print(name_list)
# with open("1.txt", "w", encoding="utf-8") as f:
#     f.write(response.content.decode("utf-8"))


# 从文件中读取到json数据,json.load(文件对象)
file_obj = open("1.txt", "r", encoding="utf-8")
json_str = json.load(file_obj)
print(type(json_str))

