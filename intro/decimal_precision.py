#coding:utf-8

import decimal 

decimal.getcontext().prec = 4
print decimal.Decimal(1) / decimal.Decimal(7)
