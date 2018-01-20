'很多时候数据读写不一定是文件还有可能是内存读写'
from io import StringIO, BytesIO

f = StringIO()
i = 0
while (True):
    i = i + 1
    if (i < 100):
        f.write('weixinjie%d' % i)
    else:
        break

print(f.getvalue())

f = StringIO('hello \n hi \n goodbay')
print(f.readline())

# 使用byteio
f = BytesIO()
f.write('中文'.encode('utf-8'))
print(f.getvalue())
