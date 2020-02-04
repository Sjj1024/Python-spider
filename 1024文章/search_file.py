import requests
from urllib.parse import quote
import re

keyword = "尤物"
url_keyword = quote(keyword, encoding="gbk")

# url = f"https://cl.202d.cf/search.php?step=2&s_type=forum&keyword={url_keyword}&method=AND&pwuser=&sch_area=0&f_fid=8&sch_time=all&orderway=postdate&asc=DESC&randcode_a=74&randcode_b=74"
url = f"https://cl.202d.cf/search.php?step=2&s_type=forum&keyword=%C3%C0%C5%AE&sch_area=0&f_fid=16&sch_time=all&method=AND&orderway=postdate&asc=DESC&randcode_a=79&randcode_b=79"

header = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.79 Safari/537.36",
    "cookie": "__cfduid=dfa225c67782ccf6bc9b627951576951d1580623976; UM_distinctid=1700487e65b113-067c0c08f57a2-6701434-100200-1700487e65c165; 227c9_ck_info=%2F%09; 227c9_groupid=8; PHPSESSID=rgq46966ompb4dv53p2r9t9jp1; 227c9_ipfrom=520a1c6a765bfad3e68f6d4977e12749%09Unknown; 227c9_postReplyLastData=37981431024; CNZZDATA950900=cnzz_eid%3D1515184249-1580622728-https%253A%252F%252Fcl.202d.cf%252F%26ntime%3D1580707225; 227c9_winduser=AAVQVlcFO1cACwBUBFVWWFdXAwxUVVFQB1YMCVpQU1cIAFEABFBSaw%3D%3D; 227c9_lastvisit=0%091580711565%09%2Fsearch.php%3F"
}

res = requests.get(url, headers=header)
# print(res.content.decode("gbk"))
str_res = res.content.decode("gbk")
want_content = re.search(r'<table width="100%" cellspacing="0" cellpadding="0">.*</table>', str_res, re.S)
# print(want_content.group())
res_content = want_content.group()
repl_cont1 = res_content.replace('<td width="3%" class="h"><b>狀態</b></td>', "")
repl_cont2 = re.sub(r'<td align="center">.*?</td> ', "", repl_cont1)
# print(repl_cont2)
repl_cont3 = f"""
<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<title>cl搜索结果</title>
</head>
<body>
{repl_cont2}
</body>
</html>
"""

# print(repl_cont3)
rel_source = 'href="' + "https://cl.202d.cf/"
repl_cont4 = repl_cont3.replace('href="', rel_source)
print(repl_cont4)

