#coding:utf-8

from collections import deque

q = deque(range(5))
q.append(5)
q.appendleft(6)

#deque([6, 0, 1, 2, 3, 4, 5])
print q

#5
print q.pop()

#6
print q.popleft()

#None
print q.rotate(3)

#deque([2, 3, 4, 0, 1])
print q

#None
print q.rotate(-1)

#deque([3, 4, 0, 1, 2])
print q
