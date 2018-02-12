#using python3
import sys

x = [0,200,375,550,750,950]
n = 5
L = 400


num_refills = 0
cur_refill = 0
last_refill = 0

while (cur_refill <= n):
	last_refill = cur_refill
	while(cur_refill <=n and (x[cur_refill + 1] - x[last_refill] <= L)):
		cur_refill += 1
	if(cur_refill == last_refill):
		print "Impossible"
		sys.exit(0)
	if (cur_refill <= n):
		num_refills + 1

print num_refills


