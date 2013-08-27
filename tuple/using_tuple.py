#coding:utf-8

hexStringChars = ('A', 'B','C', 'D', 'E', 'F')
hexStringNums = ('1', '2', '3', '4', '5', '6','7', '8', '9','0')
hexStrings = ["1FC", "1FG", "222", "Ten"]

for hexString in hexStrings:
    for x in hexString:
        if ((not x in hexStringChars) and (not x in hexStringNums)):
            print hexString + " is not a hex string."
            break

tupleList = list(hexStringChars)
#list
print type(tupleList)
listTuple = tuple(hexStrings)
#tuple
print type(listTuple)
