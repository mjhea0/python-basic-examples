#coding:utf-8

import math

print sum(x ** 2 for x in range(4))
print sorted(x ** 2 for x in range(4))
print sorted((x ** 2 for x in range(4)), reverse=True)

print map(math.sqrt, (x ** 2 for x in range(4)))
