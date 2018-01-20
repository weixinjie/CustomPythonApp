# list与tuple

# ----------------list测试
testList = ['韦新杰', "张睿", "小朋友"]
print(testList)

# 使用len函数进行测量数组
print(len(testList))

# 根据下标引用数组类型
print(testList[0], testList[1], testList[2])

# 引用数组最后一个元素
print(testList[len(testList) - 1])
# 使用-1下标直接引用最后一个元素
print(testList[-1])
print(testList[-2])

# list是一个可变的列表
testList.append("我是新加入的数据")
print(testList[-1])
# insert到指定的位置
testList.insert(0, "我是第一个数据")
print(testList)
# 使用pop将list的元素进行剔除 默认是剔除最后一个，当然也可以指定index
testList.pop()
print(testList)
testList.pop(1)
print(testList)

# 根据下标可以直接替换list元素,替换的数据类型可以是不一样的数据类型
testList[0] = 123
print(testList)
# 替换的数据也可以是一个list
testList2 = [123, "weixinjie"]
testList[0] = testList2
print(testList)

# ----------------tuple测试

# tuple数据一旦初始化就不能改变了
testTuple = ("weixinjie", 123, b'wei')
print(testTuple)

# 定义一个空的tuple
testTuple = ()
print(testTuple)


