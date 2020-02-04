import json
import random
import time
import requests


# 访问个人信息
def get_info(username):
    info_url = f"https://api.github.com/users/{username}"
    header = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36"
    }
    # 获取到个人信息
    res = requests.get(info_url, headers=header)
    print(res.content.decode("utf-8"))
    # 获取个人所有仓库
    # print("开始获取个人所有仓库信息")
    # resp_url = f"https://api.github.com/users/{username}/repos"
    # all_resp = requests.get(resp_url, headers=header)
    # print(all_resp.content.decode("utf-8"))

def get_filesha(username):
    info_url = f"https://api.github.com/repos/{username}/Front-Study/contents/testapi"
    header = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36"
    }
    # 获取到个人信息
    res = requests.get(info_url, headers=header)
    res_list = json.loads(res.content.decode("utf-8"))
    file_name_list = [i['name'].split(".")[0].replace("test", "") for i in res_list]
    num_list = [int(n) for n in file_name_list if n]
    num_list.sort()
    print(num_list)
    return num_list[-1]+1

def use_token(username, token, filename):
    url1 = f"https://api.github.com/repos/{username}/Front-Study/contents/testapi/{filename}?access_token={token}"
    header = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36",
        # "Authorization": f"{token}",
    }
    data = {
        "message": "commit from INSOMNIA",
        "content": "bXkgbmV3IGZpbGUgY29udGVudHM="
    }
    put_cont = json.dumps(data)
    # 处理超时请求异常重新发送请求，最多3次
    i = 0
    while i < 3:
        try:
            res = requests.put(url1, headers=header, data=put_cont)
            # print(res.content.decode())
            print(f"文件{filename}创建成功----------->")
            return res
        except requests.exceptions.RequestException:
            i += 1

def del_file():
    url1 = f"https://api.github.com/repos/{username}/Front-Study/contents/testapi?access_token={token}"
    header = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36",
        # "Authorization": f"{token}",
    }
    data = {
        "message": "commit from INSOMNIA",
        "content": "bXkgbmV3IGZpbGUgY29udGVudHM="
    }

def more_put(username, token, n):
    x = 0
    dao_time = 0
    while True:
        if dao_time <= 0:
            x += 1
            print(f"开始第{x}天的请求------------>")
            time_n = [1, 2, 4, 5, 8, 10, 11, 12, 13, 18, 20, 21, 23, 26, 30, 37, 45, 55]
            put_count = random.choice(time_n)
            print(f"要发送的请求次数是{put_count}-------------->")
            lose_time = 0
            for i in range(put_count):
                filename = f"test{n}.html"
                print(f"开始发送第{i}次请求------------>")
                res = use_token(username, token, filename)
                n += 1
                # 执行随机延迟时间多少秒
                random_time = random.randint(1, 1000)
                print(f"执行睡眠时间{random_time}秒------------>")
                lose_time += random_time
                time.sleep(random_time)
            dao_time = 60*60*24 - lose_time
        print(f"开始执行第{x}天的睡眠----------->")
        dao_time -= 2
        time.sleep(2)
        print(f"还剩{dao_time}秒------------>")


if __name__ == '__main__':
    # github用户名和密码
    username = "Sjj1024"
    token = "8ba97ece7134a91d2f6065de9eee6b23d8a4cdee"
    # 获取个人信息
    # get_filesha(username)
    # 使用token
    # use_token(username, token)
    # 发送多次请求
    # 创建的文件序号，从0开始
    n = get_filesha(username)
    more_put(username, token, n)
