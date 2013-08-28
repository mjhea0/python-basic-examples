#coding:utf-8

import threading
import random
import time

class PrintThread( threading.Thread ):
   def __init__( self, threadName ):
      threading.Thread.__init__( self, name = threadName )
      self.sleepTime = random.randrange( 1, 6 )
      print "Name: %s; sleep: %d" % ( self.getName(), self.sleepTime )

   def run( self ):
      print "%s going to sleep for %s second(s)" % ( self.getName(), self.sleepTime )
      time.sleep( self.sleepTime )
      print self.getName(), "done sleeping"

thread1 = PrintThread( "thread1" )
thread2 = PrintThread( "thread2" )
thread3 = PrintThread( "thread3" )

thread1.start()   # invokes run method of thread1
thread2.start()   # invokes run method of thread2
thread3.start()   # invokes run method of thread3
