# dis 与 set

# 测试dis
disTest = {'weixinjie': 100, "laoma": 100, "zhangrui": 100}
print(disTest)
# 获取value可以通过key的方式获得,如果获取一个不存在的key则会报错
print(disTest['weixinjie'])

# dis的数据可以通过动态添加进去
disTest['新加入的数据'] = "我是新加入的数据"
print(disTest)

# 多次采用同样的key来添加，后加入的value会冲掉前一个value
disTest['新加入的数据'] = "weixinjie"
print(disTest)

# 要避免不存在key的情况出现,采用in关键字来判断
if ('weixinjie' in disTest):
    print("weixinjie在dis里面")

# 采用dis的get方法来获取数据,可以自己设置默认值
print(disTest.get('weixinjie', '此key不存在'))

# 如果删除一个key则可以采用pop(key)的方法
disTest.pop("weixinjie")
print(disTest)

# 开始测试set

# 创建一个set,需要输入一个list
testSet = set(['我是测试set1', '我是测试set2', '我是测试set3', '我是测试set4'])
print(testSet)

# 重复添加的数据会被自动过滤
testSet.add('我是测试set1')
print(testSet)

# 通过remove方法删除数据
testSet.remove('我是测试set1')
print(testSet)

# 两个set可以做交集 并集等操作
testSet1 = set([1, 2, 3])
testSet2 = set([2, 3, 4])
print(testSet1 & testSet2)
print(testSet1 | testSet2)
