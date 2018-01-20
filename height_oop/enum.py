# !/usr/bin/env python3
# -*- coding: utf-8 -*-

'测试枚举类'
from enum import Enum, unique

Month = Enum('Mon', ('jan', 'fab', 'mar', 'oper', 'mey'))
print(Month.fab)

# value是枚举类型自动赋值的从1开始
for name, member in Month.__members__.items():
    print(name, member, member.value)


# 如果想自己控制枚举类型 @unique装饰器可以帮助我们检查保证没有重复值。
@unique
class MEnum(Enum):
    a = 11111
    b = 22222
    c = 33333


# 获取枚举值的集中方式
print(MEnum.a.value)
print(MEnum['a'].value)
