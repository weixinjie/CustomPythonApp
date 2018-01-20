# 函数作为返回值

def lazy_sum(*args):
    def sum(*args):
        sumTotal = 0
        for arg in args:
            sumTotal = sumTotal + arg
        return sumTotal

    return sum


print(lazy_sum([1, 2, 3]))

# 每次调用lazy_sum时都会返回一个新的函数，相互调用不会影响应为是两个变量
f = lazy_sum()
f_2 = lazy_sum()
print(f == f_2)


########闭包 返回闭包时牢记一点：返回函数不要引用任何循环变量，或者后续会发生变化的变量。
