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
        arr=quick_sort(arr,low,pi-1)
        arr=quick_sort(arr,pi+1,high)
    return (arr)

array = [24,3.8,14,4.9,5.8,55,9.7,17.8,22,17.9,18.0,22,22.2,3.2]      
x = quick_sort(array,0,len(array)-1)
print (x)  
    


#x = [3.2,3.8,4.9,5.8,9.7,17.8,17.9,18.0,22,22.2,24]


n = len(x) - 1

L = 2 # max age gap of clildrens




num_groups = 1
cur_pos = 0
last_pos = 0



while (cur_pos <= n):
	while(cur_pos < n   and (x[cur_pos] - x[last_pos]) <= L):
		cur_pos += 1
		
		if((x[cur_pos] - x[last_pos]) > L):
			num_groups += 1
			
	last_pos = cur_pos
	cur_pos += 1


print ('the minimum number of groups are',num_groups)


