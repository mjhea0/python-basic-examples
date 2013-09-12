from mongoengine import *

connect('mongoengine_test')

class Member(Document):
    login_name = StringField()
    password = StringField()
    
Member(login_name='boostbob', password='123456').save()

member = Member.objects(login_name='boostbob').first()
print member.password
print member.id
print Member.objects(id='522fe538421aa90ac932a6dc').first().id

