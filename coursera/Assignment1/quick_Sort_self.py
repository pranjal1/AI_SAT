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
        print(arr)
        print(low,pi-1,pi+1,high)
        quick_sort(arr,low,pi-1)
        quick_sort(arr,pi+1,high)
        
array = [4,4,1,2,2,5,9,4]      
quick_sort(array,0,len(array)-1)
  
    

