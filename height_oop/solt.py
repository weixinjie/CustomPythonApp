# !/usr/bin/env python3
# -*- coding: utf-8 -*-

'使用solt来限制类所能绑定的属性'


class Student(object):
    __slots__ = ('name', 'age')  # 用tuple定义允许绑定的属性名称
    pass


s = Student()
# 可以动态绑定属性
s.name = 'weixinjie'
s.age = 100
print(s.age)

# 使用solt方法来限制可以动态绑定的属性
s = Student()
# s.sex = 'nan' 由于sex不在slots中这句代码会报错


