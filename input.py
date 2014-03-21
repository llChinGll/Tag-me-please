# -*- coding: utf-8 -*-
import sys 
import os
import json	
import httplib

sys.path.append(os.path.abspath("../clone-kucut"))
sys.path.append(os.path.abspath("clone-kucut"))
from kucut import SimpleKucutWrapper as KUCut

dic=[]
flagdic= True

def gendic(data):
	global dic,flagdic
	for i in data:
		if not i in dic:
			dic.append(i)
			#if flagdic:
			#	flagdic = False
			#	print i

def getdic():
	global dic
	return dic
 	
def gethttp(d):
	conn = httplib.HTTPConnection("ml.curve.in.th")
	conn.request("GET", "/json/"+d)
	r1 = conn.getresponse()
	#print r1.status, r1.reason
	data = r1.read()
	conn.close()
	return data

def inputtrain(tag):
	global flagdic
	data = gethttp(tag)	
	obj = json.loads(data)
	#flagdic = True
	data = []
	for d in obj[0]["data"]:
		gendic(d["cut"])
		data.append(d["cut"])
	return data

def inputdata():
	#f = open('data.in','r')
	#data = f.read()
	data = raw_input().strip()
	myKUCut = KUCut()
	result = myKUCut.tokenize([data])
	return result[0][0]
