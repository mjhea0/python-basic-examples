#coding:utf-8

def echo(message): 
    print message 


def indirect(func, arg): 
     func(arg)     

indirect(echo, 'Hello jello!')
