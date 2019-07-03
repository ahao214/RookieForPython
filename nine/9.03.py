# try...except语句的基本用法

# 先定义一个x变量，但x变量中没有值(为none)
x = None
while True:
    try:
        # 如果x已经有了值，表示已经捕捉了异常，那么再次输入数据时，就不需要输入x的值了
        if x == None:
            x = int(input("请输入分子："))
        y = int(input("请输入分母："))
        print("x/y = {}".format(x/y))
        break;
    except:
        print("分母不能为0，请重新输入分母")

