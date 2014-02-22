def train(data,dic):
    #data = ['a','a','a','f','g','h','i','i']
    #dic = {'a':1,'b':2,'c':3,'d':4,'e':5}
    KB = {}
    for i in data :
        if dic.has_key(i):
	#update +1
	    val = dic[i]
	    dic[i] = val+1
	else:
	    dic[i] = 1
	#add key val = 1
    print " == train =="
	#some code
	#some code
	#return KB
    KB = dic
    for key in KB:
	print key + "=" + str(KB[key])
    return KB
	

