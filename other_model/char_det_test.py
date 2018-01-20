# 使用chardet对文本进行字符识别
import chardet

# 使用chardet对文本进行识别 结果中 encoding代表编码 confidence 代表百分之多少的成功  language代表语言
s = chardet.detect('韦新'.encode('utf-8'))
print(s)


