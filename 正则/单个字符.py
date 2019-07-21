# 匹配单个字符
"""
match 是从头开始匹配，serch可以不从头开始，加上^就和match一样了，
findall可以找到所需要的所有，形成一个列表返回
\d 匹配单个数字
\w 匹配单个单词字符，包含_下划线，除了特殊字符
\s 匹配空白字符
\n 匹配换行
\t 匹配空格

"""
import re

# \d 匹配单个数字
ret = re.match(r"[0-9]","1233adfa333")
print(ret.group())

# \w 匹配单个单词字符
ret = re.match(r"13\n3","13\n3")
print(ret.group())

# 匹配10到29的数，下面几个版本
ret = re.match(r"[1-2][0-9]","21")
print(ret.group())


ret = re.match(r"[12][0123456789]","21")
print(ret.group())


ret = re.match(r"[12]\d","21")
print(ret.group())

# \w匹配到字母,也包含中文等,范围超级广泛
ret = re.match(r"\w","21")
print(ret.group())

# \s匹配到空白字符，\n\t都是看不见的空白字符
ret = re.match(r"\s","\n")
print(ret.group())

# .匹配任意字符，除了\n，
ret = re.match(r".","aad")
print(ret.group())
