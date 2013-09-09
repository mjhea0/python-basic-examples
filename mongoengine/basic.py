#coding:utf-8

from mongoengine import *

connect('mongoengine_test')

class User(Document):
    email = StringField(required=True)
    first_name = StringField(max_length=50)
    last_name = StringField(max_length=50)
    
class Post(Document):
    title = StringField(max_length=120, required=True)
    #引用User对象
    author = ReferenceField(User)
    #列表结构
    tags = ListField(StringField(max_length=30))
    #列表的元素是嵌入式文档
    #不只能向前引用Comment对象
    comments = ListField(EmbeddedDocumentField('Comment'))
    #整数测试
    likes = IntField(default=1)
		#可以继承
    meta = {'allow_inheritance': True}

class TextPost(Post):
    content = StringField()

class ImagePost(Post):
    image_path = StringField()

class LinkPost(Post):
    link_url = StringField()
    
class Comment(EmbeddedDocument):
    content = StringField()
    name = StringField(max_length=120)
    
ross = User(email='ross@example.com', first_name='Ross',last_name='Lawley').save()

post1 = TextPost(title='Fun with MongoEngine', author=ross)
post1.content = 'Took a look at MongoEngine today, looks pretty cool.'
post1.tags = ['mongodb', 'mongoengine']
post1.save()

post2 = LinkPost(title='MongoEngine Documentation', author=ross)
post2.link_url = 'http://docs.mongoengine.com/'
post2.tags = ['mongoengine']
post2.save()

print Post.objects.count()
object_id = Post.objects.first().id
print type(object_id)
print object_id

p = Post.objects(id=object_id, tags='mongoengine').first()
print p

#原子更新操作
Post.objects(id=object_id).update_one(add_to_set__tags=['ruby', 'python'])
p.reload()
p.tags.append('xyz')
p.save()
print p.tags

#未知位置更新
Post.objects(id=object_id, tags='ruby').update(set__tags__S='rubyX')
p.reload()
print '未知位置更新后'
print p.tags

#整数累加操作
print p.likes
Post.objects(id=object_id).update_one(inc__likes=2)
print p.reload().likes == 3