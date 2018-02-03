# Uses python3
n = int(input()) #first line input
a = [int(x) for x in input().split()] #second line inputs
max_arr = 0
for i in a:
        if i > max_arr:
                max_arr = i
a.remove(max_arr)                
sec_max_arr = 0
for i in a:
        if i > sec_max_arr:
                sec_max_arr = i

print(max_arr*sec_max_arr)                
 