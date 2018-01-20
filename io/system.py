# 测试操作文件与目录
import logging
import os

import shutil

print(os.name)

# 获取系统详细信息
print(os.uname())

# 获取系统环境变量
print(os.environ)

# 获取某个变量的值
print(os.environ.get('SDKMAN_BROKER_SERVICE'))

# 操作文件和目录

# 查看当前绝对路径
path = os.path.abspath('.')
print(path)

# 创建一个新的目录,首先将新的目录表示出来(这里仅仅是区分了操作系统)
newPath = os.path.join(path, 'weixinjie')
os.mkdir(newPath)

# 删除路径
os.rmdir(newPath)

# 需要拆分路径的时候使用split函数
print(os.path.splitext("/Users/will/Downloads/test.txt"))

# 文件重命名(注意后面也是绝对路径才行 )
try:
    os.rename('/Users/will/Downloads/app.zip', 'test_apk.zip')
    os.remove('/Users/will/Downloads/app.zip')
except Exception as e:
    logging.error(e)

# 对文件进行复制
try:
    shutil.copyfile('/Users/will/Downloads/aaa.jpg', '/Users/will/Downloads/bbb.jpg')
except Exception as e:
    logging.error(e)

# 过滤文件夹
print([x for x in os.listdir('.') if os.path.isdir(x)])

print([x for x in os.listdir('/Users/will/Downloads') if os.path.isfile(x)])
print(os.listdir('/Users/will/Downloads'))

print([x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1] == '.py'])
