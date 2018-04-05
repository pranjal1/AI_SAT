dictlist = [dict() for x in range(2)]
dictlist[0] = {0:1,1:1,2:1,3:1,4:1,5:1}
dictlist[1] = {7:1,8:1,9:1,10:1}
tgt = [1,6,11]
count = [0  for x in range(len(tgt))]
loops = 0
for i in range(len(tgt)):
	for x in dictlist:
		loops+=1
		tmp = x.get(tgt[i])
		if tmp is None:
			tmp = 0
		count[i]+=tmp	

print (count)	
print (loops)




