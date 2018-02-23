#using python3
#change the print and return statement for python3

amt = int(input())

val1 =1
val2 =5
val3 =10
change = 0

if(amt>=val3):
	temp=amt//val3
	change+=temp
	amt-=temp*val3

if(amt>=val2):
	temp=amt//val2
	change+=temp
	amt-=temp*val2

if(amt>=val1):
	change+=amt

print (change)	
	
		
		
		 
