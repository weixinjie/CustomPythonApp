# 测试异步
import asyncio


@asyncio.coroutine
def hello(name):
    print('hello ', name)
    # 这句代码指的是异步调用
    yield from asyncio.sleep(1)
    print('我又说hello了', name)


if (__name__ == '__main'):
    loop = asyncio.get_event_loop()
    loop.run_until_complete(hello('weixinjie'))
    loop.close()


# 并发请求多个网页的数据 使用yield from语句代表先执行到这里，弄好了在调用
@asyncio.coroutine
def wget(host):
    print('wget %s...' % host)
    connect = asyncio.open_connection(host, 80)
    reader, writer = yield from connect
    header = 'GET / HTTP/1.0\r\nHost: %s\r\n\r\n' % host
    writer.write(header.encode('utf-8'))
    yield from writer.drain()
    while True:
        line = yield from reader.readline()
        if line == b'\r\n':
            break
        print('%s header > %s' % (host, line.decode('utf-8').rstrip()))
    # Ignore the body, close the socket
    writer.close()


# 使用task进行并发请求
loop = asyncio.get_event_loop()
tasks = [wget(host) for host in ['www.sina.com.cn', 'www.sohu.com', 'www.163.com']]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()


# python3.5以后引入了新的语法 async/await 使用async代表asyncio.coroutine使用awit代替yield from
