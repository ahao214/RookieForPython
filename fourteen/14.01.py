# 读取与搜寻XML文件
from xml.etree.ElementTree import parse
# 开始分析products.xml文件，files/products.xml是要读取的XML文件的名字
doc = parse('files/products.xml')
# 通过XPath搜搜子节点集合，然后对这个子节点集合进行迭代
for item in doc.iterfind('products/product'):
    # 读取product节点的id子节点的值
    id = item.findtext('id')

    name = item.findtext('name')
    price = item.findtext('price')

    print('uuid', item.get('uuid'))
    print('id', id)
    print('name', name)
    print('price', price)
    print('-------------------------')





