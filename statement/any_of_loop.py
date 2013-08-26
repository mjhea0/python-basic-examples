#coding:utf-8

for x in [n**2 for n in range(5)]:
    print x, ':',

for x in map((lambda x:x**2), range(5)):
    print x, ':',
