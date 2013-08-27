#coding:utf-8

def foo():
     print 'in foo()'

bar = foo
bar()

def bar(argfunc):
  argfunc()

bar(foo)

def convert(func, seq):
    return [func(eachNum) for eachNum in seq]

myseq = (123, 45.67, -6.2e8, 999999999L)
print convert(int, myseq)
print convert(long, myseq)
print convert(float, myseq)
