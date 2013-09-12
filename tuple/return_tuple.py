#coding:utf-8

def func():
    return (1,2)
    
a, b = func()
print a
print b

(a, b) = func()
print a
print b