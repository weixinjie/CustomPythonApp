# !/usr/bin/env python3
# -*- coding: utf-8 -*-

'测试使用property将方法变成属性调用'


#
class Student(object):
    @property
    def score(self):
        return self._score

    # 定义了上述的属性之后会自动生成这个setter的装饰器
    @score.setter
    def score(self, score):
        if (isinstance(score, int)):
            self._score = score
        else:
            self._score = 0
            print('傻逼 输入的参数不对')

    # 只使用propery来定义的话这个属性是一个可读属性
    @property
    def age(self):
        return 2015


s = Student()
s.score = ''
print(s.score)
print(s.age)
