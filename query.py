#-*- coding:utf-8 -*-
def query(kblist,datalist,vocab):
	s=""
	for i in datalist:
		s += " "+i 
	#print s
	datadict = {}
	for i in datalist:
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
		total = len(class_dict.keys())+vocab
		for key_in_class in datadict.keys():
			key_in_class =  key_in_class.encode('utf-8')
			class_val = class_dict[key_in_class]
			prob = prob*(class_val+1)/total
		allprob.append(prob)
		cc+=1
	norm = sum(allprob)
	#print allprob
	for i in range(len(allprob)):
		allprob[i] = allprob[i]/norm
	#print norm,allprob
	return allprob
