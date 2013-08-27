#coding:utf-8

numList = [2000, 2003, 2005, 2006]
stringList = ["Essential", "Python", "Code"]
mixedList = [1, 2, "three", 4]
subList = ["A", "B", ["C", 2006]]
listList = [numList, stringList, mixedList, subList]

for x in listList:
    for y in x:
        if isinstance(y, int):
            print y + 1
        if isinstance(y, basestring):
            print "String:" + y
