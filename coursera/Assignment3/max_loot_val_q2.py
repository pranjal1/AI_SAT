# Uses python3
import sys



def partition_sorter(arr,low,high):
    pivot = arr[high][2]
    index = low-1    
    for counter in range(low,high+1):
        if (arr[counter][2]>=pivot): #for descending order
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



def get_optimal_value(capacity, weights, values):
    value = 0.
    i = 0
    val_per_wt = [(x,y,x/y) for x, y in zip(values, weights)]
    val_per_wt = quick_sort(val_per_wt,0,len(val_per_wt)-1)
    counter = len(val_per_wt)
    while(counter>0):

	    if (val_per_wt[i][1] <= capacity):
	        capacity -= val_per_wt[i][1]
	        value += val_per_wt[i][0]
	    else:
	    	value += capacity*val_per_wt[i][2]
	    	capacity = 0
	    i+=1 
	    counter-=1
#	    print (i,counter)

    return value


if __name__ == "__main__":
	data = list(map(int, sys.stdin.read().split()))
	n, capacity = data[0:2]
	values = data[2:(2 * n + 2):2]
	weights = data[3:(2 * n + 2):2]

	opt_value = get_optimal_value(capacity, weights, values)
	print("{:.10f}".format(opt_value))

    	    		
	
