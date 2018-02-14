#using python3
import sys

x = [0,200,375,550,750,950]
n = 5
L = 400


num_refills = 0
cur_pos = 0
last_pos = 0
range_left = L

while (cur_pos < n-1):
	while(cur_pos < n and (x[cur_pos+1] - x[last_pos]) <= range_left):		
		range_left -= (x[cur_pos+1] - x[last_pos])		
		cur_pos += 1		
		last_pos = cur_pos
			
	if((x[cur_pos+1] - x[last_pos]) > L):
		print 'cannot move forward from position ',cur_pos 
		sys.exit(0)	
	print 'Stop @ ',cur_pos,x[cur_pos]
	num_refills += 1
	range_left = 400

print num_refills


