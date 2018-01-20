# 用itertools来操作迭代的对象
import itertools

# 无线循环的迭代器
from contextlib import contextmanager, closing
from urllib.request import urlopen

natuals = itertools.count(1)
if (__name__ == '__main_'):
    for n in natuals:
        print(n)

# cycle会把传入的序列进行无限循环
natuals_str = itertools.cycle('wei')
if (__name__ == '__main_'):
    for n in natuals_str:
        print(n)

# 使用repeat负责把一个元素循环多少遍
ns = itertools.repeat('wei', 3)
for n in ns:
    print(n)

# 使用chain把对象串联起来
testChain = itertools.chain('abc', 'de')
for n in testChain:
    print(n)

# groupby把相邻的元素放到一起
for key, group in itertools.groupby('AABCBCCDDEEFF'):
    print(key, list(group))


# 高级with使用,只要是实现了__enter__跟__exit__的语句都可以使用with
class CustomQueue(object):
    def __init__(self, name):
        self.name = name

    def __enter__(self):
        print('正在执行enter语句')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            print('发生了错误')
        else:
            print('正确的执行了')

    def query(self):
        print('我正在使用 %s 的名字' % self.name)


with CustomQueue('韦新杰大帅哥') as q:
    q.query()


# 使用contentmanager来操作
class CustomQueue2(object):
    def __init__(self):
        print('初始化了')

    def query(self):
        print('调用了query函数')


@contextmanager
def create_query():
    print('begin')
    q = CustomQueue2()
    yield q
    print('end')


with create_query() as c:
    c.query()

# 如果对象没有实现上下文 可以使用@close来实现
with closing(urlopen('https://www.python.org')) as page:
    for line in page:
        print(line)
