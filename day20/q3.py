a=[1,2,3]
print(id(a))
a=a+[4,5]
print(id(a))

b=[1,2,3]
print(id(b))
b.extend([4,5])
print(id(b))