# 将多维列表进行一维化处理，字符串整体返回
def enumList(nestedList):
    try:
        try: nestedList + ''  # 如果nestedList不是字符串类型的值，会抛出异常
        except TypeError:
            pass # 如果nestedList不是字符串类型的值，会继续使用for语句对其进行迭代
        else:
            # 如果nestedList是字符串类型的值，直接抛出TypeError异常，在异常处理代码中
            # 会直接通过yield语句返回该值
            raise TypeError
        # 继续对nestedList进行迭代
        for subList in nestedList:
            for element in enumList(subList):
                yield element
    except TypeError:
        yield nestedList

nestedList = ['a', ['b', ['c'], 20, 123,[['hello world']]]]
for num in enumList(nestedList):
    print(num, end=' ')





