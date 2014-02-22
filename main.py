# -*- coding: utf-8 -*-

from input import *
from training import *
from query import *

tags = ["อาหาร","สัตว์เลี้ยง","ฟุตบอล","ชีวิตวัยรุ่น","มนุษย์เงินเดือน","ความงาม","หุ้น","เที่ยวต่างประเทศ","การเมือง"]
data = {}
for t in tags:
	print "=== input ",t," ==="
	data[t] = input(t)
dic = getdic()

KB = []
for t in tags:
	print "=== process ",t," ==="
	#print data[t]
	KB.append(train(data[t],dic))

for k,v in KB[5].iteritems():
	if v!=0:
		print k," => ",v
query(KB,[dic[1]],len(dic))

dm = demo()
train(dm,dic)

