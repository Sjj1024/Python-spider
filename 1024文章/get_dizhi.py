import json
import requests

url = "https://get.xunfs.com/app/listapp.php"
header = {"Content-Type": "application/x-www-form-urlencoded"}
data = {"a": "get18", "system": "ios"}

res = requests.post(url=url, headers=header, data=data)
res_json = json.loads(res.content.decode("utf-8"))
print(res_json)
# 打印出地址信息和更新时间
home_url = [res_json["url1"], res_json["url2"], res_json["url3"], res_json["update"]]
# print(home_url)

for i in home_url:
    url = "https://" + i + "/"
    try:
        res = requests.get(url, timeout=5)
        if res.status_code == 200:
            print(url)
    except:
        continue