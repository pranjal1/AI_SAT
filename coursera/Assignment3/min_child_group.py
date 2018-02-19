#using python3
import sys


x = [3.2,3.8,4.9,5.8]
n = len(x) -1 
L = 1


num_refills = 0
cur_pos = 0
last_pos = 0
range_left = L

while (cur_pos < n-1):
	while(cur_pos < n and (x[cur_pos+1] - x[last_pos]) <= range_left):		
		range_left -= (x[cur_pos+1] - x[last_pos])
		print x[cur_pos]		
		cur_pos += 1		
		last_pos = cur_pos
	print '======================'			
	num_refills += 1
	range_left = L

print num_refills + 1 


