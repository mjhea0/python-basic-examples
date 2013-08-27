#coding:utf-8

#(key,value) pairs
items = [('name', 'Gumby'), ('age', 42)]
d = dict(items)

print d
print d['name']

#keyword arguments
d = dict(name='Gumby', age=42)
print d

#list arguments
fdict = dict((['x', 1], ['y', 2]))
print fdict

#zip
print dict(zip(('x', 'y'), (1, 2)))
