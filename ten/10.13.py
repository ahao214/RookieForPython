# 递归生成器
def enumList(nestedList):
    try:
       # 对多维列表进行迭代
        for subList in nestedList:
            # 将多维列表中的每一个元素传入enumList函数，如果该元素是一个列表，那么会继续迭代
            # 否则会抛出TypeError异常，在异常处理代码中直接通过yield语句返回这个普通的元素值
            # 这个异常也是递归的终止条件
            for element in enumList(subList):
                yield element

    except TypeError:
        # 将普通的列表值作为生成值返回
        yield nestedList
nestedList = [4, [1, 2, [3, 5, 6]],[4, 3, [1,2 ,[4,5]],2],[1,2, 4, 5, 7]]
# 迭代生成器
for num in enumList(nestedList):
    print(num, end=' ')


