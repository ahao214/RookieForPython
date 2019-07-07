# 使用match方法和search方法对文本模式进行匹配和搜索
import  re
# 进行文本模式匹配，匹配失败，match方法返回None
m = re.match('python', 'I love python')
if m is not None:
    print(m.group())
print(m)

# 进行文本模式搜索，搜索成功
m = re.search('python', 'I love python')
if m is not None:
    print(m.group())
print(m)

