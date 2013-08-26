#coding:utf-8

age = 12
assert age >= 12, 'Children under the age of 12 are not allowed'

age = 10 
assert 0 < age < 100 
age = -1 
assert 0 < age < 100 

'''没有往下面执行了'''

print 'here...'

assert 1 == 1
assert 2 + 2 == 2 * 2
assert len(['my list', 12]) < 10
assert range(3) == [0, 1, 2]
assert 1 == 0
assert 1 == 0, 'One does not equal zero silly!'
