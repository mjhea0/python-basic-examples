#coding:utf-8

import time
 
class Timer(object):
    def __init__(self, verbose=False):
        self.verbose = verbose
 
    #进入的时候
    def __enter__(self):
        self.start = time.time()
        return self
 
    #退出的时候
    def __exit__(self, *args):
        self.end = time.time()
        self.secs = self.end - self.start
        self.msecs = self.secs * 1000  # millisecs
        if self.verbose:
            print 'elapsed time: %f ms' % self.msecs
            
with Timer() as t:
    print '%s%s' % ('one', 1)

#打印运行时间
print '耗费%s秒' % t.secs