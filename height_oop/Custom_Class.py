# 定制类

class Student(object):
    # 使用slots可以限制当前类的属性
    # __slots__ = ('zhangrui', 'hehe', 'name')

    def __init__(self, na=''):
        self.name = na

    # 重写__str__函数,输出的时候可以定制化输出
    def __str__(self):
        return self.name

    # repr函数跟str函数是差不多,不过repo函数是给程序看的
    __repr__ = __str__

    def __getattr__(self, na):
        return Student(self.name + '/' + na)


print(Student('weixinjie'))
print(Student().username.getimage.hahaha)


# __call__方法,可以通过实例直接调用
class TestClass(object):
    def __init__(self):
        print('我已经初始化了')

    def __call__(self, *args, **kwargs):
        print(args, kwargs)


t = TestClass()
print(t('weixinjie', 123123123, {'aaa': 123, 'bbb': 321}))
