import requests
import json
from pprint import pprint

"""
通过json获取数据，使用json的时候，需要在头信息中加上reference字段
其实像这种json的url地址中有些参数是可以删掉的，例如：
os=ios&for_mobile=1&callback=jsonp1&  这句话是完全没有用的，
还有&loc_id=108288&_=0  这句话也是没有用的，如果你不确定些参数的含义，可以将这些参数删除掉之后试一下，看是否能请求成功，
如果可以请求成功，表示这些参数是没有用的，不然的话是有用的


使用json常用的方法，来讲json数据和python数据相互转化：
"""
url = "https://m.douban.com/rexxar/api/v2/subject_collection/tv_variety_show/items?start=0&count=18"
header = {
    "Referer": "https://m.douban.com/tv/tvshow",
    "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) "
                  "Version/11.0 Mobile/15A372 Safari/604.1 "
}

res = requests.get(url, headers=header)
# 使用json.load方法:将获取到的json类文件对象中的字符串提取出来，转换成python类型数据(转成字典类型)
jsonStr = res.content.decode()
pyStr = json.loads(jsonStr)
print(type(pyStr))
# print(pyStr)
#  使用pprint进行美化打印
# pprint(pyStr)

# 使用json.dump：将python字典转成json字符串
with open("json.txt", "w", encoding="utf-8") as file:
    # ensure_ascii参数默认会让pyStr中的中文使用ascii码方式进行编码，默认为True，设为False即可
    # indent 参数可以将格式变得优美，意思是将子元素和父级元素之间缩进多少个字符
    file.write(json.dumps(pyStr, ensure_ascii=False, indent=2))

with open("json.txt", "r") as file2:
    # file2是一个类文件对象，
    cont = json.load(file2)
    print(cont)