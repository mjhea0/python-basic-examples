#coding:utf-8

def weird():
    spam = 42
    return (lambda: spam * 2)     

act = weird()
print act()     # prints 84
