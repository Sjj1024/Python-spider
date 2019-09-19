import requests

# 测试淘宝评论竟然是带上了referer反爬
url1 = "https://github.com/Sjj1024/image-all/edit/master/2-up.py"
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36",
    "Cookie": "_ga=GA1.2.122455557.1552987940; _octo=GH1.1.3155740.1552987947; _device_id=6c3a29ec42caf7fd2347a2036a068ffb; user_session=HeZoJPfYbcgLivS5LWi9dd8PDQVEyFdxUTVnqnihuSfCIS28; __Host-user_session_same_site=HeZoJPfYbcgLivS5LWi9dd8PDQVEyFdxUTVnqnihuSfCIS28; logged_in=yes; dotcom_user=Sjj1024; has_recent_activity=1; _gat=1; tz=Asia%2FShanghai; _gh_sess=cW1Td3lTdlBsWU9iaHd5aXVUVGphZnNsNVRyc1FaSUZuY1FZNlEvalZWdFYrc2JabnNiWTUzVnNIdlZNa3h2ZnkwYlJPby9CVCtqakV3bW8yaXpuSzZXMU42SGxIZmNEc2tCQ2FTc0x6bjZYejlIeHBJdVVuLytUKzBoOG04ZHZ0VW9KOGtLc3Z3bFh6N1EzdlFLamlGc1J4ZTFDMys1UzcyV3FvaVJ5QlV2eUthMFUyQnNvSHl3cXk5by9nUCt2a2trMTEwWGJJNkxaZHNXS2I5KzBVYmhYTytVaHFNU1pyQzEvRmU2bHNCMTZtZjlTTFYrUFFGNVRxdzhUeFRmcURlMUZnNU5md0grVUhBenQ5dWx5VzhNTC9yS3hBM3dPY3l0WHhrOVA0ZTAwVzJzbVQ2WDQybE51RTczTDkxQWJIdGNpenNlZFREOU4reUdKa29pSmxnPT0tLXMwU0MzRUhQSVhxb0hiWmVtMHlheWc9PQ%3D%3D--f639d6d39e26ef04f1319c6ab59bf7da2bca1a83",
    # "Referer": "https://item.taobao.com/item.htm?spm=a219r.lm5734.14.1.552b523cSi2MBs&id=575740530252&ns=1&abbucket=10"
}
data = {"authenticity_token":"4udKxBjg+YddP5n3Jdw1ZEtzIcp+9zim+zBN4jmi9b7W4YjG/d27SnwJDUIN7Z6LFT91xWgQahJsT2+fJVC31g==",
        "value":"我爱你",
        "filename":"2-up.py",
        "new_filename":"2-up.py",
        "content_changed":True,
        "target_branch":"master",
        "commit":"96326f787261f824713e557f75651c0e0f3c7e13",
        "same_repo":1,
        "placeholder_message":"Update 2-up.py",
        "commit-choice":"direct"
        }
ret = requests.post(url1,data=data,headers=header)
res_json = ret.content.decode("utf-8")
with open("github.html", "w", encoding="utf-8") as f:
    f.write(res_json)
