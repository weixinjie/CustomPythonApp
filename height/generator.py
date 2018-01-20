# 测试生成器

# 生成器跟列表生成器只有外层的符号不一样 需要将[]改成()
L = [x * x for x in range(10)]
print(L)

# 我们是不可以直接打印G的值的
G = (x * x for x in range(10))
print(G)
# 如果需要打印G的值，则需要使用next方法
print(next(G))
print(next(G))


# 可以使用for循环来迭代generator
def aaa():
    for a in G:
        print(a)


aaa()


# 可以使用yield来定义一个生成器函数(generator), 普通函数是顺序执行 generator函数是调用next的时候执行并且从上次yield的地方开始执行
def generatorTest():
    print('我是generatorTest 我他么在输出1')
    yield
    print('我是generatorTest 我他么在输出2')
    yield
    print('我是generatorTest 我他么在输出3')
    yield


gen = generatorTest()

while (True):
    try:
        print(next(gen))
    except StopIteration as e:
        print(e.value)
        break
