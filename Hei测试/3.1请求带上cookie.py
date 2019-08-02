import requests

"""请求带上cookie,有两种方法，这是第一种，第二种是将cookie转换成字典形式，然后通过get请求的时候赋值：Cookies=Cookielist"""
url = "http://www.renren.com/970747831/profile"
header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36",
          "Cookie":"anonymid=jvgl0npdp1ifjn; depovince=GW; jebecookies=a5d14b42-d6c9-4ba4-bbe7-5e29d7dacb08|||||; _r01_=1; JSESSIONID=abcGyNf3X2vnN7_ZPzCQw; ick_login=9a78f2a5-4764-4f14-9d50-5d8e78e2dbfb; _de=81536BDC74E97447DFCB1E6B11F59233; p=9e5d2af93025ca7ee3072048845ba7b41; first_login_flag=1; ln_uact=15670339118; ln_hurl=http://head.xiaonei.com/photos/0/0/men_main.gif; t=7839f7d3bff8defe46371e4c3aee8d561; societyguester=7839f7d3bff8defe46371e4c3aee8d561; id=970747831; xnsid=63990ba1; loginfrom=syshome; jebe_key=f919d89f-48f9-4a84-be73-f6c666916f8f%7Cd97fe2b41316a25ce2fa2f4f1d268080%7C1557402155533%7C1%7C1557402154455; wp_fold=0; XNESSESSIONID=256aa60664d9; WebOnLineNotice_970747831=1"
          }
response = requests.get(url, headers=header)
print(response.status_code)

with open("ren.html", "w", encoding="UTF-8") as f:
    f.write(response.content.decode())
