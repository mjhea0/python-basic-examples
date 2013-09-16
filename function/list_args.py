#coding:utf-8

def func(*args):
    for x in args:
        print x
    
func(1,2,3)

args = (1,2,3)
func(*args)

args = [1,2,3]
func(*args)