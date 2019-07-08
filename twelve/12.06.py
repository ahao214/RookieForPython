set1 = set(range(10))
print(type(set1))

print(set1)


set2 = set('hello')
print(set2)

set3 = set(['Bill', 'Mike', 'john', 'Hero'])
print(set3)

a = set ((1,2, 3))
b = set([3, 5, 1, 7])

print(a.union(b))
print(a | b)
# 求a和b的交集
print(a.intersection(b))
# 求a和b的交集
print(a & b)



