#coding:utf-8

from mongoengine import *

connect('mongoengine_test')

class Emoji(Document):
    content = StringField()
    
str = "Post succeed! \u{1F604}\u{1F603}\u{1F600}\u{1F60A}\u263A\u{1F609}\u{1F60D}\u{1F61B}\u{1F61D}\u{1F61C}\u{1F619}\u{1F617}\u{1F618}"
e = Emoji(content = str).save()
ee = Emoji.objects().first()

print ee.content

#Emoji.objects.delete()