# 属性
class Rectangle:
    def __init__(self):
        self.left = 0
        self.top = 0

    # 同时设置left属性和top属性的值，position参数值应该是元祖或列表类型
    def setPosition(self, position):
        self.left,self.top = position

    # 同时获取left属性和top属性的值，返回的值是元祖类型
    def getPosition(self):
        return self.left, self.top

r = Rectangle()
r.left = 10
r.top = 20
print('left','=', r.left)
print('top', '=', r.top)
# 通过setPosition方法设置left属性和top属性的值
r.setPosition((30, 50))

# 通过getPosition方法返回left属性和top属性的值
print('position', '=', r.getPosition())





