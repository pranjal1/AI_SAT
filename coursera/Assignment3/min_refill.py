#using python3
import sys

x = [0,200,375,550,750,950]
n = 5
L = 400


num_refills = 0
cur_pos = 0
last_pos = 0
range_left = 400

while (cur_pos < n):
	last_pos = cur_pos
	while(cur_pos <n and (x[cur_pos + 1] - x[last_pos] <= range_left)):
		range_left -= (x[cur_pos + 1] - x[last_pos])
		print range_left
		cur_pos += 1
		if(cur_pos == last_pos):
			print "Impossible"
			sys.exit(0)
	
	num_refills + 1
	range_left = 400

print num_refills


