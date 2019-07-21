import re
# 分组等使用
"""
(a|b|c) 表示ａ，或者ｂ，或者ｃ，ａｂｃ都是正则表达式内容

(a|b|c)　ret.group(１)表示只要正则成功，就可以单独取出ａ包含的内容，
不取出所有的内容。




"""

# 分组的应用：
ret = re.match(r"^[a-zA-Z]{6,18}@(163|126)\.com","laowang@163.com")
print(ret.group(1))

# 分组的应用：
ret = re.match(r"([a-zA-Z]{6,18})@(163|126)\.com","laowang@163.com")
print(ret.group(1,2))



# 分组的应用,\1就表示匹配和(\w*)相同的内容,两个标签的时候，记得</\2>*</\1>
html1 = """<body><h1>hahaha</h1></body>"""
ret = re.match(r"<(\w*)><(\w*)>.*</\2>*</\1>",html1)
print(ret.group())



# 分组的应用,使用Ｐ给分组命名，
html1 = """<body><h1>hahaha</h1></body>"""
ret = re.match(r"<(?P<p1>\w*)><(?P<p2>\w*)>.*</(?P=p2)>*</(?P=p1)>",html1)
print(ret.group())