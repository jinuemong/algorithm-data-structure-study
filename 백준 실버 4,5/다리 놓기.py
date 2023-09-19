

# 다리 놓기
# 겹칠 수 없는 다리

import sys
input = sys.stdin.readline
T =  int(input().strip())

for _ in range(T):
    n,m = list(map(int,input().split()))
    n , m = [i for i in range(1,n+1)] , [i for i in range(1,m+1)]
    print(n,m)