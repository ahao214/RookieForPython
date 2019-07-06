# 三角形
class RightTriangle:
    def __init__(self):
        # 定义一个变量n，表示当前的行数
        self.n =  1
    def __next__(self):
        # 通过字符串的乘法获取直角三角形每一行的字符串，每一行字符串的长度是2 * n -1
        result = '*' * (2 * self.n - 1)
        # 行数加1
        self.n += 1
        return  result
    # 返回方法必须返回一个迭代器
    def __iter__(self):
        return  self

rt = RightTriangle()
# 对迭代器进行迭代
for e in rt:
    # 限制输出行的长度不能大于20，否则会无限输出行
    if len(e) > 20:
        break;
    print(e)

print("-----------------------------")

# 可无限制迭代斐波那契数列
class Fibonacci:
    # 在构造方法中定义两个变量a和b，用来表示fbnq数列的最开始的两个值
    def __init__(self):
        self.a = 0
        self.b = 1
    def __next__(self):
        # self.a就是当前要迭代的值
        result = self.a
        # 计算fbnq的下一个值，并将a变成原来的b，将b变成下一个值
        self.a, self.b = self.b, self.a + self.b
        # 返回当前迭代的值
        return  result
    # 该方法必须返回一个迭代器
    def __iter__(self):
        return  self;

fibs = Fibonacci()
# 对fbnq数列进行迭代
for fib in fibs:
    print(fib, end = ' ')
    # 迭代的值不能超过500
    if fib > 500:
        break;


