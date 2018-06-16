#using python3
import sys

def edit_distance(str1,str2):
	rows = len(str1)+1
	cols = len(str2)+1
	table = [[0 for x in range(0,cols)] for y in range(0,rows)]
	for x in range(0,rows):
		table[x][0]=x
	for x in range(0,cols):
		table[0][x]=x
	
	for x in range(1,rows):
		for y in range(1,cols):
			if(str1[x-1] == str2[y-1]):
				table[x][y] = table[x-1][y-1]
			else:
				table[x][y] = min(1+table[x-1][y-1],1+table[x-1][y],1+table[x][y-1])	
	print(table[x][y])
	

if __name__ == '__main__':
	input = sys.stdin.read()
	data = list(input.split())
	#print(data[0],data[1])
	edit_distance(data[0],data[1])
