# 使用字符集

import  re
m = re.match('[ab][cd][ef][gh]', 'adfh')
print(m.group())

m = re.match('[ab][cd][ef][gh]', 'bceg')
print(m.group())

m = re.match('[ab][cd][ef][gh]', 'abceh')
print(m.group())



