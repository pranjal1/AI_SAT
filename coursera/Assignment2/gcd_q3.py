#using python3

def gcd_compute(a,b):
	if (b==0):
		return a 
	else:
		c = a % b
		ans = gcd_compute(b, c)
		return ans


ip = input() #change this to input() before submission
tokens = ip.split()
num1 = int(tokens[0])
num2 = int(tokens[1])
print (gcd_compute(num1,num2))
