#coding:utf-8

from mongoengine import *

connect('mongoengine_test')

class User(Document):
    name = StringField()
    email = EmailField()
    rating = IntField()
    
    #申明后自动创建索引
    meta = {
        'indexes': ['name', 'email', '-rating', ('name', 'rating')]
    }

#测试一个数据
bob = User(name='boostbob',email='debugger@126.com', rating=1)
bob.save()