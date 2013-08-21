# -*- coding: UTF-8 -*-
#coding=utf-8
#encoding:utf-8

try:
    input("please type 1/0:")
except ZeroDivisionError:
    ''' 尝试捕捉异常 '''
    print 'can not be divided by zero'
except:
    ''' 其他异常 '''
    print 'unknown errors'