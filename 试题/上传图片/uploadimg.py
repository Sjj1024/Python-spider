# 上传图片到服务器
import requests
source_url = "https://www.louimg.com/"
url = source_url + "upload.php"
header = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.79 Safari/537.36",
            "referer": "https://www.louimg.com/"
        }
file = {"Filedata": ("first.jpg", open("2.jpg", "rb"), "image/jpeg")}

res = requests.post(url, headers=header, files=file)
sucstr = res.content.decode("utf-8")
if "suc" in sucstr:
    info_list = sucstr.split(",")
    jpg_url = source_url + info_list[0].split(":")[1] + info_list[1]
    print(jpg_url)


