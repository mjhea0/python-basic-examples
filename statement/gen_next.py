#coding:utf-8

def simpleGen():
    yield 1
    yield '2 --> punch!'

myG = simpleGen()
print myG.next()
print myG.next()
