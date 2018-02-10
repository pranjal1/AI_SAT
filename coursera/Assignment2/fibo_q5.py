#using python3

def fibo_compute(n):
	a = 0
	b = 1
	sum = 0
	if (n == 0):
		return 0
	if (n == 1):
		return 1
	else:
		for counter in range(1,n):
			sum = a + b
			a = b
			b = sum
		return sum

inputs = raw_input()
token = inputs.split()
n = int(token[0])
m = int(token[1])
fib_arr = []
fib_arr.append(0)
fib_arr.append(1)
i = 2 
rem1 = 10
while(1):
	hmm = fibo_compute(i)
	rem = hmm % m
	if (rem == 0):	
		rem1 = fibo_compute(i+1)%m
		if(rem1 == 1):
			break
	fib_arr.append(rem)
	i+=1
rep = i
print(fib_arr[n % rep])


