# 测试序列化
import json

# 使用json模块进行序列化
d = {'key1': "value1", 'key2': 'value2'}
print(json.dumps(d))


class Student(object):
    def __init__(self, name, age):
        self._name = name
        self._age = age


s = Student('weixinjie', 100)
# 每个实例都有一个__dict__属性来存储实例的变量
jsonStr = json.dumps(s, default=lambda obj: obj.__dict__)
print(jsonStr)


# 反序列化
def toStudent(d):
    return Student(d['_name'], d['_age'])


print(json.loads(jsonStr, object_hook=toStudent))
