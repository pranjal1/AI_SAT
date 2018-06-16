# Uses python3
import sys

def compare_and_merge(left, right):
    if not len(left) or not len(right):
        return left or right
    result = []
    i, j = 0, 0
    while (len(result) < len(left) + len(right)):
        if left[i][0] <= right[j][0]:
            result.append(left[i])
            i+= 1
        else:
            result.append(right[j])
            j+= 1
        if i == len(left):
            result.extend(right[j:])
            break
        if j == len(right): 
            result.extend(left[i:])
            break

    return result

def bin_divide(list):
    if len(list) < 2:
        return list

    middle = len(list)//2
    left = bin_divide(list[:middle])
    right = bin_divide(list[middle:])
    return compare_and_merge(left, right)



def fast_count_segments(starts, ends, points):
    cnt = []
    lengthy_list = [[x,'l',0] for x in starts]
    for x in points:
        lengthy_list.append([x,'p',0])
    for x in ends:
        lengthy_list.append([x,'r',0])    
    lengthy_list=bin_divide(lengthy_list)
    val = 0
    dict_soln = {}
    for x in lengthy_list:
        a = x[0]
        b = x[1]
        if(b=='l'):
            val+=1
        elif(b=='r'):
            val-=1
        x[2] = val       
        keys = str(a)+b    
        dict_soln[keys]= x         
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

