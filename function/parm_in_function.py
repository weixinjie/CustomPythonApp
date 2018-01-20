# 函数的参数

# 定义一个平方函数,默认n等于2
def power(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s


# 可以重新指定n的值为3
print(power(5, 3))


# 定义一个函数，可以使用默认参数
def student(age, score, home='jinan', love='book'):
    print(age, score, home, love)


# 传递参数的时候可以省略默认参数
student(10, 200)
# 传递参数的时候可以指定某个默认参数名称
student(10, 200, love='zhangrui')


# 使用默认参数的时候也是有坑的
def add_end(L=[]):
    L.append("END")
    return L


# 由于L是可变的,连续多次输出的时候会记住这些数据
print(add_end())
print(add_end())


# 使用None这些不可变的数据就不会记住
def add_end_success(L=None):
    if (L is None):
        L = []
    L.append("end")
    return L


print(add_end_success())
print(add_end_success())


# 使用*使得参数变成可变参数
def sumTest(*param):
    sum = 0
    for pa in param:
        sum = sum + pa
    return sum


print(sumTest(0))
print(sumTest(1, 2, 3))


# python允许传入参数的时候加入*来讲list或者tuple作为可变参数传入进去
def testChangeFunction(*param):
    for a in param:
        print(a)


testList = ['weixinjie', 1111]
testTuple = ('weixinjie', 222)
testChangeFunction(*testList)
testChangeFunction(*testTuple)


# 允许使用**来表示关键字参数,内部自动组装成一个dict
def testKeyWord(name, age, **kw):
    print(name, age, 'other', kw)


testKeyWord('name', 111, city='beijing', home='shandong')


# 检查关键字参数
def testkeyWord2(name, age, **kw):
    if ('city' in kw):
        print("city is in")
        pass
    if ('user' in kw):
        print("user is in")
        pass

    print(name, age)


testkeyWord2('weixinjie', 11111, city='shandong')


# 如果想限制关键字参数的名称 则使用*来做区分 *后面的参数在传递的时候一定要传入
def testKeyWord3(name, age, *, city, zipcode):
    print(name, age, city, zipcode)


testKeyWord3('weixinjie', 23, city='beijing', zipcode=10000)


# 如果参数列表中有可变参数了,则后面的关键字参数就不需要*来做区分了
def testKeyWord4(name, age, *args, city, zipcode):
    print(name, age, args, city, zipcode)


testKeyWord4('weixinjie', 23, city='beijing', zipcode=10000)


# *代表可变参数,**代表关键字参数
def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)


f1(1, 2, 3, 'a', 'b', x=99)
