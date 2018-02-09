#using python3

def lcm_compute(a,b):
        if (b==0):
                return a
        else:
                a_dash = a % b
                ans = lcm_compute(b,a_dash)
                return ans



ip = input() #change for python3
token = ip.split()
num1 = int(token[0])
num2 = int(token[1])
print (int(num1*num2)//lcm_compute(num1,num2)) #// means to discard the remainder

#5/2 = 2.5 and 5//2 = 2
#here // is used because the product of num1 and num2 is large and produces unexpected results

