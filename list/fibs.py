#coding:utf-8

fibs = [0, 1] 
for i in range(8):
    fibs.append(fibs[-2] + fibs[-1]) 

print fibs
