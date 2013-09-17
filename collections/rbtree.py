import rbtree

class Post:
    def __init__(self):
        self.time = 1
        
    def __cmp__(self, other):
        print 'called'
        return self.time < other.time
        
    def __str__(self):
        return 'ptime ' + str(self.time)
        
        
r = rbtree.rbtree()

p1 = Post()
p1.time += 1
p2 = Post()
p3 = Post()

r[p1] = p1
r[p2] = p2

print '-----------'

for x in r:
    if x >= p1:
        print x