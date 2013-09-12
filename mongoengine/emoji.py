#coding:utf-8

from mongoengine import *
import base64

connect('mongoengine_test')

class Emoji(Document):
    content = StringField()
    
file = open('/Users/bob/downloads/emoji.txt', "rb")
str = file.read()
print base64.b64encode(str)
print base64.b32encode(str)
print base64.b16encode(str)

#数据库
e = Emoji(content = str).save()
ee = Emoji.objects().first()
print ee.content

#base64 encode
str = "eyJzdGF0dXMiOiJQb3N0IHN1Y2NlZWQhIPCfmITwn5iD8J+YgPCfmIrimLrwn5iJ8J+YjfCfmJvwn5id8J+YnPCfmJnwn5iX8J+YmCIsInBhcmFtcyI6eyJhIjoiYiJ9fQ=="
print base64.b64decode(str)

#base32 decode
str = "PMRHG5DBOR2XGIR2EJIG643UEBZXKY3DMVSWIIJA6CPZRBHQT6MIH4E7TCAPBH4YRLRJROXQT6MIT4E7TCG7BH4YTPYJ7GE56CPZRHHQT6MJT4E7TCL7BH4YTARCYITQMFZGC3LTEI5HWITBEI5CEYRCPV6Q===="
print base64.b32decode(str)

str = "7B22737461747573223A22506F737420737563636565642120F09F9884F09F9883F09F9880F09F988AE298BAF09F9889F09F988DF09F989BF09F989DF09F989CF09F9899F09F9897F09F9898222C22706172616D73223A7B2261223A2262227D7D"
#base16 decode
print base64.b16decode(str)

Emoji.objects.delete()