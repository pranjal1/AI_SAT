
import sys

def naive_count_segments(n,m,starts,ends,points):
	loops = 0
	dictlist = [dict() for x in range(n)]
	for i in range(n):
		for j in range(starts[i],ends[i]+1):
			dictlist[i][j] = 1
			loops+=1
	count = [0  for x in range(len(points))]
	for i in range(len(points)):
		for x in dictlist:
			loops+=1
			tmp = x.get(points[i])
			if tmp is None:
				tmp = 0
			count[i]+=tmp
	print (loops)		
	return count


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[1]
    starts = data[2:2 * n + 2:2]
    ends   = data[3:2 * n + 2:2]
    points = data[2 * n + 2:]
    #use fast_count_segments
    cnt = naive_count_segments(n,m,starts,ends,points)
    for x in cnt:
    	print(x,end = ' ')
'''
3 2
0 5
-3 2
7 10
1 6

1 3
-10 10
-100 100 0

2 3
0 5
7 10
1 6 11
'''