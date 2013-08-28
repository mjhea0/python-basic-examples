#coding:utf-8

class counter: 
    count = 0                            
    def __init__(self): 
        self.__class__.count += 1             

counter 
print counter.count                                
c = counter() 
print c.count                                        
print counter.count 
d = counter()                                    
print d.count 
print c.count 
print counter.count
