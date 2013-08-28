#coding:utf-8

def cube(x): return x*x*x
print map(cube, range(1, 11))

def inc(x): return x + 10 
counters = [1, 2, 3, 4] 

print map(inc, counters)
print map((lambda x: x + 3), counters)
