# Uses python3
import sys


def partition_sorter(arr,low,high):
    pivot = arr[high]
    index = low-1    
    for counter in range(low,high+1):
        if (arr[counter][0]<pivot[0]):
            index+=1
            arr[counter],arr[index] = arr[index],arr[counter]
        if (arr[counter][0]==pivot[0]):
            index+=1
            arr[counter],arr[index] = arr[index],arr[counter]
            if ((arr[counter][1] == 'r' and pivot[1] == 'l') or (arr[counter][1] == 'p' and pivot[1] == 'l') or (arr[counter][1] == 'r' and pivot[1] == 'p')):
                print('haha')
                arr[counter][1],arr[index][1] = arr[index][1],arr[counter][1]           
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

def fast_count_segments(starts, ends, points):
    cnt = []
    lengthy_list = [[x,'l',0] for x in starts]
    for x in ends:
        lengthy_list.append([x,'r',0])
    for x in points:
        lengthy_list.append([x,'p',0])    
    quick_sort(lengthy_list,0,len(lengthy_list)-1)
    print(lengthy_list)
    val = 0
    dict_soln = {}
    for x in lengthy_list:
        a = x[0]
        b = x[1]
        x[2] = val
        if(b=='l'):
            val+=1
        elif(b=='r'):
            val-=1
        keys = str(a)+b    
        dict_soln[keys]= x 
    print(dict_soln)         
    for x in points:
        cnt.append(dict_soln[str(x)+'p'][2])    
    return cnt
    

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[1]
    starts = data[2:2 * n + 2:2]
    ends   = data[3:2 * n + 2:2]
    points = data[2 * n + 2:]
    #use fast_count_segments
    cnt = fast_count_segments(starts, ends, points)
    for x in cnt:
        print(x, end=' ')

