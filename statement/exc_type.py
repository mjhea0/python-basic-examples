#coding:utf-8

import sys

dict = {}
dict[ValueError] = "Enter a valid value"
dict[IOError] = "An error occurred in the IO system"

try:
    raise ValueError
except:
    if dict.has_key(sys.exc_type) :
        print dict[sys.exc_type]
