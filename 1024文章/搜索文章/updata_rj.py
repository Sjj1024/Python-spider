import re
import json
import requests


url = "https://www.cnblogs.com/1024shen/p/12259399.html"
header = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.79 Safari/537.36"
}
res = requests.get(url, headers=header)
# print(res.content.decode("utf-8"))
str_html = res.content.decode("utf-8")
updata_ms = re.search(r"<pre>(.*?)</pre>", str_html)
# print(updata_ms.group(1))
updata_ms2 = updata_ms.group(1)
updata_ms3 = updata_ms2.replace("<br />", "")
updata_ms4 = updata_ms3.replace(" ", "")
updata_ms5 = json.loads(updata_ms4)
print(updata_ms5)