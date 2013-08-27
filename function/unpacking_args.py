#coding:utf-8

def func(a, b, c, d): 
    print a, b, c, d

args = (1, 2)
args += (3, 4)
func(*args)

args = {'a': 1, 'b': 2, 'c': 3}
args['d'] = 4
func(**args)

func(*(1, 2), **{'d': 4, 'c': 4})
func(1, *(2, 3), **{'d': 4})
func(1, c=3, *(2,), **{'d': 4})
