# 测试递归函数

def recursionFunc(n):
    if (n == 0):
        return 1
    return n * recursionFunc(n - 1)


print(recursionFunc(3))
