# 高阶函数

# 函数调用
from functools import reduce

print(abs(-1))

# 变量可以指向函数的结果
x = abs(-10)
print(x)

# 直接输出abs是指的函数本身 注意函数名
print(abs)

# 直接使用变量来指向函数
f = abs
print(f(-100))


# 函数的参数可以是函数所以可以称之为高阶函数
def doublef(x, y, f):
    return f(x) + f(y)


print(doublef(-1, -1, abs))


# 高阶函数之map:map接收两个参数一个是函数一个是iterator
def double(x):
    return x * x


testR = map(double, [1, 2, 3])
print(list(testR))

testList = map(str, range(10))
print(list(testList))


# 高阶函数之reduce:reduce将返回的结果与下一个参数做累加运算
def double2(x, y):
    return x + y


testReduce = reduce(double2, [1, 2, 3])
print(testReduce)

# 使用filter进行过滤序列,filter会根据函数的true或者false来决定是否保留序列中的元素
testList2 = list(range(10))


def functionFilter(x):
    return x % 2 == 0


# 注意使用filter计算的数据是一个iterator也就是一个惰性的数据，可以使用next或者使用list函数强制转成list
print(list(filter(functionFilter, testList2)))

# 使用sorted函数对list进行排序 key接收一个函数名,reverse代表是否将顺序反过来
testList3 = [1, 4, 2, 3, 6, -100]
print(sorted(testList3, key=abs, reverse=True))

