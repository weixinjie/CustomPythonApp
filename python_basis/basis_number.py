# python基础-数据类型
a = 100
if (a > 0):
    print(a)
else:
    print(-a)

# python数据类型
# 字符串数据类型(\代表转义)
a = 'hi I\'m \"weixinjie\" \\'
print(a)

# 上述代码用\表示转义,可以使用r代表不转义
print(r"hi I\'m \"weixinjie\" \\")

# \n代表换行  '''...'''表示内部有多行输出
print('''weixinjie \n hehe \n hehe''')

# 布尔值注意大小写敏感应该是True False 可以使用 and or not来运算
testBoolean = True
testBoolean2 = False
print(testBoolean and testBoolean2)

# 常量，使用全部大写的名称来表示
PI = 3.141592654
print(PI)

# 运算 /是除法 //是地板除(向下取整)  %是取余数
testNum = 10
testNum2 = 3
print(testNum / testNum2, testNum % testNum2, testNum // testNum2)
