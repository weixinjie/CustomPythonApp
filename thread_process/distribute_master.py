import queue

import random
from multiprocessing.managers import BaseManager

task_queue = queue.Queue()

task_result = queue.Queue()


class QueueManager(BaseManager):
    pass


# 注册发送任务的队列
QueueManager.register('get_task_queue', callable=lambda: task_queue)
# 注册接收任务的队列
QueueManager.register('get_task_result', callable=lambda: task_result)
manager = QueueManager(address=('', 5000), authkey=b'abc')
# 启动队列
manager.start()

# 获取通过网络获取的任务
task = manager.get_task_queue()
result_task = manager.get_task_result()

# 放几个任务进去
for i in range(1000000):
    n = random.randint(0, 10000)
    task.put(n)
    print('我放了一个任务  %s' % (n,))

while (True):
    r = result_task.get(10)
    print('我从结果队列中取出任务了', r)

