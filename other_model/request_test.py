# 测试使用test模块
import requests
import ssl

# 忽略所有的证书验证
re = requests.get('http://12306.com')
print(re.status_code)
print(re.text)

# 传入一个带参数的url
ssl._create_default_https_context = ssl._create_unverified_context
# 使用https的时候可以不检查
re = requests.get('https://www.baidu.com', params={'q': 'python', 'cat': '1001'}, verify=False)
print(re.url)
print(re.status_code)
# 检查编码
print(re.encoding)
# 获取content
print(re.content)

print('可以直接输出json ', re.json)

# 可以添加header
re = requests.get('https://www.baidu.com',
                  headers={'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit'},
                  verify=False)
print(re.status_code)

# 发送post请求
re = requests.post('https://baidu.com', data={'form_email': 'abc@example.com', 'form_password': '123456'}, verify=False)
print(re.status_code)

params = {'key': 'value'}
r = requests.post('https://www.baidu.com', json=params, verify=False)  # 内部自动序列化为JSON
print(r.url)

# 上传文件
upload_files = {'file': open('__init__.py', 'rb')}
r = requests.post('http://www.baidu.com', files=upload_files)
print(r.headers)
print(r.cookies)

# 自己指定cookies
cs = {'weixinjie': 'aaa'}
# 可以自己指定timeiout
r = requests.post('https://www.baidu.com', cookies=cs, verify=False, timeout=1)
print(r.cookies)
