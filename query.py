
def query(kblist,datalist,vocab):
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
	for class_dict in kblist:
		prob = 1
		total = len(class_dict.keys())+vocab
		for key_in_class in datadict.keys():
			class_val = class_dict.get(key_in_class)
			prob = prob*(class_val+1)/total
		allprob.append(prob)
	norm = 0
	for i in allprob:
		norm = norm + i
	for i in allprob:
		i = i/norm
