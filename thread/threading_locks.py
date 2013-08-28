#coding:utf-8

import threading, time

b = 50

l = threading.Lock()

def threadcode():
    global b
    print "Thread %s invoked" % threading.currentThread().getName()

    #acquire / release

    l.acquire()
    try:
        print "Thread %s running" % threading.currentThread().getName()
        time.sleep(1)
        b = b + 50
        print "Thread %s set b to %d" % (threading.currentThread().getName(),b)
    finally:
        l.release()

print "Value of b at start of program:", b

childthreads = []

for i in range(1, 5):
    t = threading.Thread(target = threadcode, name = "Thread-%d" % i)

    t.setDaemon(1)

    t.start()
    childthreads.append(t)

for t in childthreads:
    t.join()

print "New value of b:", b
