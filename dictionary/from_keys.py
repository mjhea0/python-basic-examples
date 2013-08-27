#coding:utf-8

#fromkeys method creates a new dictionary with the given keys
#each with a default corresponding value of None
print {}.fromkeys(['name', 'age'])

#If you don't want to use None as the default value
#you can supply your own default
print dict.fromkeys(['name', 'age']) 
print dict.fromkeys(['name', 'age'], '(unknown)')

d = dict.fromkeys(['name', 'age'], '(unknown)') 
print d.get('name')
print d['name']
