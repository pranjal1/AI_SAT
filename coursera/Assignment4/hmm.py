# Uses python3
import sys

# sum of values of variable j is answer, figure out the way

def compare_and_merge(left, right):


	return result

def bin_divide(list,cnt):
	if len(list) < 2:
		return list

	middle = len(list)//2
	left,cnt = bin_divide(list[:middle],cnt)
	right,cnt = bin_divide(list[middle:],cnt)
	
	#if not len(left) or not len(right):
	#	return left or right

	result = []
	i, j = 0, 0
	while (len(result) < len(left) + len(right)):
		if left[i] <= right[j]:
			result.append(left[i])
			i+= 1
		else:
			result.append(right[j])
			cnt +=len(left[i:])#this is the most important logic 
			j+= 1
		if i == len(left):
			result.extend(right[j:])
			break
		if j == len(right): 
			result.extend(left[i:])
			break	
	return (result,cnt)

if __name__ == '__main__':
	input = sys.stdin.read()
	data = list(map(int, input.split()))
	a = data[1:]
	n = int(data[0])
	sort_list,cnt = bin_divide(a,0)
	print (cnt)





