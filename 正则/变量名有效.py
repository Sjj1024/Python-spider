# 判断变量名是否有效
import re

# file_name = input("请输入变量名：")
# # \ｗ也包含中文，所以不能使用，要使用[０－９ａ-zＡ-Z_]*
# ret = re.match(r"^[a-zA-Z_]+[0-9a-zA-Z_]*$", file_name)
# try:
#     if ret.group():
#         print(file_name + "符合规范")
#     else:
#         print(file_name + "不符合规范")
# except:
#     print(file_name + "不符合规范")
    # 匹配五位以上的数字
    # ret = re.match(r"\d{5}\d*","10000242424")
    # print(ret.group())
    # # 匹配五位以上的数字,\d{5,}表示可以是５位或者多位，
    # ret = re.match(r"\d{5,}","10000242424")
    # print(ret.group())

#
# email = input("请输入变量名：")
# # 因为.是特殊字符，需要使用\转义,
# ret = re.match(r"^[a-zA-Z_]{4,20}@163\.com$", email)
# try:
#     if ret.group():
#         print(email + "符合规范")
#     else:
#         print(email + "不符合规范")
# except:
#     print(email + "不符合规范")


# 匹配６到１８个邮箱，必须以字母开头
email = input("请输入变量名：")
# 因为.是特殊字符，需要使用\转义,
ret = re.match(r"^[a-zA-Z][a-zA-Z_]{5,17}@163\.com$", email)
try:
    if ret.group():
        print(email + "符合规范")
    else:
        print(email + "不符合规范")
except:
    print(email + "不符合规范")