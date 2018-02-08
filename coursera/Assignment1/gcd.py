#using python3
print 'enter the first number'
num1 = int(raw_input())
print 'enter the second number'
num2  = int(raw_input())
if num1 < num2:
	num1,num2 = num2,num1

print num1,num2
gcd = 0

for i in range(1,num2+1):
	remainder1 = num1 % i
	remainder2 = num2 % i
	if(remainder1 == 0 and remainder2 == 0 and i > gcd):
		gcd = i

print 'gcd is : ', gcd
print 'lcm is : ', (num1*num2)/gcd
