#coding:utf-8

import sys

def excFunc() :
    raise ValueError

try:
    excFunc()
except:
    print "Got an exception"
    print sys.exc_info()
