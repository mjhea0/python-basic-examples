#coding:utf-8

import os 

dirname = r'/tmp/'
print os.listdir(dirname)        

[f for f in os.listdir(dirname) 
    if os.path.isfile(os.path.join(dirname, f))]    

[f for f in os.listdir(dirname) 
    if os.path.isdir(os.path.join(dirname, f))]
