#using python3
#smart idea for computing last digit of nth fibonacii number, only use unit dit in calculation
n1 = 0
n2 = 1
lim = int(input())
if(lim==0):
	print(n1)
elif(lim==1):
	print(n2)
else:
	for counter in range(1,lim):
		sum = (n1+n2)%10
		n1 = n2%10
		n2 = sum
	print(sum)

