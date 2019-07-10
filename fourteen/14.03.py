# 要先安装xmltodict
# 在命令行运行 pip install xmltodict

# XML字符串转换为字典
import xmltodict

# 打开products.xml文件
f = open('files/products.xml', 'rt', encoding='utf-8')

# 读取product.xml文件中的所有内容
xml = f.read()

# 分析xml字符串，并转换为字典
d = xmltodict.parse(xml)

# 输出字典内容
print(d)

f.close()


