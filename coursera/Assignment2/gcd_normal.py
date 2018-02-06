#using python3
import time

st_time = time.time()
print('enter 1st number : ')
num1 = int(input())
print('enter 2nd number : ')
num2 = int(input())
gcd = 1

if num2>num1:
	num1,num2 = num2,num1
for counter in range(1,num2+1):
	if (num1%counter == 0 and num2%counter == 0 and counter > gcd):
		gcd = counter
		
print('the GCD is : ')
print(gcd)		
print(time.time() - st_time)
		
#5
#2
#n_larger+1 * 2 (WCS)

#O(2*n_larger+9)