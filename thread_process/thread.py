# 测试多线程

# 启动一个线程只需要将函数传递进去就行了
import threading

import time


def testFunctin():
    print("当前的线程名称为 ", threading.current_thread().getName())
    i = 0
    while (i < 5):
        print('我是线程 %s 我正在执行 %s' % (threading.current_thread().getName(), i))
        i = i + 1


testFunctin()
t = threading.Thread(target=testFunctin, name='子线程1')
t.start()
t.join()

# 线程锁
# 假定这是你的银行存款:
count = 0
lock = threading.Lock()


def change(n):
    global count
    count = count + n
    count = count - n


def runInThread(n):
    for i in range(100000):
        lock.acquire()
        try:
            change(n)
        finally:
            lock.release()


t1 = threading.Thread(target=runInThread, name='t1', args=(5,))
t2 = threading.Thread(target=runInThread, name='t2', args=(19,))
t1.start()
t2.start()
t1.join()
t2.join()
print('------当前的余额 ', count)
