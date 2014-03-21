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

def openfile(permiss):
	try:
		f = open("train.in",permiss)
	except IOError:
		f = open("tagmeplease/train.in",permiss)
	return f
	
def closefile(f):
	f.close()

def getKB():
	f = openfile("r")
	l = 0
	c = 0
	KB = []
	for line in f:
		sp = line.split(":")
		if c ==0:
			for i in sp:
				KB.append({})
				l+=1
		else:
			key = sp[l].strip()
			for i in range(l):
				KB[i][key] = int(sp[i])
			gendic([key])
		c+=1
	#print l			
	closefile(f)
	return KB

def learn(tags):
	
    if isupdate():
       print "uptodate"
       return getKB()

    f = openfile("w")
    f.write(":".join(tags)+"\n")

    data = {}
    for t in tags:
       print "=== get traininput ",t," ==="
       data[t] = inputtrain(t)
    dic = getdic()

    ss = {}
    for i in dic:
		ss[i] = ""

    KB = []
    for t in tags:
        print "=== train ",t," ==="
        #print data[t]
        KBval = train(data[t],dic)
        for k,v in KBval.items():
           ss[k]+= str(v)+":"
        KB.append(KBval)
   
    for i in dic:
		ss[i] += i
		f.write(ss[i].encode('utf-8')+"\n")

    closefile(f)

    return KB
	

