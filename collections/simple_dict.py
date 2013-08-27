#coding:utf-8

class SimpleDictionary:
   def __getitem__(self, key):
      return self.__dict__[key]

   def __setitem__(self, key, value):
      self.__dict__[key] = value
