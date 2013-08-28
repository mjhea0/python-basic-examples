#coding:utf-8

def add(x,y): return x+y

print reduce(add, range(1, 11))

print reduce((lambda x, y: x + y), [1, 2, 3, 4])
print reduce((lambda x, y: x * y), [1, 2, 3, 4])
