import requests

"""
通过json获取数据，使用json的时候，需要在头信息中加上reference字段
其实像这种json的url地址中有些参数是可以删掉的，例如：
os=ios&for_mobile=1&callback=jsonp1&  这句话是完全没有用的，
还有&loc_id=108288&_=0  这句话也是没有用的，如果你不确定些参数的含义，可以将这些参数删除掉之后试一下，看是否能请求成功，
如果可以请求成功，表示这些参数是没有用的，不然的话是有用的

"""
url = "https://m.douban.com/rexxar/api/v2/subject_collection/tv_variety_show/items?start=0&count=18"
header = {
    "Referer": "https://m.douban.com/tv/tvshow",
    "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) "
                  "Version/11.0 Mobile/15A372 Safari/604.1 "
}

res = requests.get(url, headers=header)
print(res.content.decode())
