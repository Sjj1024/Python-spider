import re

texturl = "type='image'>&nbsp;<br><br><input data-link='https://www.kanjiantu.com/image/h1AuC' data-src='https://www.kanjiantu.com/images/2019/07/20/IMG_20190718_233233b2c56b681efaaad5.md.jpg' "

res = re.findall(r"data-src='(.*?)'", texturl)

print(res)
