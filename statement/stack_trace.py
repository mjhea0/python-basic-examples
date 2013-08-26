#coding:utf-8

import sys
import traceback

def excFunc() :
    raise ValueError
    
try:
    excFunc()
except:
    print "Got an exception"
    print traceback.print_stack(sys.exc_info()[2])
