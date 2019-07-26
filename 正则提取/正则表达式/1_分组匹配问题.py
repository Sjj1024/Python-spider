import re

texturl = '<h3><a href="htm_data/1907/16/3582293.html" target="_blank" id=""><font color=green>[原创]女教师的新婚夜在婚床上放飞自我[25P]</font></a></h3>'

res = re.findall(r'<h3><a href="(.*?)".*?<font color=green>(.*?)</font>', texturl)

print(res)
