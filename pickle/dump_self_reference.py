#coding:utf-8

try:  
    import cPickle as pickle  
except ImportError:  
    import pickle

#pickle可以解决自引用问题
#marshal会出问题

list = [1]
list.append(list)

str = pickle.dumps(list)
print str

load_list = pickle.loads(str)
print load_list
print type(load_list)
