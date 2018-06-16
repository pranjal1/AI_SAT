import itertools
import sys
import random


def edit_distance(str1,l1,str2,l2):
	#print(str1,str2,l1,l2)
	if(l1 == -1 or l2 == -1):
		return 0
	elif(str1[l1] == str2[l2]):
		return(1+edit_distance(str1,l1-1,str2,l2-1))
	else:
		return(max(edit_distance(str1,l1-1,str2,l2),edit_distance(str1,l1,str2,l2-1)))	


def list_of_combs(arr):
    """returns a list of all subsets of a list"""
    
    combs = []
    for i in range(0, len(arr)+1):
        listing = [list(x) for x in itertools.combinations(arr, i)]
        combs.extend(listing)
    return combs


for x in range(0,1000):
	print(x)
	a=[]
	for x in range(0,10):
		a.append(random.randint(0,1000))

	b=[]

	for x in range(0,10):
		b.append(random.randint(0,1000))

		
	l1 = list_of_combs(a)
	l2 = list_of_combs(b)
	maxi = 0
	for x in l1:
		for y in l2:
			if(x==y):
				if(len(x)>maxi):
					maxi=len(x)
	if(maxi!=edit_distance(a,len(a)-1,b,len(b)-1)):				
		print(a,b)

