#coding:utf-8

def func(dict_args):
    for k, v in dict_args.items():
        print k, v

func({'one': 1, 'two': 2})

def func_kwargs(**kwargs):
    for k, v in kwargs.items():
        print k, v

func_kwargs(a=1, b=2, c=3)

dict_args = {'a': 1, 'b': 2, 'c': 3}
#TypeError: func_kwargs() takes exactly 0 arguments (1 given)
#func_kwargs(dict_args)
func_kwargs(**dict_args)