#using python3
import sys

def evalt(a, b, op):	
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    else:
        assert False


def MinandMax(i,j,table_max,table_min,operands):
	min_val = 100000000
	max_val = -100000000
	
	for k in range(i,j):
		a = evalt(table_max[i][k],table_max[k+1][j],operands[k-1])
		b = evalt(table_max[i][k],table_min[k+1][j],operands[k-1])
		c = evalt(table_min[i][k],table_max[k+1][j],operands[k-1])
		d = evalt(table_min[i][k],table_min[k+1][j],operands[k-1]) 
		min_val = min(a,b,c,d,min_val)
		max_val = max(a,b,c,d,max_val)
	return(min_val,max_val)

def get_maximum_value(numbers,operands):
	n = len(numbers)
	table_max = [[0 for x in range(0,n+1)] for y in range(0,n+1)]
	table_min = [[0 for x in range(0,n+1)] for y in range(0,n+1)]
	for i in range(1,n+1):
		table_max[i][i],table_min[i][i] = numbers[i-1],numbers[i-1]
	
	for s in range(1,n):
		for i in range(1,n-s+1):
			j=i+s
			table_min[i][j],table_max[i][j] = MinandMax(i,j,table_max,table_min,operands)
	
	print(table_max[1][n])


if __name__ == "__main__":
	input = sys.stdin.read()
	counter = 0
	numbers=[]
	operands=[]
	for val in input:
		if counter%2==0:
			numbers.append(int(val))
		else:		
			operands.append(val)
		counter+=1
	get_maximum_value(numbers,operands[:len(operands)-1])
	
	
		
