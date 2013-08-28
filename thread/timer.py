#coding:utf-8

import threading
import os

def clean_queue (qPath):
    jobList = os.listdir(qPath)

    for j in jobList:
        delPath = "%s/%s" % (qPath, j)
        os.remove(delPath)
        print "Removing " + delPath

qPath = "/print/queue01"
waitTime = 600 #10 minutes

#Create timer thread
wakeCall = threading.Timer(waitTime, clean_queue, (qPath ,))

#Start timer thread
wakeCall.start()
