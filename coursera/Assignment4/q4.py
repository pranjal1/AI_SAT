# Uses python3
import sys


# sum of values of variable j is answer, figure out the way

def naive_way(arr):
	i = 0
	j=0
	x = 0
	arr1 = arr
	for i in range(0,len(arr)):
		for j in range(i,len(arr)):
			#print (arr)
			if arr1[i]>arr1[j]:
				arr1[i],arr1[j] = arr1[j],arr1[i] 
				x+=1
	return x

def compare_and_merge(left, right,num_invs):
	if not len(left) or not len(right):
		return left or right
	result = []
	i, j = 0, 0
	var1 = len(left)
	while (len(result) < len(left) + len(right)):
		if left[i] <= right[j]:
			result.append(left[i])
			i+= 1
		else:
			result.append(right[j])
			num_invs +=(var1-i)#this is the most important logic 
			j+= 1
		if i == len(left):
			result.extend(right[j:])
			break
		if j == len(right): 
			result.extend(left[i:])
			break

	return (result,num_invs)

def bin_divide(list,num_invs):
	if len(list) < 2:
		return list,num_invs

	middle = len(list)//2
	left,num_invs = bin_divide(list[:middle],num_invs)
	right,num_invs = bin_divide(list[middle:],num_invs)
	return (compare_and_merge(left, right,num_invs))

if __name__ == '__main__':
	input = sys.stdin.read()
	data = list(map(int, input.split()))
	a = data[1:]
	n = int(data[0])
	sort_merge,n_c = bin_divide(a,0)
	print (n_c)




