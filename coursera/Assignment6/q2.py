#using python3
import sys

def optimal_weight(W, w, n):
	table = [[0 for x in range(0,W+1)] for y in range(0,n+1)]
	for i in range(1,n+1):
		for j in range(1,W+1):
			if(j == w[i-1] or ((j-w[i-1])>0 and table[i-1][j-w[i-1]] != 0)):
				if (table[i-1][j] == 0):
					table[i][j] = 1
				else:
					table[i][j] = 2 
			else:
				table[i][j] = table[i-1][j]
	if(table[i][j] == 2):
		print(1)
	else:
		print(0)

if __name__ == '__main__':
	input = sys.stdin.read()
	n, *w = list(map(int, input.split()))
	W = sum(w)
	if(W%3 != 0 or len(w)<3):
		print(0)
	else:
		optimal_weight(int(W/3), w,n)

#logic here:
#1. calculating the number of ways to reach a sum (given by value of j) from (0 to W/3) using dynamic programming.
#2. if value of j is equal to the w[i-1] i.e the element in w is exactly equal to the sum then we add the value in cell until 2.
#3. if value of table[i-1][j-w[i-1]] != 0 means that if we add this element i.e w[i-1] to the previous sum table[i-1][j-w[i-1]], we get the current sum
#4. if not both the case copy previous cell, (previous means top not left); we are scanning the table in top down approach.
