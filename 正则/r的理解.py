# r的理解
import re


# 在系统里面,\表示转义
str1 = "d:\a\b\c\t\c"
print(str1)
# 结果：c:\c,为什么\c不发生转义？

#
# # 要想输出\，就得使用\\
# # str1 = "c:\\a\\b\\c"
# print(str1)
# # 结果: c:\a\b\c
#
#
# # 正则表达式里,\\也表示一个\,字符串里\\也表示一个\，
# # 要想匹配这个字符串，该怎么操作？
# str1 = "c:\\a\\b\\c"
# ret = re.match("c:\w*\c", str1)
# print(ret.group())
# # 结果: c:

# 正则表达式里,\\也表示一个\,字符串里\\也表示一个\，
# # 加个ｒ来转义一下，结果是
# str1 = "c:\\a\\b\\c"
# ret = re.match(r"c:\w*\\", str1)
# print(ret.group())
# # 结果: c: