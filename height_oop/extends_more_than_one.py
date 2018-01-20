# 多重继承

class Run:
    def run(self):
        print('我可以奔跑')


class Fly:
    def fly(self):
        print("我可以飞")


class Zhangrui(Run, Fly):
    pass


z = Zhangrui()
z.run()
z.fly()
