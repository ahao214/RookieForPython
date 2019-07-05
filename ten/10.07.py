class Rectangle:
    def __init__(self):
        self.left = 0
        self.top = 0
        # 用于监控position属性的写操作，可以同时设置left属性和top属性
        def setPosition(self, position):
            self.left, self.top = position

        # 用于监控position属性的读操作，可以同时获取left属性和top属性
        def getPosition(self):
            return self.left, self.top
        # 用于监控position属性的删除操作
        def deletePosition(self):
            print('position属性已经被删除')
            # 重新初始化left和top属性
            self.left = 0
            self.top = 0

        position = property(getPosition, setPosition, deletePosition)

r = Rectangle()
r.left = 10
r.top = 20
print('left', '=', r.left)
print('top', '=', r.top)

