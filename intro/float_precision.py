#coding:utf-8

import math

format = "Pi with three decimals: %.3f" 
from math import pi 
print format % pi

'''浮点数格式化'''
print "Today's stock price: %f" % 50.462, 5 
print "Today's stock price: %.2f" % 50.4625     
print "Change since yesterday: %+.2f" % 1.5

print '%f' % 1234.567890
print '%.2f' % 1234.567890
print '%E' % 1234.567890
print '%e' % 1234.567890
print '%g' % 1234.567890
print '%G' % 1234.567890
print "%e" % (1111111111111111111111L)

for each_num in (.2, .7, 1.2, 1.7, -.2, -.7, -1.2, -1.7):
    print "int(%.1f)\t%+.1f" % (each_num, float(int(each_num)))
    print "floor(%.1f)\t%+.1f" % (each_num, math.floor(each_num))
    print "round(%.1f)\t%+.1f" % (each_num, round(each_num))
    print '-' * 20
