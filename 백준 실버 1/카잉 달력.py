# m = 10 , n = 12
# 1 > 1 : 1
# 2 > 2 : 2
# 11 > 1 : 11
# 12 > 2 : 12
# 13 > 3 : 1

t = int(input())

def find_k(m,n,x,y):
    k = x
    while k <= m*n :
        if (k-x) % m ==0 and (k-y) % n == 0:
            return k
        k += m
    return -1

for _ in range(t):
    m,n,x,y = map(int,input().split())
    print(find_k(m,n,x,y))
