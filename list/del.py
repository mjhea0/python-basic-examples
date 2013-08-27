#coding:utf-8

x = [1, 2, 3, 4, 5]
print x

del x[1]                 # x is now [1, 3, 4, 5]
print x

del x[::2]               # x is now [3, 5]
print x
