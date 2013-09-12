#coding:utf-8

from mongoengine import *

connect('mongoengine_test')

class User(Document):
    name = StringField()
    tags = ListField(StringField())
    likes = IntField()

#没有任何记录
#User.objects.update_one(add_to_set__tags='ruby', inc__likes=2)
#user = User.objects.first()
##'NoneType' object has no attribute 'reload'
#user.reload()
#print user.id

#没有任何记录
User.objects.update_one(add_to_set__tags='ruby', inc__likes=2, upsert=True)
user = User.objects.first()
user.reload()
print user.id