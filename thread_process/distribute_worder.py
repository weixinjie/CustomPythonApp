# 分布式之work进程
from multiprocessing.managers import BaseManager


class QueueManager(BaseManager):
    pass


# 由于这个Queue要从网络上获取名字,所以要进行注册
QueueManager.register('get_task_queue')
QueueManager.register('get_task_result')
server_addr = '127.0.0.1'
print('我正在连接到服务端  ', server_addr)
manager = QueueManager(address=(server_addr, 5000), authkey=b'abc')
manager.connect()

task = manager.get_task_queue()
result = manager.get_task_result()

for i in range(1000000):
    try:
        n = task.get(timeout=1)
        result.put(n)
        print('我是工作进程,我将%s放进来了' % (n,))
    except Exception as e:
        print(e)
