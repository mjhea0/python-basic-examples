from mongoengine import *

connect('mongoengine_test')

class User(Document):
    name = StringField()
    tags = ListField(StringField())
    likes = IntField()
    
user = User(name='bob', tags=['mongo', 'python']).save()
print user.tags

User.objects(name='bob').update_one(add_to_set__tags='ruby', inc__likes=1)
user.reload()
print user.tags
print user.likes