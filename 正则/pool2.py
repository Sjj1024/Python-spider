import os  # 导入的ｏｓ模块可以查看进程号
import time
import multiprocessing
import random


def test1(mag):
    print("%d进程开始启动，进程号是：%s" % (mag, os.getpid()))
    start_time = time.time()
    time.sleep(random.random()*2)  # 随机延迟一个时间
    end_time = time.time()
    all_time = end_time - start_time
    print("%d进程已经结束，耗时:%.2f" % (mag, all_time))


def main():
    # 建立一个进程池
    po = multiprocessing.Pool(3)

    # 向进程池里添加函数
    for i in range(10):
        po.apply_async(test1, args=(i,))

    # 开启进程，并等待进程池里进程运行完毕
    print("进程开始－－－－")
    po.close()  # 关闭进程池
    po.join()  # 等待进程池里的进程运行完毕
    print("进程运行完毕－－－－－")


if __name__ == '__main__':
    main()