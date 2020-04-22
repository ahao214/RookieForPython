# 未使用函数抽象的代码实现
data = {}
# 下面的代码初始化字典data和key的值
data["d"]={}
data["names"]=[]
data["products"]=[]
print("请输入字典数据，key和value之间用逗号分隔")

# 从控制台输入key为d的值
dictStr = input(":")
# 将以逗号分隔的字符串转换为列表
list = dictStr.split(",")
keys =[]
values =[]

# 将列表拆分成keys和values的两个列表
for i in range(len(list)):
    # key
    if i % 2 == 0:
        keys.append(list[i])
    else:
        values.append(list[i])

# 利用zip和dict函数将keys和values两个列表合并成一个字典，
# 并利用update方法将该字典追加到key为d的值的后面
data["d"].update(dict(zip(keys, values)))


print("请输入姓名，多个姓名之间用逗号分隔")
# 从控制台输入key为names的值
nameStr = input(":")

# 将以逗号分隔的字符串转换为列表
names = nameStr.split(",")
# 将列表names追加到key为names的值的后面
data["names"].extend(names)


print("请输入产品，多个产品之间用逗号隔开")
# 从控制台输入key为products的值
productStr = input(":")

# 将以逗号分隔的字符串转换为列表
products = productStr.split(",")
# 将列表products追加到key为products的值的后面
data["products"].extend(products)

# 输出字典data中的数据，每一个key和对应值是一行
for key in data.keys():
    print(key, ":", data[key])





