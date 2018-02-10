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


mother = [(0,0)]
sum = 0
for i in range(0,60):
	x = fibo_compute(i)%10
	sum = (sum + x)%10
	mother.append((x,sum))

tot = sum	

n =int(input())
print ((n//60)*tot + mother[n%60+1][1])






