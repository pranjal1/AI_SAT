#using python3
import sys
import math

def main_function(n):
	comp_var1=0
	comp_var2=0
	table = [[0 for x in range(0,n+1)] for y in range(0,3)]
	for x in range(0,n+1):
		table[0][x]=x
	for i in range(2,n+1):
		comp_var1 = table[2][int(i/2)] if (math.floor(i/2) == i/2) else 10000000000
		comp_var2 = table[2][int(i/3)] if (math.floor(i/3) == i/3) else 10000000000
		min_val = min(table[2][i-1],comp_var1,comp_var2)
		if (min_val == table[2][i-1]):
			table[1][i] = table[0][i-1]
		elif (min_val == comp_var1):
			table[1][i] = table[0][int(i/2)]
		else:
			table[1][i] = table[0][int(i/3)]	
		table[2][i] = 1+min_val

	stop_var = table[1][n]
	stack_ans = []
	stack_ans.append(n)
	while(stop_var!=0):
		stack_ans.append(table[0][stop_var])
		stop_var = table[1][stop_var]
	print(len(stack_ans)-1)
	for x in reversed(stack_ans):
		print(x,end=" ")

if __name__ == '__main__':
	input = sys.stdin.read()
	main_function(int(input))
