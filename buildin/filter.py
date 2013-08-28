#coding:utf-8

def f(x): return x%2 != 0 and x%3 != 0
print filter(f, range(2, 25))
