#using python3
#finding the product of the largest two numbers using the quick sort technique
#firstly, trying to successfully implement quick sort


#this function sorts the array in the given low to high limit
def partition_sorter(arr,low,high):
    pivot = arr[high]
    index = low-1    
    for counter in range(low,high+1):
        if (arr[counter]<=pivot):
            index+=1
            arr[counter],arr[index] = arr[index],arr[counter]
            
    return index


def quick_sort(arr,low,high):
    if low < high:
        pi = partition_sorter(arr,low,high)
        #in every recursion, both of the below 
        #functions are called by the above
        #if condition restricts the unnecessary one
        quick_sort(arr,low,pi-1)
        quick_sort(arr,pi+1,high)
        
#arr = [5]*996 
arr = []   
for i in range(0,1000):
	arr.append(1000-i) 
print (arr)	
quick_sort(arr,0,len(arr)-1)
for x in arr:
    print (x,end=' ')
  
    
