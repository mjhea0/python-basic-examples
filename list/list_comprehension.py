#coding:utf-8

print [x*x for x in range(10)] 

print [x*x for x in range(10) if x % 3 == 0] 
print [(x, y) for x in range(3) for y in range(3)]

li = [1, 9, 8, 4] 
print [elem*2 for elem in li]                   
print li                                             

li = [elem*2 for elem in li]                  
print li
