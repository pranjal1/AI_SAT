#Uses python3

import sys

def largest_number(a):
	#write your code here
	res = ""
	for x in a:
		res += x
	return res


def get_MSB(n):
        while(1):
                rem = n//10
                if (rem==0):
                        return n
                n=rem

if __name__ == '__main__':
	input = sys.stdin.read()
	data = input.split()
	a = data[1:]
	print (a)
	print(largest_number(a))
    




