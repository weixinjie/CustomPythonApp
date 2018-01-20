# 类和实例
class Student(object):
    # 定义类的时候会首先执行这个方法
    def __init__(self, name, score, sex):
        self.name = name
        self.score = score
        self.sex = sex

    def print_message(self):
        print(self.name)
        print(self.score)
        print(self.sex)


s = Student('weixinjie', 100, 'man')
s.print_message()


# 如果我们希望隐藏类内部细节,可以通过将自己的参数添加__来表示
class Student2(object):
    # 定义类的时候会首先执行这个方法
    def __init__(self, name, score, sex):
        self.__name = name
        self.__score = score
        self.__sex = sex

    def print_message(self):
        print(self.__name)
        print(self.__score)
        print(self.__sex)


# 此时不可以通过实例.属性来获取了
s2 = Student2('weixinjie', 111, 'women')
s2.print_message()

# 错误写法 直接通过s2.__来访问私有变量是错误的,此时python解释器会自动添加一个__name新的属性
s2.__name = 'zhangrui'
s2.print_message()
