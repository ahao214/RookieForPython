fruits = ['apple', 'orange', 'banana', 'purple']
new_fruit = []
fruit = input("请输入一种水果名称：")
fruit = fruit.strip()
if fruit in fruits:
    new_fruit.append(fruit)
else:
    print("你输入的水果不存在！")

if len(new_fruit) > 0:
    for item in new_fruit:
        print("得到的水果是：%s" % item)

