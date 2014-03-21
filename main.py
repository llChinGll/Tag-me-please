# -*- coding: utf-8 -*-

from input import *
from training import *
from query import *

tags = ["อาหาร","สัตว์เลี้ยง","ฟุตบอล","ชีวิตวัยรุ่น","มนุษย์เงินเดือน","ความงาม","หุ้น","เที่ยวต่างประเทศ","การเมือง"]
dic = getdic()
KB = learn(tags)
data = inputdata()
prob = query(KB,data,len(dic))
order = [0,1,2]
swap = True
while swap:
	swap=False
	for i in range(len(prob)-1):
		if prob[i]<prob[i+1]:
			tmp = prob[i]
			prob[i]=prob[i+1]
			prob[i+1] =tmp

			tmp = tags[i]
			tags[i]=tags[i+1]
			tags[i+1] =tmp
			swap = True
			
print "1st : ",tags[0]
print "2nd : ",tags[1]
print "3rd : ",tags[2]
