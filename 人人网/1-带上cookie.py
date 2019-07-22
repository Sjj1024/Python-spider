import requests


class RenRen(object):
    def __init__(self):
        self.url = "http://www.renren.com/880151247/profile"
        self.header = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36",
            "Cookie":"anonymid=jvgl0npdp1ifjn; _r01_=1; depovince=GW; __utma=151146938.1421662606.1563692607.1563692607.1563692607.1; __utmz=151146938.1563692607.1.1.utmcsr=renren.com|utmccn=(referral)|utmcmd=referral|utmcct=/; ln_uact=15670339118; ln_hurl=http://hdn.xnimg.cn/photos/hdn521/20190509/1940/h_main_iXmR_497300002fae195a.jpg; jebe_key=f919d89f-48f9-4a84-be73-f6c666916f8f%7Cd97fe2b41316a25ce2fa2f4f1d268080%7C1563692692308%7C1%7C1563692691393; _de=81536BDC74E97447DFCB1E6B11F59233; jebecookies=7dc507f7-68bc-4f31-aa91-fa08f09dcaae|||||; JSESSIONID=abcDFqlUKnMtV7a9BGyWw; ick_login=f545093a-30a3-403e-8fa0-1deb7aed1354; p=3551a202d1191b576331d58897ee272c1; first_login_flag=1; t=8a0d06838468a58c2da7a8ff269e66601; societyguester=8a0d06838468a58c2da7a8ff269e66601; id=970747831; xnsid=e77e1a70; ver=7.0; loginfrom=null; wp_fold=0; jebe_key=f919d89f-48f9-4a84-be73-f6c666916f8f%7Cd97fe2b41316a25ce2fa2f4f1d268080%7C1563692692308%7C1%7C1563779428060"
        }

    def request_url(self):
        res = requests.get(self.url, headers=self.header)
        res_html = res.content.decode("utf-8")
        return res_html

    def run(self):
        # 获取url和参数
        # 发送请求
        html_content = self.request_url()

        # 解析数据
        with open("renren.html", "w", encoding="utf-8") as f:
            f.write(html_content)

        # 保存数据


if __name__ == '__main__':
    RenRen().run()
