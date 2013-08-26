#coding:utf-8

try:
   v = int(raw_input("Enter a value: "))
   print "We got some valid input!"
   x = 100 / v
except KeyboardInterrupt:
   print "well, ok, if you don't really want to.."
except ZeroDivisionError:
   print "You can't divide by ZERO!"
except:
    print "Some other error happened here"
else:
    print "All went well, x = ", x
