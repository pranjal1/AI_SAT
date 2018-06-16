# Uses python3
import sys
import random
num_invs = 0

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

def compare_and_merge(left, right):
	if not len(left) or not len(right):
		return left or right
	result = []
	i, j = 0, 0
	global num_invs
	while (len(result) < len(left) + len(right)):
		if left[i] <= right[j]:
			result.append(left[i])
			i+= 1
		else:
			result.append(right[j])
			num_invs +=len(left[i:])
			j+= 1
		if i == len(left):
			result.extend(right[j:])
			break
		if j == len(right): 
			#num_invs +=len(left[i+1:])*len(result)
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



if __name__ == '__main__':
	#input = sys.stdin.read()
	#data = list(map(int, input.split()))
	for x in range(0,1000):
		data = random.sample(range(1, 100), 100)
		a = data[1:]
		n = int(data[0])
		#print(a)
		sort_merge = bin_divide(a)
		sort_naive = naive_way(a)
		if (sort_naive-num_invs)!=0:
			print(sort_naive,num_invs)
			print('------------------------')
		num_invs =0



