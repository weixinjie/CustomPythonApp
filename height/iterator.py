# 测试迭代器

#  使用迭代器来迭代dirt
from collections import Iterable

testDir = {'a': 1, 'b': 3, 'c': 'zhangrui'}
# 迭代key
for key in testDir.keys():
    print(key)
# 迭代value
for value in testDir.values():
    print(value)

# 迭代item
for key, value in testDir.items():
    print(key, ":", value)

# 迭代字符串
for char in 'weixinjie':
    print(char)

# 判断此对象是否是可迭代的
bool = isinstance(testDir, Iterable)
print(bool)

# 使用enumerat使得迭代变成下标的类型
for i, value in enumerate(testDir):
    print('当前索引', i, "当前数据", value)

# 在for循环中同时引用两个变量
for x, y in [(1, 1), (2, 2), (3, 3)]:
    print(x, y)
