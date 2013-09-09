#coding:utf-8

from mongoengine import *

connect('mongoengine_test')

class User(Document):
    email=EmailField()
    
#是否验证
#Invalid Mail-address: debugger@126: ['email']
#bob = User(email='debugger@126').save()

bob = User(email='debugger@126.com').save()
bob.email = 'xxx@xyz'

#捕捉并且打印异常
try:
    bob.save()
except Exception, ex:
    print ex
    
bob.email = 'debugger@126.com'
bob.save()

#存在
user = User.objects(email__iexact='debugger@126.com')
print user

#不存在
user = User.objects(email__iexact='debugger@126.cn')
print user

debugger126 = User.objects(email__iexact='debugger@126.com').count()
print debugger126