#-*- coding:utf-8 -*-
from word import *
def query(kblist,datalist,vocab):
	s=""
	for i in datalist:
		s += " "+i 
	#print s
	doclen = len(datalist)
	print "doclen=", doclen
	datadict = {}
	#datalist = cutword(datalist)
	#datalist = stopword(datalist)
	for i in datalist:
		i = i.encode('utf-8')
		if datadict.has_key(i):
			tmp = datadict.get(i)
			upd = { i:tmp+1 }
			datadict.update(upd)
		else: 
			upd = { i:1 }
			datadict.update(upd)

	allprob = []
	cc = 0
	for class_dict in kblist:
		prob = 1.0
		total = len(class_dict.keys())+0.01*vocab
		for key_in_class in datadict.keys():
			print key_in_class
			#key_in_class = key_in_class.encode('utf-8')
			class_val = class_dict[key_in_class]
			prob = prob*(class_val+0.01)*((datadict[key_in_class]+0.1)/(doclen+1))/total
			#prob = prob*(class_val+0.1)/total
		allprob.append(prob)
		cc+=1
	norm = sum(allprob)
	#print allprob
	for i in range(len(allprob)):
		allprob[i] = allprob[i]/norm
	#print norm,allprob
	return allprob
