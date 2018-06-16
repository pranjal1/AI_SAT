#using python3
import sys

def max_sub_str(str1,l1,str2,l2,str3,l3):
	table=[]
	table = [[[0 for x in range(0,l2+1)] for y in range(0,l1+1)] for z in range(0,l3+1)]

	for z in range(1,1+l3):
		for x in range(1,l1+1):
			for y in range(1,l2+1):
				if (str1[x-1]==str2[y-1]==str3[z-1]):
					table[z][x][y] = 1+table[z-1][x-1][y-1]
				else:
					table[z][x][y] = max(table[z-1][x][y],table[z][x-1][y],table[z][x][y-1])	
	print(table[z][x][y])



if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    an = data[0]
    data = data[1:]
    a = data[:an]
    data = data[an:]
    bn = data[0]
    data = data[1:]
    b = data[:bn]
    data = data[bn:]
    cn = data[0]
    data = data[1:]
    c = data[:cn]
    max_sub_str(a,len(a),b,len(b),c,len(c))
