#coding:utf-8

dict1 = {}
dict2 = {'host': 'earth', 'port': 80}
print cmp(dict1, dict2)

dict1['host'] = 'earth'
print cmp(dict1, dict2)

dict1['port'] = 8080
print cmp(dict1, dict2)

dict1['port'] = 80
print cmp(dict1, dict2)

dict1 = {}
dict2 = {'host': 'earth', 'port': 80}
print len(dict1) > len(dict2)
