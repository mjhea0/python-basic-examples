#coding:utf-8

aList = [1, 2, 3, 4, 5, 6, 7, 8, 9]
low = 3
high = 7

#If a function body is a single return expression statement
#you may choose to replace the function with the special lambda expression form
print filter(lambda x, l=low, h=high: h>x>l, aList)


bigger = lambda a, b: a > b

print bigger(1,2)
print bigger(2,1)
