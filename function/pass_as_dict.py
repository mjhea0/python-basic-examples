#coding:utf-8

def fun(name, location, year=2006):
    print "%s/%s/%d" % (name, location, year)

dictionary = {'name':'Brendan','location':'Orlando', 'year':1999}
#using ** syntax
fun(**dictionary)
