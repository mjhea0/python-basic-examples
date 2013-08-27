#coding:utf-8

x = {'username': 'admin', 'machines': ['foo', 'bar', 'baz']}
y = x.copy()

y['username'] = 'mlh'

#x当中的也被移除了
#说明默认的copy是浅拷贝
y['machines'].remove('bar')

print y
print x
