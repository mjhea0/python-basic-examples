#coding:utf-8

d = {"server":"A", "database":"master"}    
print d 

del d['server']                                 
print d 

d.clear()                                      
print d

del d

try:
  print d
except:
  print "Error, Not Defined."
