#coding:utf-8

import os 
for k, v in os.environ.items():
    print "%s=%s" % (k, v) 
print "\n".join(["%s=%s" % (k, v) for k, v in os.environ.items()])
