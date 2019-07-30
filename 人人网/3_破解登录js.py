# 破解js的方式来等撸人人网
import requests
import js2py

if __name__ == '__main__':
    # 创建session对象来保存cookie
    session = requests.session()
    session.headers = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Mobile Safari/537.36"
    }

    # codejs缺失rkey，所以需要发送请求获取
    rkey_url = "http://activity.renren.com/livecell/rKey"
    n = session.get(rkey_url).json()["data"]

    # 需要执行的js核心代码
    code_js = """
    t.password = t.password.split("").reverse().join(""),
                    setMaxDigits(130);
                    var o = new RSAKeyPair(n.e,"",n.n)
                      , r = encryptedString(o, t.password);
                    t.password = r,
                    t.rKey = n.rkey
    """
