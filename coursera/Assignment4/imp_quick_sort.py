#using python3
import sys

def partition_sorter(arr,low,high):
    pivot = arr[high]
    index = low-1    
    for counter in range(low,high+1):
        if (arr[counter]<=pivot):
            index+=1
            arr[counter],arr[index] = arr[index],arr[counter]
         
    return index


def quick_sort(arr,low,high):
    #print(arr,low,high)
    if low < high:
        pi = partition_sorter(arr,low,high)
        #in every recursion, both of the below 
        #functions are called by the above
        #if condition restricts the unnecessary one
        quick_sort(arr,low,pi-1)
        quick_sort(arr,pi+1,high)


#arr = [5]*100000
if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    dict_arr = {}
    for x in a:
        try:
            dict_arr[str(x)] +=1
        except KeyError:
            dict_arr[str(x)] = 1# made into string because python was sorting keys by default
    arr = []
    for x in dict_arr.keys():
        arr.append(int(x)) 
    quick_sort(arr,0,len(arr)-1)
    for x in arr:
        for y in range(0,dict_arr[str(x)]):
            print (x,end=' ')

