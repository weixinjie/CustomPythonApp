# 测试装饰器
import functools
import time


# 每个函数都一个name属性
def now():
    return time.time()


f = now
# 注意 f代表函数的引用  f()代表执行函数
print(f())
print(f.__name__)
print(now.__name__)


# 开始制作一个装饰器
def log(function):
    def wrapper(*args, **kw):
        print('function-', function.__name__)
        return function(*args, **kw)

    return wrapper


@log
def now2():
    return time.process_time()


print(now2())


# 制作一个带参数的装饰器
def logger(test):
    def decorator(function):
        # 需要使用wrap函数更改函数签名
        @functools.wraps(function)
        def wrapper(*args, **kwargs):
            print(test)
            return function(*args, **kwargs)

        return wrapper

    return decorator


@logger('weixinjie正在输出')
def now3():
    return time.process_time()


print(now3(), now3.__name__)


# 偏函数
def integer(str, base):
    return int(str, base)


# 可以使用functiontools中的partial方法自己定义一个base为固定值的偏函数
f2 = functools.partial(integer, base=8)
print(f2('100'))
