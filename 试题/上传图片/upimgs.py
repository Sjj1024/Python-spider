# 执行一个文件夹，上传多张图片到服务器，返回所有图片外联
import os
import requests


class UpFile:
    def __init__(self, localpath):
        self.name = "上传文件到服务器"
        self.localpath = localpath
        self.sourceurl = "https://www.louimg.com/"
        self.uploadurl = self.sourceurl + "upload.php"
        self.wailian_url = []
        self.header = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.79 Safari/537.36",
            "referer": "https://www.louimg.com/"
        }

    def get_imgs(self):
        print("获取文件夹中的所有图片文件")
        files = os.listdir(self.localpath)
        source_list = [os.path.join(self.localpath, i) for i in files]
        return source_list

    def uploadone(self, jpgfile):
        print("上传单张图片")
        res = requests.post(self.uploadurl, headers=self.header, files=jpgfile)
        sucstr = res.content.decode("utf-8")
        if "suc" in sucstr:
            info_list = sucstr.split(",")
            jpg_url = self.sourceurl + info_list[0].split(":")[1] + info_list[1]
            self.wailian_url.append(jpg_url)
            print(jpg_url)

    def start_load(self, source_jpgs):
        print("开始上传图片序列")
        for index, value in enumerate(source_jpgs):
            jpg_name = str(index + 1) + ".jpg"
            file = {"Filedata": (jpg_name, open(value, "rb"), "image/jpeg")}
            self.uploadone(file)

    def run(self):
        print("开始真正的上传")
        source_jpgs = self.get_imgs()
        self.start_load(source_jpgs)
        print(self.wailian_url)


if __name__ == '__main__':
    localpath = "G:\PaChong\Python-spider\妹子图片\LoveGirl盖尔\偷拍自拍\!如同透過窗欞的清新空氣沁人心扉[12P]"
    upuser = UpFile(localpath)
    upuser.run()
