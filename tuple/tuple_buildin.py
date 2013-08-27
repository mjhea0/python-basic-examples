#coding:utf-8

t = (['xyz', 123], 23, -103.4)
print str(t) #(['xyz', 123], 23, -103.4)
print len(t) #3
print max(t) #['xyz', 123]
print min(t) #-103.4
print cmp(t, (['xyz', 123], 23, -103.4, 'free', 'easy')) #-1
print list(t) #[['xyz', 123], 23, -103.4]
