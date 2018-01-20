# 使用模块

# !/usr/bin/env python3
# -*- coding: utf-8 -*-

# 任何模块的第一个字符串都会被当做模块的注释
'测试使用模块'
import sys

__author__ = 'weixinjie'


def test():
    args = sys.argv
    return args


# 当单独运行这个模块的时候python解释器会把__name__这个变量变成__main__ 最常见的就是运行测试(别的模块运行此模块判断就为false了)
if (__name__ == '__main__'):
    print(test())


# 当希望使用private时需要使用 _来做区别(当然这只是一个区分外部也是可以直接引用的)
def publicTest():
    _private_1()
    _private_2()


def _private_1():
    print(1)


def _private_2():
    print(2)
