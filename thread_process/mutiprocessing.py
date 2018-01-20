# 使用mutiprocessing来创建多进程
import logging
import random

from multiprocessing import Process, Queue

import time
from multiprocessing.pool import Pool

import subprocess


def testFunction(name):
    print('我的进程是%s' % os.getpid())


if __name__ == 'sss__main__sss':
    print('父进程是%s' % os.getpid())
    p = Process(target=testFunction, args=('我是子进程的名字',))
    print('子进程要启动了')
    p.start()
    # join函数可以将该子进程插入到当前进程中执行,这个进程执行完毕后才会执行下面的方法
    p.join()
    print('子进程结束了%s' % os.getpid())


# 进程池

def long_time_task(name):
    print('我是子进程 %s (%s)...' % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('子进程 %s 运行了 %0.2f 秒.' % (name, (end - start)))


if __name__ == 'sss__main__sss':
    print("父进程启动了。。。%s" % (os.getpid()))
    p = Pool(1000)
    for i in range(50000000):
        p.apply_async(long_time_task, args=(i,))
    p.close()
    p.join()

# 使用subprocess模块来控制子进程的输入跟输出
r = subprocess.call(['nslookup', 'www.python.org'])
print(r)

print('$ nslookup')
p = subprocess.Popen(['nslookup'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
output, err = p.communicate(b'set q=mx\npython.org\nexit\n')
print(output.decode('utf-8'))
print('Exit code:', p.returncode)


# 进程之间的通信

# 可以使用mutiprocessing模块来保证进程之间的通信机制 可以使用Queue Pipes来保证通信 下面演示queue通信机制

# 写入的方法
def write(q):
    for c in range(500):
        q.put(c)
        sleepTime = random.random()
        print('我是写入的方法,我将%s写进去了，我要睡%s秒' % (c, sleepTime))
        time.sleep(sleepTime * 10)


def read(q):
    while (True):
        value = q.get(True)
        print('我是取出的方法,我将%s取出来了' % (value,))


if (__name__ == '__main__'):
    q = Queue()
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))
    pw.start()
    pr.start()
