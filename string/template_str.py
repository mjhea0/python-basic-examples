#coding:utf-8

import string

values = [5, 3, 'blue', 'red']
s = string.Template("Variable v = $v")

for x in values:
    print s.substitute(v=x)
