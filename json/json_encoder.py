#coding:utf-8

from json import JSONEncoder
from json import JSONDecoder

#注意构造JSONEncoder()对象后使用
str = JSONEncoder().encode({"foo": ["bar", "baz"]})
print str
print type(JSONDecoder().decode(str))