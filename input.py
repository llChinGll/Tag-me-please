# -*- coding: utf-8 -*-

import json	
import httplib

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

def input(tag):
	global flagdic
	data = gethttp(tag)	
	obj = json.loads(data)
	#flagdic = True
	for d in obj[0]["data"]:
		gendic(d["cut"])

def demo():
	j = '[{"tag":"\u0e25\u0e30\u0e04\u0e23\u0e42\u0e17\u0e23\u0e17\u0e31\u0e28\u0e19\u0e4c","data":[{"id":"441","href":"\/topic\/31674804","title":"\u0e21\u0e35\u0e43\u0e04\u0e23\u0e40\u0e04\u0e22\u0e2d\u0e48\u0e32\u0e19\u0e40\u0e23\u0e37\u0e48\u0e2d\u0e07\u0e17\u0e30\u0e40\u0e25\u0e41\u0e1b\u0e23 \u0e02\u0e2d\u0e07 \u0e27.\u0e27\u0e34\u0e19\u0e34\u0e08\u0e09\u0e31\u0e22\u0e01\u0e38\u0e25\u0e1a\u0e49\u0e32\u0e07\u0e04\u0e30","cut":["\u0e2a\u0e23\u0e38\u0e1b","\u0e41\u0e25\u0e49\u0e27","\u0e15\u0e2d\u0e19","\u0e08\u0e1a","\u0e19\u0e32\u0e07\u0e40\u0e2d\u0e01","\u0e22\u0e2d\u0e21","\u0e04\u0e37\u0e19\u0e14\u0e35","\u0e01\u0e31\u0e1a","\u0e1e\u0e23\u0e30\u0e40\u0e2d\u0e01","\u0e21\u0e31\u0e49\u0e22","\u0e04\u0e30","_","\u0e43\u0e19","\u0e19\u0e34\u0e22\u0e32\u0e22","\u0e40\u0e02\u0e35\u0e22\u0e19","\u0e44\u0e27\u0e49","\u0e40\u0e1b\u0e47\u0e19","\u0e1b\u0e23\u0e34\u0e28\u0e19\u0e32","_","\u0e41\u0e15\u0e48","\u0e40\u0e02\u0e49\u0e32\u0e43\u0e08","\u0e27\u0e48\u0e32","\u0e43\u0e19","\u0e25\u0e30\u0e04\u0e23","_","(","\u0e02\u0e2d","_","tag","_","\u0e25\u0e30\u0e04\u0e23","\u0e42\u0e17\u0e23\u0e17\u0e31\u0e28\u0e19\u0e4c","\u0e14\u0e49\u0e27\u0e22","\u0e04\u0e48\u0e30",")","_","\u0e19\u0e32\u0e07\u0e40\u0e2d\u0e01","\u0e40\u0e14\u0e34\u0e19","\u0e08\u0e32\u0e01","\u0e1e\u0e23\u0e30\u0e40\u0e2d\u0e01","\u0e21\u0e32","\u0e44\u0e21\u0e48","\u0e22\u0e2d\u0e21","\u0e04\u0e37\u0e19\u0e14\u0e35","\u0e14\u0e49\u0e27\u0e22","_","\u0e41\u0e15\u0e48","\u0e43\u0e19","\u0e19\u0e34\u0e22\u0e32\u0e22","\u0e1a\u0e23\u0e23\u0e22\u0e32\u0e22","\u0e44\u0e27\u0e49","\u0e27\u0e48\u0e32","\u0e40\u0e14\u0e34\u0e19","\u0e40\u0e04\u0e35\u0e22\u0e07","\u0e01\u0e31\u0e19","\u0e44\u0e1b","_","\u0e1b\u0e25","_","\u0e40\u0e01\u0e25\u0e35\u0e22\u0e14","\u0e1e\u0e23\u0e30\u0e40\u0e2d\u0e01","\u0e40\u0e23\u0e37\u0e48\u0e2d\u0e07","\u0e19\u0e35\u0e49","\u0e21\u0e32\u0e01","_","\u0e2a\u0e38\u0e14","\u0e46\u0e46\u0e46\u0e46","_","\u0e02\u0e2d\u0e07","\u0e04\u0e27\u0e32\u0e21","\u0e40\u0e25\u0e27","_","\u0e2a\u0e07\u0e2a\u0e32\u0e23","\u0e19\u0e32\u0e07\u0e40\u0e2d\u0e01","\u0e21\u0e32\u0e01","_","\u0e40\u0e04\u0e22","\u0e2d\u0e48\u0e32\u0e19","\u0e23\u0e31\u0e01","\u0e40\u0e23\u0e48","_","\u0e1e\u0e23\u0e30\u0e40\u0e2d\u0e01","\u0e2d\u0e38\u0e1a\u0e32\u0e17\u0e27\u0e4c","\u0e1e\u0e2d\u0e01\u0e31\u0e19"],"created_at":{"date":"2014-02-18 18:47:50","timezone_type":3,"timezone":"UTC"}}]}]'

	obj = json.loads(j)[0]
	gendic(obj["data"][0]["cut"])	
	return [obj["data"][0]["cut"]]	
