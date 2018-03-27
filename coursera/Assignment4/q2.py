# Uses python3
import sys

def get_majority_element(a,n):
	count_arr={}
	for i in a:
		count_arr[i] = 0
	for i in a:
		count_arr[i] += 1
	for i in a:
		if(count_arr[i] > n):
			return 0		
	return -1



if __name__ == '__main__':
	input = sys.stdin.read()
	data = input.split()
	a = data[1:]
	n = int(data[0])
	if get_majority_element(a,n/2) != -1:
		print(1)
	else:
		print(0)
