#coding:utf-8

d2 = {'spam': 2, 'ham': 1, 'eggs': 3}         # Make a dictionary

print d2.get('spam' )                         # A key that is there
print d2.get('toast')                         # A key that is missing
print d2.get('toast', 88)
