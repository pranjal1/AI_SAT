#using python3
import sys

def compute_change(denominations,n,no_terms):
	table = [[0 for x in range(0,no_terms+1)] for y in range(0,n)]
	for x in range(0,no_terms+1):
		table[0][x] = x
	for i in range(1,n):
		for j in range(0,no_terms+1):
			if(j<denominations[i]):
				table[i][j]=table[i-1][j]
			else:
				table[i][j]=min(table[i-1][j],1+table[i][j-denominations[i]])#cool logic
	print(table[i][j])

if __name__ == '__main__':
	input = sys.stdin.read()
	compute_change([1,3,4],3,int(input))

