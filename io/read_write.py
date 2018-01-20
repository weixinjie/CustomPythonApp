'测试文件读写'

# 测试文件读取
try:
    f = open('/Users/will/Downloads/test.txt', 'r')
    print(f.read())
finally:
    if f:
        f.close()

print("-----------------")

# python使用with语句来帮我们自动调用close方法
with open('/Users/will/Downloads/test.txt', 'r') as f:
    print(f.read())

# 按行来读取
with open('/Users/will/Downloads/test.txt', 'r') as f:
    for line in f.readlines():
        print(line.strip(), '哈哈哈')

# 读取二进制文件
f = open("/Users/will/Downloads/aaa.jpg", 'rb')
# print(f.read())
f.close()

# 遇到编码不规则的文件,可以指定编码格式或者使用ignore来忽略错误类型
f = open('/Users/will/Downloads/test.txt', 'r', encoding='gbk', errors='ignore')
print(f.read())
f.close()

# 开始写文件
f = open('/Users/will/Downloads/test.txt', 'w')
f.write('我爱张睿')
# 一定不要忘了进行close关闭输出流
f.close()

# 读写文件的权限文件使用文档 https://docs.python.org/3/library/functions.html#open
# 使用with函数来进行写文件
# a代表追加  w代表写入(删除后重新写入)  r代表读取
with open('/Users/will/Downloads/test.txt', 'a') as f:
    f.write('我爱张睿啊啊啊啊啊啊啊啊啊')
    f.close()
