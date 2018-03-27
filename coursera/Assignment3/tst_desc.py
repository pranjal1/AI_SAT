def partition_sorter3(arr,low,high):
    print (arr)
    pivot = arr[high][1]
    index = low-1    
    for counter in range(low,high+1):
        if (arr[counter][1]>=pivot):
            index+=1
            arr[counter],arr[index] = arr[index],arr[counter]
            
    return index


def quick_sort3(arr,low,high):
    if low < high:
        pi = partition_sorter3(arr,low,high)
        #in every recursion, both of the below 
        #functions are called by the above
        #if condition restricts the unnecessary one
        arr=quick_sort3(arr,low,pi-1)
        arr=quick_sort3(arr,pi+1,high)
    return (arr)

a=[[9, 9], [91, 9], [14, 1], [13, 1], [12, 1], [917, 9]]
print (a)
b=quick_sort3(a,0,len(a)-1)
print(b)

