#Uses python3

import sys

def partition_sorter(arr,low,high):
    pivot = arr[high]
    index = low-1    
    for counter in range(low,high+1):
        if (arr[counter]>=pivot):
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

 



def max_dot_product(a, b):
    #write your code here
    a = quick_sort(a,0,len(a)-1)
    b = quick_sort(b,0,len(b)-1)
    res = 0
    for i in range(len(a)):
        res += a[i] * b[i]
    return res

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    a = data[1:(n + 1)]
    b = data[(n + 1):]
    print(max_dot_product(a, b))
    
