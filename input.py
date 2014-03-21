# -*- coding: utf-8 -*-
import sys 
import os
import json	
import httplib
from time import gmtime, strftime
from word import *

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
		w = cutword(d["cut"])
		w = stopword(w)
		gendic(w)
		data.append(w)

	return data

def inputdata():
	#f = open('data.in','r')
	#data = f.read()
	data = raw_input().strip()
	myKUCut = KUCut()
	result = myKUCut.tokenize([data])
	return result[0][0]


def isupdate():
	conn = httplib.HTTPConnection("ml.curve.in.th")
	f = open("log.in",'r')
	time = f.readline()
	f.close()
	
	print "lastupdate:",time
	conn.request("GET", "/update/"+time)
	r1 = conn.getresponse()
	#print r1.status, r1.reason
	data = r1.read()
	conn.close()
	if data == "uptodate":
		return True
	else:
		f = open("log.in",'w')
		time = strftime("%Y-%m-%d %H:%M:%S", gmtime())
		f.write(time)
		f.close()
		return False

