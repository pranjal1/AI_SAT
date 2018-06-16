#using python3

def compute_change(denominations,num_of_dens,n):
	table=[[0 for x in range(n+1)] for x in range(num_of_dens)]
	for x in range(n+1):
		table[0][x] = x

	for i in range(1,num_of_dens):
		for j in range(1,n+1):
			print(i,j)
			if j<denominations[i]:
				table[i][j] = table[i-1][j]
				print("haha")
			else:
				table[i][j] = min(table[i-1][j],1+table[i][j-denominations[i]])
			#print(table[i][j],end = " ")
		#print('\n')
	print(table)				

compute_change([1,3,4],3,10)
