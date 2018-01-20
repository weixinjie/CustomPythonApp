# 测试循环

# 可以从list或者tuple中进行迭代
testList = ["weixinjie", "zhangrui", 13123]
for test in testList:
    print(test)
testTuple = ("weixinjie", "zhangrui", 12333)
for test in testTuple:
    print(test)

# 使用range函数+list函数可以生成一个list
testList = range(10)
print(list(testList))

# 计算一个和
sum = 0
for sum_index in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    sum += sum_index
print(sum)

# 计算一个和(另一个算法)
sum = 0
for sum_index in range(5):
    sum += sum_index
print("使用range函数", sum)

# 使用while来循环
testStr = "weixinjie"
n = 5
while (n > 0):
    n = n - 1
    print(testStr)

# 使用break提前结束
n = 1
while (n < 100):
    if (n > 10):
        break
    n = n + 1
    print(n)

# 使用continue继续循环
n = 10
while (n < 100):
    n = n + 1
    if (n % 2 == 0):
        continue
    print(n)
