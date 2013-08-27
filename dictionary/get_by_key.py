#coding:utf-8

dict = {'A':'1', 'B':'2' }
dict1 = dict.copy()

print dict1
print dict1.get('A')
print dict1.get('xxx')
print dict1.get('xxx', 'no such key')
