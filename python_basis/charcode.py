#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 字符串的字符集
a = "包含中文的str"
print(a)

# 提供了ord获取char的整数 chr函数将整数转化成编码
print(ord('A'))
print(chr(66))
# 下面是16进制的编码
print("\u4e2d\u6587")

# byte的数据类型 用b+''或者b+""来表示
testStr = b'abc'
testStr2 = 'abc'
print(testStr, testStr2)

# str通过encode可以转化成指定格式的byte  byte可以decode成对应的str
print('韦新杰'.encode('utf-8'))
testByte = b'\xe9\x9f\xa6\xe6\x96\xb0\xe6\x9d\xb0'
print(testByte.decode('utf-8'))

# 如果decode的时候包含无用的字节，则采用errors= ignore来忽略
print(b'\xe4\xb8\xad\xff'.decode('utf-8', errors='ignore'))

# 通过len函数可以判断str有多少字符
testStr3 = "韦新杰aaabbb"
print(len(testStr3))
# 如果换成bytes则len函数表示有多少字节(先转化在计算)
testByte2 = "韦新杰love张睿"
print(len(testByte2.encode('utf-8')))

# 采用%进行格式化输出字符串(%表示占位)
testStr4 = "hello word %s" % "韦新杰"
print(testStr4)
# 采用格式化输出的时候:%d-整数; %f-浮点数; %s-字符串; %x-十六进制整数
testStr5 = "hello word %s %d %f " % ("韦新杰", 15, 15.0)
print(testStr5)
# 用%%来进行转义
testStr6 = 'hello word %s %%' % ("张睿")
print(testStr6)

# 采用format进行格式化输出
testStr7 = "你好呀 {0} 你的成绩提高了{1}%".format('小明', 17.34)
print(testStr7)
