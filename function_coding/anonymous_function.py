# 匿名函数

# 必须使用lambda来表示匿名函数 :前面代表参数
mapTest = map(lambda x: x * x, [1, 2, 3])
print(list(mapTest))

# 将匿名函数赋值给一个变量
f = lambda x: x + x
print(f(5))


# 可以将匿名函数进行返回
def functionTest():
    return lambda x: x - 1


# 可以将匿名函数进行返回
f2 = functionTest()
print(f2(100))
