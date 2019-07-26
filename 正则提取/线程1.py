#　多线程
import threading
import time


num1 = 0



def test1():
    global num1
    time.sleep(2)
    for i in range(5):
        num1 += 1
    print(num1)


def test2():
    global num1
    for i in range(5):
        num1 += 1
    print(num1)


def main():
    t1 = threading.Thread(target=test1)
    t2 = threading.Thread(target=test2)
    # 设置t1为守护线程，主进程一结束，子进程就结束。不然的话，主进程会等待子进程结束后再结束。
    t1.setDaemon(True)
    t1.start()
    t2.start()
    time.sleep(1)
    print(num1)




if __name__ == '__main__':
    main()
