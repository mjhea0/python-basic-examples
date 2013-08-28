#coding:utf-8

import threading, time
from sys import stdout

def sleepandprint():
    time.sleep(1)
    print "Hello from both of us."

def threadcode():
    stdout.write("Hello from the new thread.  My name is %s\n" % threading.currentThread().getName())
    sleepandprint()

print "Before starting a new thread, my name is", threading.currentThread().getName()

t = threading.Thread(target = threadcode, name = "ChildThread")
t.setDaemon(1)

t.start()
stdout.write("Hello from the main thread.  My name is %s\n" % threading.currentThread().getName())
sleepandprint()

t.join()
