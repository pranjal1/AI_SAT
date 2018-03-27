#using python3

def get_MSB(n):
        while(1):
                rem = n//10
                if (rem==0):
                        return n
                n=rem

i = int(input())
print(get_MSB(i))
