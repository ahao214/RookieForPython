# 将迭代器转换为列表
class Fibonacci:
    def __init__(self):
        self.a = 0
        self.b = 1
    def __next__(self):
        result = self.a
        self.a, self.b = self.b, self.a + self.b
        # 要想让迭代停止，需要抛出StopIteration异常
        if result > 500:
            raise StopIteration
        return result

    def __iter__(self):
        return  self

fibs = Fibonacci()
# 将迭代器转换为列表
print(list(fibs))
fibs2 = Fibonacci()

# 使用for循环对迭代器进行迭代
for fib in fibs2:
    print(fib, end = ' ')
