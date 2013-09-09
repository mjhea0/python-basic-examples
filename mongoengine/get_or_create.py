#coding:utf-8

from mongoengine import *

connect('mongoengine_test')

class User(Document):
    name = StringField()
    email = EmailField()
    
bob, created = User.objects.get_or_create(name='Bob Wang', email='debugger@126.com')
print bob, created

bob, created = User.objects.get_or_create(name='Bob Wang', email='debugger@126.com')
print bob, created

#找不到返回空列表
user = User.objects(name='not exists')
print user

#单个元素返回None
user = User.objects(name='not exists').first()
print user

#报异常
user = User.objects(name='not exists').get()
print user