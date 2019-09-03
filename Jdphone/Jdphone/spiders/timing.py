import os
import time

if __name__ == '__main__':
    # os.system('pwd')
    while True:
        os.system("scrapy crawl jdphone")
        # 每２个小时执行一次　６０＊６０＊２
        time.sleep(7200)