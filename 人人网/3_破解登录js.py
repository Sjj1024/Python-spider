# 破解js的方式来等撸人人网
import requests
import js2py

if __name__ == '__main__':
    # 创建js环境对象
    context = js2py.EvalJs()
    # 创建session对象来保存cookie
    session = requests.session()
    session.headers = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Mobile Safari/537.36"
    }

    # codejs缺失rkey，所以需要发送请求获取
    rkey_url = "http://activity.renren.com/livecell/rKey"
    context.n = session.get(rkey_url).json()["data"]
    # print(n,"0000000000000000000")

    # 获取执行js需要的相关函数
    big_url = "http://s.xnimg.cn/a85738/wap/mobile/wechatLive/js/BigInt.js"
    big_js = session.get(big_url).content.decode()
    context.execute(big_js)

    rsa_url = "http://s.xnimg.cn/a85738/wap/mobile/wechatLive/js/RSA.js"
    rsa_js = session.get(rsa_url).content.decode()
    context.execute(rsa_js)

    bar_url = "http://s.xnimg.cn/a85738/wap/mobile/wechatLive/js/Barrett.js"
    bar_js = session.get(bar_url).content.decode()
    context.execute(bar_js)

    # 登录地址和参数
    login_url = "http://activity.renren.com/livecell/ajax/clog"
    context.t = {
        "phoneNum": "15670339119",
        "password": "15670339119",
        "c1": "-100",
        "rKey": "",
    }

    # 需要执行的js核心代码
    code_js = """
    t.password = t.password.split("").reverse().join(""),
                    setMaxDigits(130);
                    var o = new RSAKeyPair(n.e,"",n.n)
                      , r = encryptedString(o, t.password);
                    t.password = r,
                    t.rKey = n.rkey
    """

    context.execute(code_js)
    print(context.t)
