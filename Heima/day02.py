import requests

# 模拟浏览器，设置请求头中的用户代理
# 内容是一个字典，所以不要写错了
content = input("请输入要查的内容:")

header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36"}
# 设置指定内容请求，也就是带参数的请求，参数格式都是字典类型的，包括用户代理和参数
parmes = {"wd": content}

# 第一种带参数的请求：
# ret = requests.get("http://www.baidu.com/", params=parmes, headers=header)

# 第二种使用formet格式,挖坑填充，这种比较流行
ret = requests.get("https://www.baidu.com/?wd={}".format(content))
print(ret.status_code)  # 打印一下状态码，就知道请求成功没有
print(ret.request.url)  # 打印一下请求的url地址有没有变化
# print(ret.content.decode("utf-8"))
