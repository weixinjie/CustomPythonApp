# 测试md5
import hashlib

md5 = hashlib.md5()
md5.update('weixinjie hahah love zhangrui'.encode('utf-8'))
print(md5.hexdigest())
