#coding:utf-8

class FooClass(object):
    version = 0.1

    def __init__(self, nm='A'):
           self.name = nm      
           print'Created a class instance for', nm
    def showname(self):
           print 'Your name is', self.name
           print 'My name is', self.__class__.__name__
    def showver(self):
           print self.version  
    def addMe2Me(self, x):     
           return x + x
           
foo1 = FooClass()
foo1.showname()
foo1.showver()

print foo1.addMe2Me(5)
print foo1.addMe2Me('xyz')
