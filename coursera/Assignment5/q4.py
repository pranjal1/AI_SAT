#using python3
import sys

def max_sub_str(str1,l1,str2,l2):
	table=[]
	table = [[0 for x in range(0,l2+1)] for y in range(0,l1+1)]
	for x in range(1,l1+1):
		for y in range(1,l2+1):
			if (str1[x-1]==str2[y-1]):
				table[x][y] = 1+table[x-1][y-1]
			else:
				table[x][y] = max(table[x-1][y],table[x][y-1])	
    
	print(table[x][y])

if __name__ == '__main__':
	input = sys.stdin.read()
	data = list(map(int, input.split()))

	n = data[0]
	data = data[1:]
	a = data[:n]

	data = data[n:]
	m = data[0]
	data = data[1:]
	b = data[:m]
	max_sub_str(a,len(a),b,len(b))

