# 测试列表生成式

# 使用list_range来创建列表
import os

testList = list(range(1, 10))
print(testList)

# 开始使用列表生成式
testList2 = [x * x for x in range(1, 10)]
print(testList2)

# 基于列表生成式的条件筛选
testList3 = [x * x for x in range(0, 10) if x % 2 == 0]
print(testList3)

# 使用两层循环
testList4 = [m + n for m in 'ABC' for n in 'XYZ']
print(testList4)

# 使用列表生成式列出当前所有文件与目录
testList5 = [d for d in os.listdir('.')]
print(testList5)

# 使用列表生成式子同时循环两个变量
d = {'x': 'A', 'y': 'B', 'z': 'C'}
testList6 = [key + '' + value for key, value in d.items()]
print(testList6)

# 将列表所有的大写改成小写
testList7 = ['HELLO', 'WORD']
testList8 = [s.lower() for s in testList7]
print(testList8)
