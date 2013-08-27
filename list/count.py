#coding:utf-8

responses = [ 1, 2, 6, 4, 8, 5, 9, 7, 8, 10,
              5, 6, 7, 5, 6, 4, 8, 6, 8, 10 ]

print "Rating     Frequency"

for i in range(1, 11):
   print "%6d %13d" % (i, responses.count(i))
