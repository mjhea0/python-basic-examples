#coding:utf-8

import thread
import time

def print_time(threadName, delay):
    while 1:
        time.sleep(delay)
        print "%s: %s" % (threadName, time.ctime(time.time()))

#Start threads to print time at different intervals
thread.start_new_thread(print_time, ("Thread01",2,))
thread.start_new_thread(print_time, ("Thread02",4,))

while 1:
    pass
