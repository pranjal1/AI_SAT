#using python3

a = 1
b = 1
print 'enter the value of n'
n = int(raw_input())
print a,b,
for i in range(0,n):
	c = a+b
	print c
	a = b
	b = c
	
