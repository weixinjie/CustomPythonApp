# 测试切片
testList = ['weixinjie', 'zhangrui', 123, 'hahhah']

# 使用切片写法取前三个
print(testList[0:2])
# 如果起始位置是0则可以省略
print(testList[:2])
# 同样支持倒数切片
print(testList[-2:-1])

testList2 = list(range(100))
print(testList2[0:10])
print(testList2[-10:])

# 11 到 20的数字
print(testList2[10:20])

# 前10个数 每两个截取一个
print(testList2[0:10:2])

# 所有数 每5个截取一个
print(testList2[::5])

# 什么都不写可以原样复制一个list
print(testList2[:])

# --------tuple也是一种list,同样可以使用切片
testTuple = ('zhangrui', 'weixinjie', 11111, 22222, 33333)
# 每隔2个输出一个
print(testTuple[0:len(testTuple):2])
print(testTuple[::2])

# String也可以使用切片来操作
testStr = 'abcdefghijklmn'
print(testStr[0:len(testStr):2])


# 自定义Trim操作来分离字符串,删除首尾的空格(注意不能删除中间的空格)
def trim(s):
    # 先删除前面的空格
    testStr = []
    first_index = 0
    latest_index = len(s)

    index = 0
    while (index < len(s)):
        if (s[index] != ' '):
            first_index = index
            break
        index = index + 1
    if (index == len(s)):
        return ''

    index = len(s) - 1
    while (index > 0):
        if (s[index] != ' '):
            latest_index = index
            break
        index = index - 1

    index = first_index
    while (index <= latest_index):
        testStr.append(s[index])
        index = index + 1

    return ''.join(testStr)


# 测试:
if trim('hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello') != 'hello':
    print('测试失败!')
elif trim('  hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败!')
elif trim('') != '':
    print('测试失败!')
elif trim('    ') != '':
    print('测试失败!')
else:
    print('测试成功!')
