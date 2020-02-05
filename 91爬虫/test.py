import requests


def get_redirect_url():
    # 重定向前的链接
    url = "重定向前的url"
    # 请求头，这里我设置了浏览器代理
    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}
    # 请求网页
    response = requests.get(url, headers=headers)
    print(response.status_code) # 打印响应的状态码
    print(response.url) # 打印重定向后的网址
    # 返回重定向后的网址
    return response.url


if __name__ == '__main__':
    redirect_url = get_redirect_url()