import re
# search模块和ｆｉｎｄａｌｌ模块
"""
match 从头开始匹配
search 匹配到个数据就停止，不再向后搜索
findall 匹配到全部的数据，返回一个搜索结果的结果
sub  替换，不止替换一个，返回替换后的字符串
split　切分，返回一个切分后的列表内容

"""

# search的应用：
ret = re.search(r"\d+","阅读数：999")
print(ret.group())

# search的应用,加上一个^就相当于ｍａｔｃｈ：
ret = re.search(r"\d+","阅读数：999")
print(ret.group())

# findall找出全部的，返回的是一个列表，不再有ｇｒｏｕｐ属性,
# 没有找到就返回一个空列表：
ret = re.findall(r"\d+","阅读数：999，阅读数：888，阅读数：999")
print(ret)

# sub替换,正则匹配到的，统统替换：
ret = re.sub(r"\d+","988", "阅读数：999，阅读数：1000")
print(ret)

# sub支持函数的调用：
def add(n):
    num = n.group()
    num = int(num) + 1
    return str(num)

# 将找到的内容传递到函数里，然后返回修改后的数据
ret = re.sub(r"\d+", add, "阅读数：999,阅读数：1000")
print(ret)


# spilt根据字符串进行切割字符串，返回一个列表：
ret = re.split(r"(:|,)", "阅读数:999,阅读数:1000")
print(ret)
