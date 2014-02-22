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
	KB.append(train(data[t],dic))

query(KB,["แมว","กิน","ข้าว","ของ","ฉัน","ไป","มาก"],len(dic))

dm = demo()
train(dm,dic)

