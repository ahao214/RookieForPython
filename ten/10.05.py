# 定义一个从list继承的类
class CounterList(list):
    #list的构造方法必须指定一个可变参数，用于初始化列表
    def __init__(self, *args):
        super().__init__(*args)
        # 初始化计数器
        self.counter = 0

    # 当从列表中获取值时，计数器加1
    def __getitem__(self, index):
        self.counter += 1
        #调用超类的__getitem__方法获取指定的值，当前方法只负责计数器加1
        return super(CounterList, self).__getitem__(index)

# 创建一个CounterList对象，并初始化列表
c = CounterList(range(10))
print(c)

# 反转列表
c.reverse()
print(c)

# 删除c中的一组值
del c[2:7]
print(c)

print(c.counter)

# 将列表c中的两个值相加，这时计数器加2，运行结果：10
print(c[1] + c[2])
print(c.counter)

print("----------------------------------")


# 定义一个从dict继承的类
class CounterDict(dict):
    # dict的构造方法必须指定一个可变参数，用于初始化字典
    def __init__(self, *args):
        super().__init__(*args)
        # 初始化计数器
        self.counter = 0

    # 当从列表中获取值时， 计数器加1
    def __getitem__(self, key):
        self.counter += 1
        # 调用超类的__getitem__方法获取指定的值，当前方法只负责计数器加1
        return super(CounterDict, self).__getitem__(key)

# 创建CounterDict对象，并初始化字典
d = CounterDict({'name':'Bill'})
print(d['name'])
print(d.get('age'))
d['age'] = 30
print(d['age'])
print(d.counter)

print("----------------------------------")


# 定义一个从str继承的类
class MultiString(str):
    # 该方法会在__init__方法之前调动，用于验证字符串构造方法的参数，
    # 该方法的参数要与__init__方法的参数保持一致
    def __new__(cls, *args, sep = '  '):
        s = ''
        for arg in args:
            s += arg + sep

        index = -len(sep)
        if index == 0:
            index = len(s)
        return str.__new__(cls, s[:index])
    def __init__(self, *args, sep = ' '):
        pass

cs1 = MultiString('a', 'b', 'c')
cs2 = MultiString('a', 'b', 'c', sep=',')
cs3 = MultiString('a', 'b', 'c', sep='')
print('['+cs1+']')
print('['+cs2+']')
print('['+cs3+']')

