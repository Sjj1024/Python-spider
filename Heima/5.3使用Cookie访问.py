import requests
"""
使用带cookie参数访问目标网址：

"""
# 1、实例化session
session = requests.session()

# 2、使用session发送post请求，把cookie设置在session中发送
header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36"}
url = "https://passport.csdn.net/login"
post_date = {"email": "648133599@qq.com", "password": "12345678"}

session.post(url, data=post_date, headers=header)
# 3、请求个人主页，带上cookie，就会请求成功
post_url = "https://me.csdn.net/weixin_44786530"
response = requests.get(post_url, headers=header)

# 查看请求状态
print(response.status_code)