#coding:utf-8

a = set([1, 2, 3])
b = set([2, 3, 4])
print a.union(b)
print a | b
set([1, 2, 3, 4])
c = a & b
print c.issubset(a)
print c <= a
print c.issuperset(a)
print c >= a
print a.intersection(b)
print set([2, 3])
print a & b
print a.difference(b)
print a - b
print a.symmetric_difference(b)
print a ^ b
print a.copy()
print a.copy() is a
