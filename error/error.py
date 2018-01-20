'测试error处理机制'
import logging

# 设置一个logging的输出级别
logging.basicConfig(level=logging.INFO)

try:
    r = 10 / 1
    print(r)
except Exception as e:
    print(e)
# 如果没有错误,那么会执行else语句并且执行finally语句
else:
    print("else语句")
finally:
    print("最终执行")

# 测试内置的logging模块
try:
    r = 10 / 0
except Exception as e:
    logging.exception(e)
print('我又执行了')


def foo(s):
    if not isinstance(s, str):
        raise Exception('不是str类型的串')
    print(s)


try:
    foo('weixinjie')
except Exception as e:
    logging.error(e)


# 将一个异常捕获出来变成另外一个异常抛出
def foo2():
    try:
        r = 10 / 0
    except ZeroDivisionError as e:
        raise ValueError("我是自定义的错误类型")


print(foo2())
