#coding:utf-8

import json
s = '{"foo": 6, "bar": [1, 2, 3]}'
d = json.loads(s)
print d
print d['foo']
print d['bar']
print type(d)