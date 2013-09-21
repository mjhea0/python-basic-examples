#coding:utf-8

import pickle, StringIO

class Person(object):
    def __init__(self, name, address):
        self.name = name
        self.address = address
    def display(self):
        print 'name:', self.name, 'address:', self.address

p = Person("张三", "中国成都")
print pickle.dumps(p)
print type(pickle.loads(pickle.dumps(p)))