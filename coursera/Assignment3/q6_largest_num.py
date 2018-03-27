#Uses python3

import sys


def IsGreaterOrEqual(digit, maxDigit):
	temp1 = str(digit)+str(maxDigit)
	temp2 = str(maxDigit)+str(digit)
	if (int(temp1) >= int(temp2)):
		return True
	return False
	

if __name__ == '__main__':
	data = list(map(int, sys.stdin.read().split()))
	a = data[1:]
	ans = ''
	while (len(a)!=0):
		maxDigit = 0
		for digit in a:
			if (IsGreaterOrEqual(digit,maxDigit)):
				maxDigit = digit
		ans+=str(maxDigit)
		a.remove(maxDigit)
	
	print(ans)
	



