import re
"""
匹配多个字符
+ 至少有一个，相当于{1，+～}
* 可以有无限多，也可以没有，相当于{0， +～}
? 可有可无，相当于{0,1}
{1,3} 表示可以有1,2,3个


"""

#　大括号表示可以有多少个前面的字符
ret = re.match(r"\d{1,5}","124444")
print(ret.group())

#　大括号表示可以有多少个前面的字符
ret = re.match(r"\d?","124444")
print(ret.group())

# 如果字符串里内容较多，可以使用”“”　内容“”“括起来
html1 = """iadfadfa
adad
adafd
dfsadsfadf
"""
ret1 = re.match(r".*", html1, re.S)
print(ret1.group())