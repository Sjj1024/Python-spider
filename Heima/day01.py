# 认识requests模块
import requests

ret = requests.get("http://www.baidu.com/")
# 给请求到的数据设置解码方式
# 第一种方式：指定请求的内容解码方式是utf-8。因为是encodeing，名词，编码方式，不是encode，
# 所以只能用等号，因为ret.text默认会根据头部信息猜测解码方式，有时候会出错，这次就是，
# 如果不说明解码方式，返回的数据就是str类型的
ret.encoding = ("utf-8")
print(ret.text)

# 第二种方式：对请求到的数据内容以utf-8解码，因为服务器返回的数据是以utf-8编码的。
print(ret.content.decode("utf-8"))

# 了解requests中其它的方法
print(ret.status_code)  # 获得相应状态码
print(ret.headers)  # 获得相应头
print(ret.url)  # 获得相应url，有时候请求地址和相应地址URl是不一样的，例如302或307重定向的时候
