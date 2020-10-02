class Student:

    def __init__(self, name, sex):
        self.__name = name
        self.sex = sex

    def get(self):
        return self.__name

    def set(self, newname):
        self.__name = newname

stu = Student("TOM", "FEMAL")
print(stu.get())

print(stu.sex)
stu.set("lph")
print(stu.get())


class Teacher:
    def __init__(self):
        print("init")


