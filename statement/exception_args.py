#coding:utf-8

def func(a, b, c) :
    if a < 0 or a > 10 :
        raise ValueError, "a must be between 0 and 10"
    if b > 50 :
        raise ValueError, "b must be less than 50"
    return a*b + c

func(-1,5,3)
func(5,100,2)
