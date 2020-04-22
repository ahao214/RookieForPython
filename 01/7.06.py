# 初始化函数
def init(data):
    data["d"] = {}
    data["names"]=[]
    data["products"]=[]

# 从控制台采集数据，并转换为列表或字典的函数，flag为True将字符串转为列表；flag为False见字符串转换为字典

# msg表示提示文本，为了方便，这是假设输入的数据以逗号分隔，也可以将分隔符通过函数参数传入

def inputListOrDict(flag, msg):
    print(msg)
    # 从控制台输入字符串
    inputStr = input(":")
    # 将字符串用逗号拆分成列表
    list = inputStr.split(",")
    # 返回列表
    if flag:
        return list;

    # 下面的代码将list转换为字典，并返回这个字典
    keys = []
    values = []
    result = {}
    for i in range(len(list)):
        # key
        if i % 2 == 0:
            keys.append(list[i])
        else:
            values.append(list[i])

    # 返回字典
    return  dict(zip(keys,values))

# 输出字典中的数据
def outDict(data):
    for key in data.keys():
        print(key, ":", data[key])
