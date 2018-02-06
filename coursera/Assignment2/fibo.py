#using python3
# to tell the number of lines the recursive code will take to compute nth fibonacii number
a = 2
b = 2
x = 1
y = 1
print('enter range')
n = int(input())
print('n','number of lines','fibonacii value')
for counter in range(0,n):
	c = a+b+3
	z = x+y
	print(counter+2,'        ',c,'          ',z),
	a = b
	b = c
	x = y
	y = z