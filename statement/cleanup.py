#coding:utf-8

try:
    raise KeyboardInterrupt
finally:
    ''' 先打印这个再打印异常信息 '''
    print '先打印Goodbye, World!之后是异常信息...'
