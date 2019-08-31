import requests

url1 = "https://item.jd.com/6051045.html"
url2 = "https://search.jd.com/s_new.php?keyword=%E6%89%8B%E6%9C%BA&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&psort=3&cid2=653&cid3=655&page=1&s=175&scrolling=y&log_id=1567233603.68952&tpl=3_M&show_items=53401701313,44126874550,100001893367,100003603159,100001485602,34487179057,7621213,50074585240,53372677476,31301071649,52588010239,100003258297,100004739684,43769837873,8348845,50645404316,39073847898,100000322417,31581424073,4938578,42847047935,7701235,100002544820,32896352259,100004363706,100002624532,47847150993,100006567258,52766070431,100006785480"
url3 = "https://search-x.jd.com/Search?callback=jQuery6938376&area=2&enc=utf-8&keyword=%E6%89%8B%E6%9C%BA&adType=7&urlcid3=655&page=4&ad_ids=291%3A24&xtest=new_search&_=1567233606172"
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36",
    "Referer":"https://search.jd.com/Search?keyword=%E6%89%8B%E6%9C%BA&enc=utf-8&psort=3&page=1"
}

ret = requests.get(url2, headers=header)
print(ret.status_code)
html_str = ret.content.decode("utf-8")

# 保存下载好的页面内容
with open("shou5.html", "w+", encoding="utf-8") as f:
    f.write(html_str)

# 开启死循环测试ip
# num = 1
# while True:
#     ret = requests.get(url1)
#     print(f'状态码-----------------------------{ret.status_code}')
#     num += 1
#     print(f'请求次数{num}')
