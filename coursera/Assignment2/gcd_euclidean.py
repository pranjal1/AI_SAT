#using python3
#uses recursion

import time

def gcd_euclidean(a,b):
	if (b == 0):
		return a
	else:
		a_dash = a % b
		ans=gcd_euclidean(b,a_dash)
		return ans


st_time = time.time()		
print('enter the 1st number')	
num1 = int(input())
print('enter the 2nd number')	
num2 = int(input())
gcd = gcd_euclidean(num1,num2)
print ('GCD is : ',gcd)
print( time.time() - st_time)