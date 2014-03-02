# -*- coding: utf-8 -*-
def cutword(data):
	#textx = [" กขค","เจี๊ยบ "]
	#text = [" abc","def "]
	data_edit = []
	for i in data:
		a=i.strip()
		a=a.strip('-')
		a=a.strip('/')
		a=a.strip('*')
		a=a.strip('=')
		a=a.strip('+')
		a=a.strip('#')
		data_edit.append(a)
		#print i
	return data_edit