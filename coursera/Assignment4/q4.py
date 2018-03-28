# Uses python3
import sys
num_invs = 0
# sum of values of variable j is answer, figure out the way

def compare_and_merge(left, right):
	if not len(left) or not len(right):
		return left or right
	print (left,right)
	result = []
	i, j = 0, 0
	while (len(result) < len(left) + len(right)):
		if left[i] <= right[j]:
			result.append(left[i])
			i+= 1
		else:
			print(left[i],right[j])
			result.append(right[j])
			j+= 1
			global num_invs
			num_invs +=1
		if i == len(left) or j == len(right):
			result.extend(left[i:] or right[j:])
			break 
		print("================================")	
	return result

def bin_divide(list):
	if len(list) < 2:
		return list

	middle = len(list)//2
	left = bin_divide(list[:middle])
	right = bin_divide(list[middle:])
	return compare_and_merge(left, right)

if __name__ == '__main__':
	input = sys.stdin.read()
	data = list(map(int, input.split()))
	a = data[1:]
	n = int(data[0])
	sort_list = bin_divide(a)
	print (num_invs)
	print(sort_list)




