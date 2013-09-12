#coding:utf-8

from mongoengine import *

connect('mongoengine_test')

class Membership(Document):
    member_id = StringField()
    follow_id = StringField()
    
#这样写法只会创建ObjectID
#Mership.objects(member_id="boostbob_id", follow_id="debugger_id").update_one(upsert=True)

#可以创建member_id和follow_id
#objects中的条件需要，不然只会创建1个记录
Membership.objects(member_id='boostbob_id', follow_id='debugger_id').update_one(set__member_id="boostbob_id",
                set__follow_id="debugger_id", upsert=True)
                
Membership.objects(member_id='boostbob_id', follow_id='debugger_id').update_one(set__member_id="boostbob_id",
                set__follow_id="sckiss_id", upsert=True)
                
print Membership.objects.count()

members = Membership.objects().only('member_id')
print [x.id for x in members]

Membership.objects(member_id="boostbob_id", follow_id="debugger_id").delete()