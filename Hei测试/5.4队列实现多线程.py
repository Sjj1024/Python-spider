# 队列的导入
from queue import Queue
import threading

# 建立一个队列对象
q1 = Queue()
for x in range(10):
    # 循环将数据放到队列中，
    q1.put(x)

# 定义一个循环获取队列中数据的方法
def get_info():
    while True:
        one1 = q1.get()
        print(one1)
        # 执行队列的task_done，告诉队列取一个之后就减一，put会让队列加一
        # q1.task_done()


# 设置一个线程
t1 = threading.Thread(target=get_info)
# 将线程设置为守护线程，主进程一结束，子线程就结束，说明这个线程是不重要的
t1.setDaemon(True)
# 线程开始
t1.start()
# 让主线程阻塞，队列阻塞，等待子线程结束，队列执行完了，则说明线程也执行完了，
q1.join()


# 一个函数运行起来是一个线程？
# 一个死循环运行起来是一个线程？
# 一个队列运行起来是一个线程?

