#using python3
import sys

def optimal_weight(W, w, n):
	table = [[0 for x in range(0,W+1)] for y in range(0,n+1)]
	for i in range(1,n+1):
		for j in range(1,W+1):
			if(j<w[i-1]):
				table[i][j] = table[i-1][j]
			else:
				table[i][j] = max(table[i-1][j],table[i-1][j-w[i-1]]+w[i-1])
	print(table[i][j])

if __name__ == '__main__':
	input = sys.stdin.read()
	W, n, *w = list(map(int, input.split()))
	optimal_weight(W, w,n)
