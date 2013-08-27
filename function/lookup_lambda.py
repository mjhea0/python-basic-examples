#coding:utf-8

def weird():
    spam = 42
    handler = (lambda: spam * 2)    

    spam = 50
    print handler()                 

    spam = 60
    print handler()                 
    
weird()
