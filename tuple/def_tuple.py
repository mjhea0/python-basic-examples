#coding:utf-8

# Tuple can be used as keys in mappings-lists can't be.
# Tuple are returned by some built-in functions and methods.
# The tuple syntax is simple-if you separate some values with commas, you automatically have a tuple:
x = 1, 2, 3
print x

# Tuples may also be enclosed in parentheses:
x = (1, 2, 3)
print x

# The empty tuple is written as two parentheses containing nothing:
x = ()
print x

# Single value
x = 42,
print x

print ['abc']
#!!!注意
print type(['abc'])   # a list
print ('xyz')
#!!!注意
print type(('xyz'))   # a str, not a tuple
print ('xyz',)
