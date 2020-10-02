# 利用match方法和group方法完成字符串的模式匹配，并抛出匹配结果
import re
m = re.match('hello', 'hello')
if m is not None:
    print(m.group())

m = re.match('hello','world')
if m is not None:
    print(m.group())
print(m)
m = re.match('hello', 'hello world')
if m is not None:
    print(m.group())

print(m)





