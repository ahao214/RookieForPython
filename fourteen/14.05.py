# 将JSON字符串类型转换为类实例

import json
class Product:
    # d参数是要传入的字典
    def __init__(self, d):
        self.__dict__ = d

# 打开products.json文件
f = open('files/product.json', 'r', encoding='utf-8')

# 从product.json文件中读取JSON字符串
jsonStr = f.read()

# 通过指定类的方式将JSON字符串转换为Product对象
my1 = json.loads(jsonStr, object_hook=Product)
# 下面3行代码输出Product对象中相应属性的值
print('name', my1.name)
print('price', my1.price)
print('count', my1.count)
print('-----------------')

# 定义用于将字典转换为Product对象的函数
def json2Product(d):
    return Product(d)

# 通过指定类回调函数的方式将JSON字符串转换为Product对象
my2 = json.loads(jsonStr, object_hook=json2Product)
# 下面3行diam输出Product对象相应属性的值
print('name', my2.name)
print('price', my2.price)
print('count', my2.count)
print('-----------------')
f.close()
