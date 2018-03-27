#Uses python3

import sys
import math

def partition_sorter(arr,low,high):
    pivot = arr[high][0]
    index = low-1    
    for counter in range(low,high+1):
        if (arr[counter][0]>=pivot):
            index+=1
            arr[counter],arr[index] = arr[index],arr[counter]
            
    return index


def quick_sort(arr,low,high):
    if low < high:
        pi = partition_sorter(arr,low,high)
        #in every recursion, both of the below 
        #functions are called by the above
        #if condition restricts the unnecessary one
        arr=quick_sort(arr,low,pi-1)
        arr=quick_sort(arr,pi+1,high)
    return (arr)

if __name__ == '__main__':
	data = list(map(int, sys.stdin.read().split()))
	a = data[1:]
	max_val = max(a)
	p_val=(int(math.log10(max_val))+1)
	unpadded_data = [[x,int(math.log10(x))+1] for x in a]
	padded_data = [[int(str(x[0]).ljust(p_val, '9')),x[1]] for x in unpadded_data]
	temp_ans = quick_sort(padded_data,0,len(padded_data)-1)
	padded_rem = [x[0]//(10**(p_val-x[1])) for x in padded_data]
	ans=''
	for i in padded_rem:
		ans+=str(i)
	print(int(ans))
