# 检验代理IP是否可用
import requests


url = "https://1024shen.com/"
header = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.79 Safari/537.36"
}
# 代理字典格式:{"协议": "代理ip：代理端口"}
proxie = {'https': '208.255.161.107:3128'}

try:
    # 没有报错说明可以用，返回状态码为200
    res = requests.get(url, headers=header, proxies=proxie, timeout=3)
    print(res.status_code)
except:
    print("代理不可用")