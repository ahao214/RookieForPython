a = set([1,2 ])
b = set([10, 20])

# 向a集合中添加一个元素值
a.add(4)
print(a)

a.add(5)
print(a)

a.add(frozenset(b))

print(a)

d={'Bill':30, 'Mike':40}
d[a] = 50
d[frozenset(a)] =60
print(d)

t = [1,2,3]
tt =(1,2,3)
d[t]= 111
a.add (t)
a.add(d)
a.add(tt)
print(a)
