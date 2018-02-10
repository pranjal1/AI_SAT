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

n =input()
tokens = n.split()
n1 = int(tokens[0])%60
n2 = int(tokens[1])%60
sum = 0
for i in range(n1,n2+1):
	x = fibo_compute(i)%10
	sum = (sum + x)%10
	


print(sum)






