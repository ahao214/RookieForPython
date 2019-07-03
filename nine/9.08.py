# 异常捕捉中的finally子句
# 未抛出异常是执行finally子句中的代码
def funone():
    try:
        print("funone正常执行")
    finally:
        print("funone finally")

# 抛出异常时执行finally子句中的代码
def funtwo():
    try:
        raise Exception
    except:
        print("funtwo抛出异常")
    finally:
        print("funtwo finally")

# 用return语句退出函数之前执行finally子句中的代码
def funthree ():
    try:
        return 20
    finally:
        print("funthree finally")

# 抛出异常时执行finally子句中的代码，但在finally子句中执行del x操作，再一次抛出了异常
def funfour():
    try:
        x = 1/0
    except ZeroDivisionError as e:
        print(e)
    finally:
        print("funfour finally")
        del x


funone()
funtwo()
print(funthree())
funfour()


