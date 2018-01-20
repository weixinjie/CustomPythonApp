# !/usr/bin/env python3
# -*- coding: utf-8 -*-

'测试从类中获取信息'
import types

__author__ = 'weixinjie'

print(type('123'))
print(type(1111))


def testFunction():
    pass


# 判断一个对象是否是函数类型
print(type(testFunction) == types.FunctionType)

# 使用instance来判断是否是列表中的其中一个类型
print(isinstance(['wei', 'xin', 'jie'], (list, dict, tuple)))

# 使用dir函数获取一个对象所有属性与方法
print(dir('abc'))

# 判断一个字符串是否有__add__属性
b = hasattr('abc', '__add__')
print(b)

# 通过setattr 与 getattr来操作一个对象的属性
s = testFunction
setattr(s, '__doc__', '测试添加属性')
print(getattr(s, '__doc__'))
