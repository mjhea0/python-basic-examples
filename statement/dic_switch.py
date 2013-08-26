#coding:utf-8

choice = 'ham' 
print {'spam':  1.25,           # A dictionary-based 'switch'
       'ham':   1.99,           # Use has_key or get for default
       'eggs':  0.99, 
       'bacon': 1.10}[choice]
