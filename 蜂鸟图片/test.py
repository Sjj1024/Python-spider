import requests
import re
import time

def daoji():
    dao_time = 0
    while True:
        if dao_time == 0:
            print("开始执行发送请求")
            dao_time = 60*60*24
        dao_time = dao_time - 2
        time.sleep(1)
        print(f"开始倒计时{dao_time}")


if __name__ == '__main__':
    daoji()