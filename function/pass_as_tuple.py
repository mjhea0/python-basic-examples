#coding:utf-8

def fun(name, location, year=2006):
    print "%s/%s/%d" % (name, location, year)

tuple = ("DaNae", "Paris", 2003)

#using * syntax
fun(*tuple)
