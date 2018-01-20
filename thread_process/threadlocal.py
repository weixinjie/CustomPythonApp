# 使用threadlocal 使得每个线程都有自己的数据备份

'测试使用thread_local'
import threading

custom_local = threading.local()


class Student(object):
    def __init__(self, name):
        self._name = name


def getFromThreadLocal():
    name = custom_local.student._name
    print(name, threading.current_thread().name)


def putThreadLocal(name):
    custom_local.student = Student(name)
    getFromThreadLocal()


# 传参的时候使用tuple的时候如果只有一个参数则需要这么写('ssss',)加一个,
t1 = threading.Thread(target=putThreadLocal, args=('thread_1_测试',), name='thread-1')
t2 = threading.Thread(target=putThreadLocal, args=('thread_2 测试',), name='thread-2')
t1.start()
t2.start()
t1.join()
t2.join()
print('执行完了我擦')
