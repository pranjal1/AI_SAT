#using python3
import sys

def edit_distance(str1,l1,str2,l2):
	if(l1 == -1 or l2 == -1):
		return 0
	elif(str1[l1] == str2[l2]):
		return(1+edit_distance(str1,l1-1,str2,l2-1))
	else:
		return(max(edit_distance(str1,l1-1,str2,l2),edit_distance(str1,l1,str2,l2-1)))
	


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
	print(edit_distance(a,len(a)-1,b,len(b)-1))
