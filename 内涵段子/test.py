import re

str1 = '<h4><a href="/article/45117.html"><b>原来月老和孟婆曾是一对</b></a></h4>'
re_obj = re.compile('<a href=".*">(.*)</a>')
result = re_obj.findall(str1, re.S)
print(result)