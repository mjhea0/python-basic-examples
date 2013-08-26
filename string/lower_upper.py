#coding:utf-8

cmpStr = "abc"
upperStr = "ABC"
lowerStr = "abc"

#string.lower() 
#string.upper()

print "\nCase In-Sensitive Compare"

if cmpStr.upper() == lowerStr.upper():
    print lowerStr + " Matches " + cmpStr

if cmpStr.upper() == upperStr.upper():
    print upperStr + " Matches " + cmpStr
