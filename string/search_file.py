#coding:utf-8

import os

#listdir函数
for f in os.listdir('/Users/bob/pcodes/python-basic-emaples/intro/'):
    if f.endswith('.py'):
        print "Python file: " + f
    elif f.endswith('.txt'):
        print "Text file: " + f
