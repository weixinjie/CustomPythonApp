# 测试定义函数

# 定义函数
def myAbs(x):
    # 我们可以对输入的数据进行类型检查
    if (not isinstance(x, (int, float))):
        raise TypeError("傻逼 输入的类型有错误")
    if (x > 0):
        return x
    else:
        return -x


print(myAbs(1111))


# 定义一个空函数
def pop(a):
    pass


# 函数返回多个值(其实返回的是一个tuple)
def functionTest():
    return 1, 2


x, y = functionTest()
print(x, y)
