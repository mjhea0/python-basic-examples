#coding:utf-8

scope = {} 
scope['x'] = 2 
scope['y'] = 3 
eval('x * y', scope) 

scope = {}
exec 'x = 2' in scope
eval('x*x', scope)

areaStr = "pi*(radius*radius)"
print "\nArea = " + str(eval(areaStr, {"pi":3.14}, {"radius":5}))
