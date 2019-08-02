# coding = utf-8  说明这个文件是以哪种格式存储的，python3里面可以不写
import requests

# 爬取贴吧页面
content = input("请输入贴吧名字:")
# 设置用户代理
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36"}
# 设置指定内容请求，也就是带参数的请求，参数格式都是字典类型的，包括用户代理和参数
url = "https://tieba.baidu.com/f?kw=" + content + "&ie=utf-8&pn={}"
# 设置页面参数
page_list = [url.format(x*50) for x in range(100)]
# print(page_list)
# 开始执行网页下载
for index, url in enumerate(page_list):
    response = requests.get(url, headers=header)

    # 开始保存数据
    file_name = "%s.html" % index
    # 这里读的方式是utf-8，那么写的方式也要是一样的，从浏览器读取出来的数据是字节类型的
    with open(file_name, "w", encoding="utf-8") as file:  # 这个utf-8指明的是此文件以utf-8打开，
        file.write(response.content.decode("utf-8"))  # 指明写的时候是以utf-8写，不填的话，默认utf-8