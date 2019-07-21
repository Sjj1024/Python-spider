"""
进程：没有运行起来叫程序，运行起来就叫进程
每一个进程单独占用一块内存空间，所以全局变量不共享

"""
import multiprocessing
import time
import os


num = 0


def test1():
    num1 = 0
    global num
    for i in range(5):
        num1 += 1
        print(num1)
        num += 1
        print(num)


def test2():
    num1 = 0
    global num
    for i in range(5):
        num1 += 1
        num += 1
        print(num1)
        print(num)
        print(os.getpid())


def main():
    p1 = multiprocessing.Process(target=test1, args=())
    p2 = multiprocessing.Process(target=test2)
    p1.start()
    time.sleep(1)
    p2.start()
    time.sleep(1)
    print(num)



if __name__ == '__main__':
    main()