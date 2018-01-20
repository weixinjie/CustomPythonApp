# !/usr/bin/env python3
# -*- coding: utf-8 -*-

'实例属性与类属性'


class Persion():
    # 通过构造方法可以构建一个实例属性
    def __init__(self, name):
        self.name = name

    # 可以直接构建一个类属性
    sex = "nan"


p = Persion('weixinjie')
print(p.name)
# 实例属性可以直接访问类属性
print(p.sex)
# 类属性可以直接通过类来表示
print(Persion.sex)
