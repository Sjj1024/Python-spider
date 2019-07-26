# fiandall里面如果有^和$ 符会是什么结果?
import gevent
import urllib.request
import re


html1 = """https://dfad.jpgdf"sdf.jpgsdhttps://"s.jpg https://dad.jpg"""
ret = re.findall(r"https://[^\"]*?[^ ]*?jpg", html1)
print(ret)

html1 = """https://dfad.jpgdf"sdf.jpgsdhttps://"s.jpg https://dad.jpg"""
ret = re.findall(r"https://[^\"]+?[^ ]+?jpg", html1)
print(ret)

html1 = """https://dfad.jpgdf"sdf.jpgsdhttps://"s.jpg https://dad.jpg"""
ret = re.findall(r"https://[^\"].*?[^ ].*?jpg", html1)
print(ret)

# fiandall里面如果有^和$ 符会是什么结果?　结果：['https://dad.jpg']
# html1 = """https://dfad.jpgdf"sdf.jpgsdhttps://"s.jpg https://dad.jpg"""
# ret = re.findall(r"https[^ ]*?jpg$", html1)
# print(ret)
