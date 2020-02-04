import json
import re
from urllib.parse import quote
import requests


class Tools_cl:
    def __init__(self):
        self.name = "工具"
        self.lei = 7
        self.dizhi = self.get_dizhi()
        self.cookie = {
            "xiaoyu": "__cfduid=dfa225c67782ccf6bc9b627951576951d1580623976; UM_distinctid=1700487e65b113-067c0c08f57a2-6701434-100200-1700487e65c165; PHPSESSID=rgq46966ompb4dv53p2r9t9jp1; 227c9_ipfrom=520a1c6a765bfad3e68f6d4977e12749%09Unknown; 227c9_postReplyLastData=37981431024; ismob=0; CNZZDATA950900=cnzz_eid%3D1515184249-1580622728-https%253A%252F%252Fcl.202d.cf%252F%26ntime%3D1580718027; 227c9_ck_info=%2F%09; 227c9_winduser=AQ1QUl0NOwYGCgVTBQIEBwJWAA0DBgRXAl1XWlIABAJVA1IEUQNba1QBAAYEAVFQUAQDWVVSAVNRUwBVAlFXWVNQUFMDB1dX; 227c9_groupid=6; 227c9_lastvisit=0%091580719747%09%2Fsearch.php%3F",
            "yunyun": "__cfduid=dfa225c67782ccf6bc9b627951576951d1580623976; UM_distinctid=1700487e65b113-067c0c08f57a2-6701434-100200-1700487e65c165; PHPSESSID=rgq46966ompb4dv53p2r9t9jp1; 227c9_ipfrom=520a1c6a765bfad3e68f6d4977e12749%09Unknown; 227c9_postReplyLastData=37981431024; ismob=0; CNZZDATA950900=cnzz_eid%3D1515184249-1580622728-https%253A%252F%252Fcl.202d.cf%252F%26ntime%3D1580718027; 227c9_ck_info=%2F%09; 227c9_winduser=AQ1XV1QFOwQMDABVUgVRVFdUBwRXV1MGVlFWXQUFBA9TBwJSDAdUawcHUVINC1UGAVUAVQICUVNWB1cGC11RDwJQAwIIVwUA; 227c9_groupid=6; 227c9_lastvisit=0%091580719949%09%2Findex.php%3F"
        }

    def get_dizhi(self):
        print("获取免翻地址")
        url = "https://get.xunfs.com/app/listapp.php"
        header = {"Content-Type": "application/x-www-form-urlencoded"}
        data = {"a": "get18", "system": "ios"}
        res = requests.post(url=url, headers=header, data=data)
        res_json = json.loads(res.content.decode("utf-8"))
        # 打印出地址信息和更新时间
        home_url = [res_json["url1"], res_json["url2"], res_json["url3"], res_json["update"]]
        for i in home_url:
            url = "https://" + i + "/"
            try:
                res = requests.get(url, timeout=5)
                if res.status_code == 200:
                    print(url)
                    return url
            except:
                continue
        return "地址获取失败"

    def search(self, keyword):
        url_keyword = quote(keyword, encoding="gbk")
        url = f"https://cl.202d.cf/search.php?step=2&s_type=forum&keyword={url_keyword}&sch_area=0&f_fid={self.lei}&sch_time=all&method=AND&orderway=postdate&asc=DESC&randcode_a=79&randcode_b=79"
        header = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.79 Safari/537.36",
            "cookie": "__cfduid=dfa225c67782ccf6bc9b627951576951d1580623976; UM_distinctid=1700487e65b113-067c0c08f57a2-6701434-100200-1700487e65c165; 227c9_ck_info=%2F%09; 227c9_groupid=8; PHPSESSID=rgq46966ompb4dv53p2r9t9jp1; 227c9_ipfrom=520a1c6a765bfad3e68f6d4977e12749%09Unknown; 227c9_postReplyLastData=37981431024; CNZZDATA950900=cnzz_eid%3D1515184249-1580622728-https%253A%252F%252Fcl.202d.cf%252F%26ntime%3D1580707225; 227c9_winduser=AAVQVlcFO1cACwBUBFVWWFdXAwxUVVFQB1YMCVpQU1cIAFEABFBSaw%3D%3D; 227c9_lastvisit=0%091580711565%09%2Fsearch.php%3F"
        }
        res = requests.get(url, headers=header)
        # print(res.content.decode("gbk"))
        str_res = res.content.decode("gbk")
        want_content = re.search(r'<table width="100%" cellspacing="0" cellpadding="0">.*</table>', str_res, re.S)
        # print(want_content.group())
        res_content = ""
        if want_content:
            res_content = want_content.group()
        repl_cont1 = res_content.replace('<td width="3%" class="h"><b>狀態</b></td>', "")
        repl_cont2 = re.sub(r'<td align="center">.*?</td> ', "", repl_cont1)
        print(1111111111111, repl_cont2)
        if not repl_cont2:
            repl_cont2 = "不好生意，没找到你要找的内容！"
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
        # rel_source = 'href="' + "https://cl.202d.cf/"
        rel_source = 'href="' + self.dizhi
        repl_cont4 = repl_cont3.replace('href="', rel_source)
        return repl_cont4

    def change_lei(self, fenlei):
        print("改变分类")
        if fenlei == "技术讨论区":
            self.lei = 7
        elif fenlei == "达盖尔的旗帜":
            self.lei = 16
        elif fenlei == "新时代的我们":
            self.lei = 8

    def updata(self):
        print("软件更新")
        self.message = {
            "version": "1.0",
            "user": "1024小神",
            "winlog": "我是提示说明窗口",
            "message": "我是更新说明"
        }