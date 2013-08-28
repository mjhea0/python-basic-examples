#coding:utf-8

import os 
import glob 

os.listdir(r'/tmp/')       

print glob.glob(r'/tmp/*.txt')
print glob.glob(r'/tmp/*.sock')
