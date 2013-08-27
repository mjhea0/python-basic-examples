#coding:utf-8

d = { 
  'title': 'Python Web Site', 
  'url': 'http://www.python.org', 
  'changed': 'Mar 14 22:09:15 MET 2005'
} 

x = {'title': 'Python Language Website'} 
d.update(x) 

print d


dict2 = {'host':'earth', 'port':80}
dict3 = {'host':'venus', 'server':'http'}

dict2.update(dict3)
print dict2
#['host', 'port', 'server']
print dict2.keys()

dict3.clear()
print dict3
