# -*- coding: utf-8 -*-
import sys 
import os
sys.path.append(os.path.abspath("clone-kucut"))
from kucut import SimpleKucutWrapper as KUCut


#f = open('data.in','r')
#data = f.read()
data = raw_input().strip()
myKUCut = KUCut()
result = myKUCut.tokenize([data])
print data
for i in result[0][0]:
	print i.encode('utf-8')
