#coding:utf-8

class myClass(object):
     def __init__(self):
         self.foo = 100

myInst = myClass()

print hasattr(myInst, 'foo')
print getattr(myInst, 'foo')
print hasattr(myInst, 'bar')
#print getattr(myInst, 'bar')
print getattr(myInst, 'bar', 'oops!')

print setattr(myInst, 'bar', 'my attr')
print dir(myInst)
print getattr(myInst, 'bar')
print delattr(myInst, 'foo')
print dir(myInst)
print hasattr(myInst, 'foo')
