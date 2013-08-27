#coding:utf-8

d = {'url': 'http://www.python.org', 'spam': 0, 'title': 'Python Web Site'}

d.popitem()
#{'title': 'Python Web Site', 'spam': 0}
print d

d.popitem()
print d


d = {'x': 1, 'y': 2}
d.pop('x')
print d
