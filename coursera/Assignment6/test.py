import sys

def solution(values):
    total = sum(values)
    if len(values) < 3 or total % 3:  # 1
        return False
    third = total // 3
    table = [[0] * (len(values) + 1) for _ in range(third + 1)]  # 2

    for i in range(1, third + 1):
        for j in range(1, len(values) + 1):  # 3
            ii = i - values[j - 1]  # 4
            if values[j - 1] == i or (ii > 0 and table[ii][j - 1]):  # 5
                table[i][j] = 1 if table[i][j - 1] == 0 else 2
            else:
                table[i][j] = table[i][j - 1]  # 6
    print(table)	
    return True if table[-1][-1] == 2 else False

if __name__ == '__main__':
	input = sys.stdin.read()
	n, *w = list(map(int, input.split()))
	print(solution(w))

