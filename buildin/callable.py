#coding:utf-8

def foo(): pass

#True
print callable(foo)

#False
print callable('bar')

class C(object): pass

#True
print callable(C)
