# Uses python3
import sys

def binary_search(a, x,left,right):
    # write your code here
    while (left<=right):
        mid = (left+right)//2 
        if (a[mid] == x):
            return mid
        else:
            if(a[mid]>x):
                right = mid - 1 
            else:
                left = mid + 1  
    return -1                 


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[n + 1]
    a = data[1 : n + 1]
    for x in data[n + 2:]:		
        print(binary_search(a, x,0,len(a)-1), end = ' ')


