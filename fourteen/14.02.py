# 要先安装dicttoxml
# 在命令行运行 pip install dicttoxml

# 字典转换为XML字符串
import dicttoxml
from xml.dom.minidom import parseString
import  os
# 定义一个字典
d =[20, 'names',
    {'name':'Bill','age':'30', 'salary':2000},
    {'name':'王军','age':'41', 'salary':3000},
    {'name':'李二','age':'23', 'salary':4560}]

# 将字典转换为XML格式(bytes形式)
bxml = dicttoxml.dicttoxml(d, custom_root = 'persons')

# 将bytes形式的XML数据按utf-8编码格式解码成XML字符串
xml = bxml.decode('utf-8')

# 输出XML字符串
print(xml)

# 解析XML字符串
dom = parseString(xml)

prettyxml = dom.toprettyxml(indent= ' ')

# 创建file目录
os.makedirs('file', exist_ok=True)

# 以只写和utf-8编码格式的方式打开persons.xml文件
f = open('file/persons.xml', 'w', encoding='utf-8')

# 将格式化的XML字符串写入persons.xml文件
f.write(prettyxml)
f.close()


