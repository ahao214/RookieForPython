# 自定义异常类，表示操作数或计算结果为负数时抛出的异常

class NegativeException(Exception):
    pass

# 自定义异常类，表示操作数为0时抛出的异常
class ZeroException(Exception):
    pass

class SpecialCalc:
    def add(self, x, y):
        # 当x和y至少有一个小于0时抛出NegativeException异常
        if x < 0 or y < 0:
            raise NegativeException
        return x + y
    def sub(self, x, y):
        # 当x和y的差值是负数时抛出NegativeException异常
        if x - y < 0:
            raise NegativeException
        return x - y

    def mul(self, x, y):
        # 当x和y至少有一个为0时抛出ZeroException异常
        if x == 0 or y == 0:
            raise ZeroException
        return x * y

    def div(self, x, y):
        return x / y

while True:
    try:
        # 创建SpecialCalc()
        calc = SpecialCalc()
        # 从console输入表达式
        expr = input("请输入要计算的表达式，例如，add(1,2):")
        # 当输入":exit"时退出while循环
        if expr == ":exit":
            break ;

        # 使用eval函数动态执行输入的表达式，前面需要加上"calc."前缀
        # 因为这些方法都属于SpecialCalc类
        result = eval('calc.' + expr)
        # 在控制台输出计算结果，保留小数点后两位
        print("计算结果:{:.2f}".format(result))

    except NegativeException:
        print("负数异常")

    except ZeroException:
        print("操作数为0异常")

    except ZeroDivisionError:
        print("分母不能为0异常")

    except:
        print("其他异常")




