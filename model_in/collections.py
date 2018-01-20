# 使用namedtuple来定义一个变量的集合(比如使用圆点与半径，或者是使用x y来表示第一个点)
from collections import namedtuple, deque, defaultdict, OrderedDict, Counter

Point = namedtuple('Point', ['x', 'y', 'z'])

point = Point(1, 2, 3)
print(point.x, point.y)

# 使用deque来实现双向队列(append appendleft pop popleft)
q = deque(['a', 'b', 'c'])
q.append('x')
q.appendleft('张睿是老大')
print(q)

q.pop()
q.popleft()
print(q)

# defaultdict 使用dirt的时候如果引用的key不存在会抛出KeyError错误 使用defaultidict的时候可以传入一个默认的构造函数
dd = defaultdict(lambda: '我是默认值')
dd['key1'] = '测试1'
print(dd['key1'])
print(dd['k'])

# 使用OrderedDict来对dict进行排序,此时排序是基于插入的顺序的
od = OrderedDict()
od['z'] = 1
od['a'] = 2
od['y'] = 3
print(list(od.keys()))


# 使用OrderedDict可以实现一个fifo(先进先出)的dict(队列)
class LastUpdatedOrderdDict(OrderedDict):
    def __init__(self, size):
        super(LastUpdatedOrderdDict, self).__init__()
        self._size = size

    def __setitem__(self, key, value):
        if (len(self) > self._size):
            last = self.popitem(last=True)
            print('remove', last)
        OrderedDict.__setitem__(self, key, value)


latest = LastUpdatedOrderdDict(2)
latest['z'] = 1
latest['a'] = 2
latest['y'] = 3
latest['d'] = 4
print(list(latest.keys()))

# Counter
c = Counter()
for ch in 'zhangruiweixinjie':
    c[ch] = c[ch] + 1
print(c)
