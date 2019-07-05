class FactorialDict:
    def __init__(self):
        # 创建字典对象
        self.numDict = {}

    # 用于计算阶乘的方法：
    def factorial(self, n):
        if n == 0 or n == 1 :
            return 1
        else:
            return n * self.factorial(n - 1)

    #从字典中获取key对应的value时调用该方法
    def __getitem__(self, key):
        print("__getitem__方法被调用,key={}".format(key))
        #判断key是在字典中存在，如果存在，返回value的阶乘，否则返回0
        if key in self.numDict:
            return self.factorial(self.numDict[key])
        else:
            return 0

    # 设置key对应的value时调用该方法
    def __setitem__(self, key, value):
        print("__setitem__方法被调用,key={}".format(key))
        self.numDict[key] = int(value)

    # 使用del语句删除key对应的key-value对时调用
    def __delitem__(self, key):
        print("__delitem__方法被调用,key={}".format(key))
        del self.numDict[key]

    #使用len函数获取字典中key-value对个数时调用
    def __len__(self):
        print("__len__方法被调用")
        return len(self.numDict)

# 创建FactorialDict对象
d = FactorialDict()
# 设置字典中的key-value值对
d['4!'] = 4
d['7!'] = 7
d['12!'] = 12
# 获取4的阶乘
print('4!','=',d['4!'])
# 获取7的阶乘
print('7!','=',d['7!'])
#获取12的阶乘
print('12!','=',d['12!'])

# 获取字典的长度
print('len', '=', len(d))

# 删除key为'7！'的key-value对
del d['7!']

# 获取7的阶乘
print('7!', '=', d['7!'])

# 获取字典的长度
print('len', '=', len(d))