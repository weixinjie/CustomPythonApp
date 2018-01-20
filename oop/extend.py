# !/usr/bin/env python3
# -*- coding: utf-8 -*-

'测试继承与多态'

__author__ = 'weixinjie'


class Animal(object):
    def run(self):
        print("animal is run")


class Dog(Animal):
    def run(self):
        print("dog is run")

    def eat(self):
        print('dog is eating')


class Zhangrui(Animal):
    pass


dog = Dog()
dog.run()

zhangrui = Zhangrui()
zhangrui.run()

# 使用 isinstance来判断是否是一个类的子类
print(isinstance(dog, Animal))
