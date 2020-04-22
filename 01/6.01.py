items  = []
while True:
    key = input("请输入key值:")
    if key == "end":
        break;
    value = input("请输入value值:")
    keyvalue = [key, value]
    items.append(keyvalue)
d = dict(items)
print(d)