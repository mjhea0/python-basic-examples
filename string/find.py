#coding:utf-8

print 'With a moo-moo here, and a moo-moo there'.find('moo')
title = "A B C D"

print title.find('A')
print title.find('B')
print title.find('D')

#找不到返回-1
print title.find('E')

searchStr =  "Red Blue Violet Green Blue Yellow Black"

print searchStr.find("Red")
print searchStr.find("Blue")
print searchStr.find("Teal")

#find from right
print searchStr.rfind("Blue")
