#coding:utf-8

L = [None] * 100

if type(L) == type([]):                      # Type testing, if you must...
    print 'yes' 

if type(L) == list:                          # Using the type name
    print 'yes' 

if isinstance(L, list):                      # Object-oriented tests
    print 'yes'
