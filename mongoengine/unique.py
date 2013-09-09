#coding:utf-8

from mongoengine import *

connect('mongoengine_test')

class User(Document):
    name = StringField(unique=True)
    
bob = User(name='bob').save()
print User.objects.count()

try:
    bob = User(name='bob').save()
except Exception, ex:
    print ex