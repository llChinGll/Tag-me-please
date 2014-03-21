# -*- coding:utf-8 -*-
from input import *
def train(data,dic):
    #data = ['a','a','a','f','g','h','i','i']
    #dic = {'a':1,'b':2,'c':3,'d':4,'e':5}
    KB = {}
    for i in dic:
	   KB[i]=0
    #print data
    for d in data:
    	for i in d:
	#print i
		  val = KB[i]
		  KB[i] = val+1
    return KB

def learn(tags):
    data = {}
    for t in tags:
       print "=== get traininput ",t," ==="
       data[t] = inputtrain(t)
    dic = getdic()

    KB = []
    for t in tags:
        print "=== train ",t," ==="
        #print data[t]
        KB.append(train(data[t],dic))
        
    return KB
	

