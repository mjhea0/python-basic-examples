#coding:utf-8

try:
   v = int( raw_input("Enter a value: "))
   print "We got some valid input!"
   x = 100 / v
except ValueError:
   print "Invalid input, please enter a value"
except KeyboardInterrupt:
   print "Please don't hit ctrl-c"
