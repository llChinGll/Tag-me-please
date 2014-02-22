# -*- coding:utf-8 -*-
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
	#add key val = 1
    print " == train =="
    #for key in KB:
    #	print key + "=" + str(KB[key])
    #KB["แมว"] =1
    return KB
	

