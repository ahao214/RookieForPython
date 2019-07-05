class Rectangle:
    def __init__(self):
        self.width = 0
        self.height = 0
        self.left = 0
        self.top = 0

    def __setattr__(self, key, value):
        print("{}被设置,新值为{}".format(key, value))
        if key == 'size':
            self.width, self.height = value

        elif key == 'position':
            self.left, self.top = value
        else:
            self.__dict__[key] = value

    def __getattr__(self, item):
        print("{}被获取".format(item))
        if item == 'size':
            return self.width, self.height
        elif item == 'position':
            return self.left, self.top

    def __delattr__(self, item):
        if item == 'size':
            self.width, self.height = 0, 0
        elif item == 'position':
            self.left,self.top = 0, 0

r =Rectangle()
r.size = 300, 500
r.position = 100, 400
print('size', '=', r.size)

print('position', '=', r.position)

del r.size, r.position
print(r.size)
print(r.position)


print("-------------------------------")
class MyClass:
    def __setattr__(self, key, value):
        if key == 'value':
            if value > 0:
                self.__dict__[key] = value
            else:
                print('{}属性的值必须大于0'.format(key))

        else:
            self.__dict__[key] = value

c = MyClass()
c.value = 20
print('c.value', '=', c.value)
c.value = -34
print('c.value', '=', c.value)
