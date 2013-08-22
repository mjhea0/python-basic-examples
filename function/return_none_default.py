#coding:utf-8

def maximum(x, y):
  if x > y:
    return x
  else:
    return y

print maximum(2, 3)

def pass_func():
  pass 

print (pass_func() == None)
