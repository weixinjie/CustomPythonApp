'使用元类'


# 使用type来创建一个函数
def hello(self):
    print('hello word')


Hello = type('Hello', (object,), dict(fn=hello))
h = Hello()
h.fn()
