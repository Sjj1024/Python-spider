import requests
from lxml import etree


# 测试淘宝评论竟然是带上了referer反爬
url1 = "https://cl.bbcb.xyz/thread0806.php?fid=7"
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36",
    "Cookie": "__cfduid=d567fea3867529dbeeff4932e33732dc81568896729; UM_distinctid=16d498878d917d-0a1cb592eeed6f-c343162-100200-16d498878da256; CNZZDATA950900=cnzz_eid%3D1623757828-1568893327-https%253A%252F%252Fcl.bbcb.xyz%252F%26ntime%3D1568893327; PHPSESSID=p04q2g1o12lbgcbp1en5l0dlf1; 227c9_ck_info=%2F%09; 227c9_winduser=BAIEAVZXaFAOBQVUAgNVBQAFAgAFVlJeBAIOAAdSBgdRDFNVCVEGPA%3D%3D; 227c9_groupid=8; 227c9_lastvisit=0%091568897590%09%2Fprofile.php%3F",
    "Referer": "https://cl.bbcb.xyz/index.php"
}
ret = requests.get(url1, headers=header)
res_json = ret.content.decode("gbk")
html = etree.HTML(res_json)
# 使用xpath提取数据
res_data = html.xpath('//*[@id="ajaxtable"]//tr/td[2]/h3/a/text()')
print(res_data)
