# -*- coding: utf-8 -*-

import requests

new_url = "https://1024.fil6.tk/htm_data/1907/16/3586699.html"
header = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36",
    "cookie": "__cfduid=d991240ded8f691413d0a5238e78525ee1563844869; UM_distinctid=16c1c6ba0a3d2-0247f6cbe42a12-c343162-100200-16c1c6ba0a462d; PHPSESSID=cjkptobgiir2bmui06ttr75gi6; 227c9_lastvisit=0%091563848591%09%2Findex.php%3Fu%3D481320%26vcencode%3D5793155999; CNZZDATA950900=cnzz_eid%3D589544733-1563841323-%26ntime%3D1563848242"
}
print(new_url)
res = requests.get(new_url, headers=header)
print(res.content.decode('gb18030', 'ignore'))
# res_html = res.text()
with open("1.html", 'a+', errors="ignore") as f:
    f.write(res.content.decode('gb18030', 'ignore'))
