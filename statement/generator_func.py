#coding:utf-8

def gensquares(N): 
    for i in range(N): 
        yield i ** 2             # Resume here later

for i in gensquares(5):          # Resume the function
    print i, ':',                # Print last yielded value
