#coding:utf-8

import time
import functools

def timeit(func):
    #不使用反射会出问题
    @functools.wraps(func)
    def wrapper():
        start = time.clock()
        func()
        end =time.clock()
        print 'used:', end - start
    return wrapper

@timeit
def foo():
    print 'in foo()'

foo()
print foo.__name__